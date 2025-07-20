"""
Analisador Sintático - Análise da estrutura do código Python
"""

import ast
from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class FunctionInfo:
    name: str
    line: int
    is_called: bool = False
    calls: List[str] = None
    
    def __post_init__(self):
        if self.calls is None:
            self.calls = []


@dataclass
class VariableInfo:
    name: str
    line: int
    is_used: bool = False
    is_assigned: bool = False


class Parser:
    """
    Analisador Sintático - Constrói AST e analisa estrutura do código
    
    Utiliza o módulo ast do Python para fazer a análise sintática,
    extraindo informações sobre funções, variáveis e estrutura do código.
    """
    
    def __init__(self):
        self.tree: Optional[ast.AST] = None
        self.functions: Dict[str, FunctionInfo] = {}
        self.variables: Dict[str, VariableInfo] = {}
        self.imports: List[str] = []
        self.control_flow: List[Dict] = []
        
    def parse(self, source_code: str) -> ast.AST:
       
        try:
            self.tree = ast.parse(source_code)
            self._analyze_structure()
            return self.tree
        except SyntaxError as e:
            raise ValueError(f"Erro de sintaxe na linha {e.lineno}: {e.text}")
    
    def _analyze_structure(self):
        if not self.tree:
            return
            
        self.functions.clear()
        self.variables.clear()
        self.imports.clear()
        self.control_flow.clear()
        
        for node in ast.walk(self.tree):
            self._visit_node(node)
    
    def _visit_node(self, node: ast.AST):
        if isinstance(node, ast.FunctionDef):
            self._analyze_function_def(node)
        elif isinstance(node, ast.Call):
            self._analyze_function_call(node)
        elif isinstance(node, ast.Assign):
            self._analyze_assignment(node)
        elif isinstance(node, ast.Name):
            self._analyze_name_usage(node)
        elif isinstance(node, ast.Import):
            self._analyze_import(node)
        elif isinstance(node, ast.ImportFrom):
            self._analyze_import_from(node)
        elif isinstance(node, ast.If):
            self._analyze_if_statement(node)
        elif isinstance(node, ast.Return):
            self._analyze_return_statement(node)
    
    def _analyze_function_def(self, node: ast.FunctionDef):
        func_info = FunctionInfo(
            name=node.name,
            line=getattr(node, 'lineno', 0)
        )
        self.functions[node.name] = func_info
        
        for arg in node.args.args:
            var_info = VariableInfo(
                name=arg.arg,
                line=getattr(node, 'lineno', 0),
                is_assigned=True
            )
            self.variables[arg.arg] = var_info
    
    def _analyze_function_call(self, node: ast.Call):
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name in self.functions:
                self.functions[func_name].is_called = True
    
    def _analyze_assignment(self, node: ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id
                if var_name not in self.variables:
                    self.variables[var_name] = VariableInfo(
                        name=var_name,
                        line=getattr(node, 'lineno', 0)
                    )
                self.variables[var_name].is_assigned = True
    
    def _analyze_name_usage(self, node: ast.Name):
        name = node.id
        
        if name in self.variables:
            self.variables[name].is_used = True
        
        if isinstance(node.ctx, ast.Load):
            if name in self.functions:
                self.functions[name].is_called = True
    
    def _analyze_import(self, node: ast.Import):
        for alias in node.names:
            self.imports.append(alias.name)
    
    def _analyze_import_from(self, node: ast.ImportFrom):
        module = node.module or ""
        for alias in node.names:
            self.imports.append(f"{module}.{alias.name}")
    
    def _analyze_if_statement(self, node: ast.If):
        if self._is_always_false(node.test):
            self.control_flow.append({
                'type': 'always_false_condition',
                'line': getattr(node, 'lineno', 0),
                'description': 'Condição sempre falsa'
            })
    
    def _analyze_return_statement(self, node: ast.Return):
        self.control_flow.append({
            'type': 'return_statement',
            'line': getattr(node, 'lineno', 0)
        })
    
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
    
    def get_unused_functions(self) -> List[FunctionInfo]:
        return [func for func in self.functions.values() if not func.is_called]
    
    def get_unused_variables(self) -> List[VariableInfo]:
        return [var for var in self.variables.values() 
                if var.is_assigned and not var.is_used]
    
    def get_unused_imports(self) -> List[str]:
        return self.imports.copy() 