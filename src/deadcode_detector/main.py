"""
Interface Principal - DeadCodeDetector CLI
"""

import sys
import argparse
import os
from pathlib import Path
from typing import List

from .analyzer import DeadCodeAnalyzer
from .reporter import Reporter


def main():
    parser = argparse.ArgumentParser(
        description="DeadCodeDetector - Analisador de código morto para Python",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python -m deadcode_detector exemplo.py
  python -m deadcode_detector exemplo.py --output relatorio.txt
  python -m deadcode_detector exemplo.py --no-colors
        """
    )
    
    parser.add_argument(
        'file',
        help='Arquivo Python para analisar'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Arquivo de saída para salvar o relatório'
    )
    
    parser.add_argument(
        '--no-colors',
        action='store_true',
        help='Desabilita cores na saída'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='DeadCodeDetector 1.0.0'
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"❌ Erro: Arquivo '{args.file}' não encontrado")
        sys.exit(1)
    
    if not args.file.endswith('.py'):
        print(f"⚠️  Aviso: Arquivo '{args.file}' não parece ser um arquivo Python")
    
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        analyzer = DeadCodeAnalyzer()
        reporter = Reporter(use_colors=not args.no_colors)
        
        print("🔍 Analisando código...")
        issues = analyzer.analyze(source_code)
        
        if args.output:
            reporter.save_report(issues, args.output, args.file)
            print(f"📄 Relatório salvo em: {args.output}")
        else:
            reporter.print_file_analysis(args.file, issues)
        
        if issues:
            sys.exit(1)  
        else:
            sys.exit(0)  
            
    except Exception as e:
        print(f"❌ Erro durante a análise: {str(e)}")
        sys.exit(1)


def analyze_file(file_path: str, use_colors: bool = True) -> List:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        analyzer = DeadCodeAnalyzer()
        return analyzer.analyze(source_code)
        
    except Exception as e:
        print(f"❌ Erro ao analisar {file_path}: {str(e)}")
        return []


def analyze_directory(directory: str, use_colors: bool = True) -> dict:
    results = {}
    directory_path = Path(directory)
    
    if not directory_path.exists():
        print(f"❌ Diretório '{directory}' não encontrado")
        return results
    
    python_files = list(directory_path.glob("**/*.py"))
    
    if not python_files:
        print(f"⚠️  Nenhum arquivo Python encontrado em '{directory}'")
        return results
    
    print(f"🔍 Analisando {len(python_files)} arquivo(s) Python...")
    
    for file_path in python_files:
        issues = analyze_file(str(file_path), use_colors)
        results[str(file_path)] = issues
    
    return results


if __name__ == "__main__":
    main() 