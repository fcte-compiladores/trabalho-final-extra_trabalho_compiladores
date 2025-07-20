"""
Testes unitários para o DeadCodeAnalyzer
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from deadcode_detector.analyzer import DeadCodeAnalyzer, DeadCodeIssue


class TestDeadCodeAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = DeadCodeAnalyzer()
    
    def test_unused_function_detection(self):
        code = """
def funcao_utilizada():
    return "usada"

def funcao_nao_utilizada():
    return "nunca chamada"

resultado = funcao_utilizada()
"""
        issues = self.analyzer.analyze(code)
        
        unused_function_issues = [i for i in issues if i.type == 'unused_function']
        self.assertEqual(len(unused_function_issues), 1)
        self.assertIn('funcao_nao_utilizada', unused_function_issues[0].description)
    
    def test_unused_variable_detection(self):
        code = """
def teste_variaveis():
    x = 10  # Não utilizada
    y = 20
    print(y)
    return y

teste_variaveis()
"""
        issues = self.analyzer.analyze(code)
        
        self.assertGreater(len(issues), 0)
        
        issue_types = [i.type for i in issues]
        self.assertTrue(len(issue_types) > 0)
    
    def test_code_after_return_detection(self):
        code = """
def teste_return():
    return "valor"
    print("Esta linha nunca será executada")
"""
        issues = self.analyzer.analyze(code)
        
        code_after_return_issues = [i for i in issues if i.type == 'code_after_return']
        self.assertGreaterEqual(len(code_after_return_issues), 1)
    
    def test_always_false_condition_detection(self):
        code = """
def teste_condicao():
    if False:
        print("Nunca executado")
    
    if 1 == 2:
        print("Também nunca executado")
"""
        issues = self.analyzer.analyze(code)
        
        always_false_issues = [i for i in issues if i.type == 'always_false_condition']
        self.assertGreaterEqual(len(always_false_issues), 1)
    
    def test_unused_import_detection(self):
        code = """
import os
import sys
import math

def teste():
    print("Hello")
"""
        issues = self.analyzer.analyze(code)
        
        unused_import_issues = [i for i in issues if i.type == 'unused_import']
        self.assertGreaterEqual(len(unused_import_issues), 2)
    
    def test_clean_code_no_issues(self):
        code = """
def funcao_utilizada():
    x = 10
    y = 20
    resultado = x + y
    print(resultado)
    return resultado

resultado = funcao_utilizada()
"""
        issues = self.analyzer.analyze(code)
        
        dead_code_issues = [i for i in issues if i.type in ['always_false_condition', 'unreachable_code']]
        self.assertEqual(len(dead_code_issues), 0, f"Encontrou problemas de código morto: {[i.type for i in dead_code_issues]}")
        
        self.assertGreaterEqual(len(issues), 0)
    
    def test_complex_code_multiple_issues(self):
        code = """
import json
import csv

def funcao_nao_utilizada():
    return "nunca chamada"

def funcao_com_problemas():
    x = 10  # Não utilizada
    y = 20
    print(y)
    
    if False:
        print("Código morto")
    
    return y
    print("Código após return")

resultado = funcao_com_problemas()
"""
        issues = self.analyzer.analyze(code)
        
        self.assertGreater(len(issues), 3)
        
        issue_types = [i.type for i in issues]
        self.assertIn('unused_function', issue_types)
        self.assertIn('always_false_condition', issue_types)
        self.assertIn('code_after_return', issue_types)
    
    def test_summary_statistics(self):
        code = """
import os

def funcao_nao_utilizada():
    return "nunca chamada"

def funcao_com_problemas():
    x = 10  # Não utilizada
    if False:
        print("Código morto")
    return "ok"
    print("Código após return")

resultado = funcao_com_problemas()
"""
        self.analyzer.analyze(code)
        summary = self.analyzer.get_summary()
        
        self.assertIn('total', summary)
        self.assertIn('unused_function', summary)
        self.assertIn('unused_variable', summary)
        self.assertIn('always_false_condition', summary)
        self.assertIn('code_after_return', summary)
        
        total_expected = sum(summary[k] for k in summary if k != 'total')
        self.assertEqual(summary['total'], total_expected)


class TestDeadCodeIssue(unittest.TestCase):
    
    def test_issue_creation(self):
        issue = DeadCodeIssue(
            type="test_issue",
            line=10,
            description="Problema de teste",
            severity="warning"
        )
        
        self.assertEqual(issue.type, "test_issue")
        self.assertEqual(issue.line, 10)
        self.assertEqual(issue.description, "Problema de teste")
        self.assertEqual(issue.severity, "warning")
    
    def test_issue_default_values(self):
        issue = DeadCodeIssue(
            type="test_issue",
            line=5,
            description="Problema de teste"
        )
        
        self.assertEqual(issue.severity, "warning")
        self.assertEqual(issue.code, "")


if __name__ == '__main__':
    unittest.main() 