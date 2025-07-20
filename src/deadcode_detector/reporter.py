"""
Gerador de Relatórios - Saída formatada dos problemas encontrados
"""

import os
from typing import List, Dict
from colorama import Fore, Back, Style, init
from .analyzer import DeadCodeIssue

init(autoreset=True)


class Reporter:
    """
    Gerador de Relatórios - Formata e exibe os problemas encontrados
    
    Gera relatórios coloridos e bem formatados dos problemas de código morto
    detectados pelo analisador.
    """
    
    def __init__(self, use_colors: bool = True):
        self.use_colors = use_colors
        
    def print_report(self, issues: List[DeadCodeIssue], source_file: str = None):
        if source_file:
            print(f"\n{Fore.CYAN}🔍 Análise de código morto: {source_file}{Style.RESET_ALL}")
            print("=" * 60)
        
        if not issues:
            print(f"{Fore.GREEN}✅ Nenhum problema de código morto encontrado!{Style.RESET_ALL}")
            return
        
        grouped_issues = self._group_issues_by_type(issues)
        
        self._print_summary(issues)
        print()
        
        for issue_type, type_issues in grouped_issues.items():
            self._print_issue_group(issue_type, type_issues)
            print()
    
    def _group_issues_by_type(self, issues: List[DeadCodeIssue]) -> Dict[str, List[DeadCodeIssue]]:
        grouped = {}
        for issue in issues:
            if issue.type not in grouped:
                grouped[issue.type] = []
            grouped[issue.type].append(issue)
        return grouped
    
    def _print_summary(self, issues: List[DeadCodeIssue]):
        total = len(issues)
        
        if self.use_colors:
            print(f"{Fore.YELLOW}📊 Resumo: {total} problema(s) encontrado(s){Style.RESET_ALL}")
        else:
            print(f"📊 Resumo: {total} problema(s) encontrado(s)")
        
        type_counts = {}
        for issue in issues:
            type_counts[issue.type] = type_counts.get(issue.type, 0) + 1
        
        for issue_type, count in type_counts.items():
            type_name = self._get_type_display_name(issue_type)
            if self.use_colors:
                print(f"   • {Fore.RED}{type_name}: {count}{Style.RESET_ALL}")
            else:
                print(f"   • {type_name}: {count}")
    
    def _print_issue_group(self, issue_type: str, issues: List[DeadCodeIssue]):
        type_name = self._get_type_display_name(issue_type)
        
        if self.use_colors:
            print(f"{Fore.RED}⚠️  {type_name.upper()}{Style.RESET_ALL}")
        else:
            print(f"⚠️  {type_name.upper()}")
        
        for issue in issues:
            self._print_issue(issue)
    
    def _print_issue(self, issue: DeadCodeIssue):
        line_info = f"Linha {issue.line}" if issue.line > 0 else "Arquivo"
        
        if self.use_colors:
            print(f"   {Fore.YELLOW}{line_info}:{Style.RESET_ALL} {issue.description}")
        else:
            print(f"   {line_info}: {issue.description}")
    
    def _get_type_display_name(self, issue_type: str) -> str:
        names = {
            'unused_function': 'Função não utilizada',
            'unused_variable': 'Variável não utilizada',
            'unused_import': 'Import não utilizado',
            'always_false_condition': 'Condição sempre falsa',
            'code_after_return': 'Código após return',
            'unreachable_code': 'Código inalcançável',
            'parse_error': 'Erro de análise'
        }
        return names.get(issue_type, issue_type)
    
    def save_report(self, issues: List[DeadCodeIssue], output_file: str, source_file: str = None):
        with open(output_file, 'w', encoding='utf-8') as f:
            original_use_colors = self.use_colors
            self.use_colors = False
            
            import sys
            original_stdout = sys.stdout
            sys.stdout = f
            
            try:
                self.print_report(issues, source_file)
            finally:
                sys.stdout = original_stdout
                self.use_colors = original_use_colors
    
    def print_usage_guide(self):
        print(f"{Fore.CYAN}🔧 DeadCodeDetector - Guia de Uso{Style.RESET_ALL}")
        print("=" * 50)
        print()
        print("Uso básico:")
        print("  python -m deadcode_detector arquivo.py")
        print()
        print("Opções:")
        print("  --output arquivo.txt    Salva relatório em arquivo")
        print("  --no-colors            Desabilita cores na saída")
        print("  --help                 Mostra esta ajuda")
        print()
        print("Exemplos:")
        print("  python -m deadcode_detector exemplo.py")
        print("  python -m deadcode_detector exemplo.py --output relatorio.txt")
        print()
        print("Tipos de problemas detectados:")
        print("  • Funções definidas mas nunca chamadas")
        print("  • Variáveis declaradas mas nunca utilizadas")
        print("  • Imports não utilizados")
        print("  • Condições sempre falsas")
        print("  • Código após declarações return")
        print("  • Código inalcançável")
    
    def print_file_analysis(self, file_path: str, issues: List[DeadCodeIssue]):
        file_name = os.path.basename(file_path)
        
        print(f"\n{Fore.CYAN}📁 Arquivo: {file_name}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}📂 Caminho: {file_path}{Style.RESET_ALL}")
        
        if issues:
            print(f"{Fore.RED}❌ {len(issues)} problema(s) encontrado(s){Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}✅ Nenhum problema encontrado{Style.RESET_ALL}")
        
        self.print_report(issues, file_name) 