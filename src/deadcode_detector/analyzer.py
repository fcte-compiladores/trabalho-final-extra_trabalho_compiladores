"""
Analisador Semântico - Detecção de código morto
"""

import ast
from typing import List, Dict, Any, Set
from dataclasses import dataclass
from .parser import Parser, FunctionInfo, VariableInfo


@dataclass
class DeadCodeIssue:
    type: str
    line: int
    description: str
    severity: str = "warning"
    code: str = ""


class DeadCodeAnalyzer:
    """
    Analisador Semântico - Detecta código morto usando análise de fluxo de controle
    
    Implementa análise semântica para detectar:
    - Código após return
    - Condições sempre falsas
    - Funções nunca chamadas
    - Variáveis não utilizadas
    - Imports não utilizados
    """
    
    def __init__(self):
        self.parser = Parser()
        self.issues: List[DeadCodeIssue] = []
        self.reachable_lines: Set[int] = set()
        self.unreachable_lines: Set[int] = set()
        
    def analyze(self, source_code: str) -> List[DeadCodeIssue]:
        """
        Analisa o código fonte em busca de código morto
        
        Args:
            source_code: Código Python como string
            
        Returns:
            Lista de problemas encontrados
        """
        self.issues = []
        self.reachable_lines.clear()
        self.unreachable_lines.clear()
        
        try:
            tree = self.parser.parse(source_code)
            
            self._analyze_control_flow(tree, source_code)
            
            self._detect_unused_functions()
            self._detect_unused_variables()
            self._detect_unused_imports()
            self._detect_always_false_conditions(tree)
            self._detect_code_after_return(tree, source_code)
            
        except Exception as e:
            self.issues.append(DeadCodeIssue(
                type="parse_error",
                line=0,
                description=f"Erro ao analisar código: {str(e)}",
                severity="error"
            ))
        
        return self.issues
    
    def _analyze_control_flow(self, tree: ast.AST, source_code: str):
        """Analisa o fluxo de controle do código"""
        lines = source_code.split('\n')
        
        for node in ast.walk(tree):
            if hasattr(node, 'lineno'):
                line_num = node.lineno
                
                if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef)):
                    self.reachable_lines.add(line_num)
                
                if isinstance(node, ast.If):
                    self._analyze_if_flow(node, lines)
                elif isinstance(node, ast.Return):
                    self._analyze_return_flow(node, lines)
    
    def _analyze_if_flow(self, node: ast.If, lines: List[str]):
        """Analisa fluxo de controle em declarações if"""
        if_line = node.lineno
        
        if self._is_always_false(node.test):
            for child in ast.walk(node):
                if hasattr(child, 'lineno') and child.lineno > if_line:
                    self.unreachable_lines.add(child.lineno)
        else:
            for child in ast.walk(node):
                if hasattr(child, 'lineno'):
                    self.reachable_lines.add(child.lineno)
    
    def _analyze_return_flow(self, node: ast.Return, lines: List[str]):
        """Analisa fluxo de controle após declarações return"""
        return_line = node.lineno
        
        for i in range(return_line, len(lines)):
            line_num = i + 1 
            if line_num not in self.reachable_lines:
                self.unreachable_lines.add(line_num)
    
    def _detect_unused_functions(self):
        """Detecta funções que não são chamadas"""
        unused_functions = self.parser.get_unused_functions()
        
        for func in unused_functions:
            self.issues.append(DeadCodeIssue(
                type="unused_function",
                line=func.line,
                description=f"Função '{func.name}' definida mas nunca chamada",
                severity="warning"
            ))
    
    def _detect_unused_variables(self):
        """Detecta variáveis que não são utilizadas"""
        unused_variables = self.parser.get_unused_variables()
        
        for var in unused_variables:
            self.issues.append(DeadCodeIssue(
                type="unused_variable",
                line=var.line,
                description=f"Variável '{var.name}' declarada mas nunca utilizada",
                severity="warning"
            ))
    
    def _detect_unused_imports(self):
        """Detecta imports que não são utilizados"""
        unused_imports = self.parser.get_unused_imports()
        
        for import_name in unused_imports:
            self.issues.append(DeadCodeIssue(
                type="unused_import",
                line=0, 
                description=f"Import '{import_name}' não utilizado",
                severity="warning"
            ))
    
    def _detect_always_false_conditions(self, tree: ast.AST):
        """Detecta condições que são sempre falsas"""
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                if self._is_always_false(node.test):
                    self.issues.append(DeadCodeIssue(
                        type="always_false_condition",
                        line=node.lineno,
                        description="Condição sempre falsa - código nunca será executado",
                        severity="warning"
                    ))
    
    def _detect_code_after_return(self, tree: ast.AST, source_code: str):
        """Detecta código após declarações return"""
        lines = source_code.split('\n')
        return_lines = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Return):
                return_lines.append(node.lineno)
        
        for return_line in return_lines:
            for i in range(return_line, len(lines)):
                line_num = i + 1
                line_content = lines[i].strip()
                
                if (line_content and 
                    not line_content.startswith('#') and
                    not line_content.startswith('"""') and
                    not line_content.startswith("'''")):
                    
                    if not self._is_control_structure_start(line_content):
                        self.issues.append(DeadCodeIssue(
                            type="code_after_return",
                            line=line_num,
                            description="Código após return - nunca será executado",
                            severity="warning"
                        ))
                        break
    
    def _is_always_false(self, test: ast.expr) -> bool:
        if isinstance(test, ast.Constant):
            return test.value is False
        elif isinstance(test, ast.Compare):
            if len(test.ops) == 1 and len(test.comparators) == 1:
                op = test.ops[0]
                left = test.left
                right = test.comparators[0]
                
                if isinstance(op, ast.Eq):
                    if isinstance(left, ast.Constant) and isinstance(right, ast.Constant):
                        return left.value != right.value
                elif isinstance(op, ast.NotEq):
                    if isinstance(left, ast.Constant) and isinstance(right, ast.Constant):
                        return left.value == right.value
        return False
    
    def _is_control_structure_start(self, line: str) -> bool:
        control_keywords = ['if', 'elif', 'else', 'for', 'while', 'try', 'except', 'finally', 'with']
        return any(line.startswith(keyword) for keyword in control_keywords)
    
    def get_summary(self) -> Dict[str, int]:
        summary = {
            'total': len(self.issues),
            'unused_function': 0,
            'unused_variable': 0,
            'unused_import': 0,
            'always_false_condition': 0,
            'code_after_return': 0,
            'unreachable_code': 0
        }
        
        for issue in self.issues:
            if issue.type in summary:
                summary[issue.type] += 1
        
        return summary 