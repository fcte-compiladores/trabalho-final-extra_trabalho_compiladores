#!/usr/bin/env python3
"""
Script de Demonstração - DeadCodeDetector
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from deadcode_detector.analyzer import DeadCodeAnalyzer
from deadcode_detector.reporter import Reporter


def demo_basic_analysis():
    print("🔍 DEMONSTRAÇÃO DO DEADCODEDETECTOR")
    print("=" * 50)
    
    code = """
import os  # Import não utilizado
import sys  # Import não utilizado

def funcao_utilizada():
    return "usada"

def funcao_nao_utilizada():
    return "nunca chamada"

def exemplo_problemas():
    x = 10  # Variável não utilizada
    y = 20
    print(y)
    
    if False:
        print("Código morto")
    
    return y
    print("Código após return")

resultado = funcao_utilizada()
exemplo_problemas()
"""
    
    print("Código de exemplo:")
    print(code)
    print("\n" + "=" * 50)
    
    analyzer = DeadCodeAnalyzer()
    reporter = Reporter()
    
    print(" Analisando código...")
    issues = analyzer.analyze(code)
    
    reporter.print_report(issues, "código_exemplo.py")
    
    summary = analyzer.get_summary()
    print(f"\n Estatísticas: {summary}")


def demo_file_analysis():
    print("\n" + "=" * 50)
    print(" ANÁLISE DE ARQUIVOS DE EXEMPLO")
    print("=" * 50)
    
    analyzer = DeadCodeAnalyzer()
    reporter = Reporter()
    
    example_files = [
        "exemplos/dead_code_1.py",
        "exemplos/dead_code_2.py",
        "exemplos/dead_code_3.py",
        "exemplos/complex_example.py"
    ]
    
    for file_path in example_files:
        if os.path.exists(file_path):
            print(f"\n Analisando: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            issues = analyzer.analyze(code)
            reporter.print_report(issues, file_path)
        else:
            print(f"⚠️  Arquivo não encontrado: {file_path}")


def demo_interactive():
    print("\n" + "=" * 50)
    print(" DEMONSTRAÇÃO INTERATIVA")
    print("=" * 50)
    
    print("Digite um código Python para analisar (digite 'SAIR' em uma linha vazia para terminar):")
    print()
    
    lines = []
    while True:
        line = input(">>> ")
        if line.strip() == "SAIR":
            break
        lines.append(line)
    
    if lines:
        code = "\n".join(lines)
        print("\n Analisando seu código...")
        
        analyzer = DeadCodeAnalyzer()
        reporter = Reporter()
        
        issues = analyzer.analyze(code)
        reporter.print_report(issues, "código_interativo.py")


def main():
    """Função principal da demonstração"""
    try:
        demo_basic_analysis()
        
        demo_file_analysis()
        
        print("\n" + "=" * 50)
        resposta = input("Deseja fazer uma demonstração interativa? (s/n): ").lower().strip()
        
        if resposta in ['s', 'sim', 'y', 'yes']:
            demo_interactive()
        
        print("\n✅ Demonstração concluída!")
        print("Para usar o DeadCodeDetector em seus próprios arquivos:")
        print("  python -m deadcode_detector arquivo.py")
        
    except KeyboardInterrupt:
        print("\n\n  Demonstração interrompida pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro durante a demonstração: {e}")


if __name__ == "__main__":
    main() 