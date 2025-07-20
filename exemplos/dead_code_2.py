"""
Exemplo 2: Problemas intermediários de código morto
Complexidade: Intermediária
"""

import math  # Import não utilizado
import random  # Import não utilizado
from typing import List, Dict  # Imports não utilizados

class Calculadora:
    """Classe com métodos não utilizados"""
    
    def __init__(self):
        self.historico = []  # Variável não utilizada
        self.ultimo_resultado = 0
    
    def soma(self, a, b):
        """Método utilizado"""
        resultado = a + b
        self.ultimo_resultado = resultado
        return resultado
    
    def subtracao(self, a, b):
        """Método não utilizado"""
        return a - b
    
    def multiplicacao(self, a, b):
        """Método não utilizado"""
        return a * b
    
    def divisao(self, a, b):
        """Método não utilizado"""
        if b == 0:
            return None
        return a / b

def fibonacci(n):
    """Função recursiva com código morto"""
    if n <= 1:
        return n
    
    resultado = fibonacci(n-1) + fibonacci(n-2)
    return resultado
    print("Esta linha nunca será executada")  # Código morto

def processar_lista(lista):
    """Função com variáveis não utilizadas"""
    tamanho = len(lista)  # Variável não utilizada
    soma = 0
    contador = 0  # Variável não utilizada
    
    for item in lista:
        soma += item
    
    return soma

def validar_email(email):
    """Função com condição sempre falsa"""
    if "@" not in email:
        return False
    
    if len(email) < 5:
        return False
    
    if False:  # Condição sempre falsa
        print("Email inválido por algum motivo")  # Código morto
    
    return True

# Funções auxiliares não utilizadas
def formatar_data(data):
    """Função não utilizada"""
    return data.strftime("%d/%m/%Y")

def calcular_media(numeros):
    """Função não utilizada"""
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def main():
    """Função principal"""
    calc = Calculadora()
    resultado = calc.soma(10, 20)
    print(f"Resultado: {resultado}")
    
    # Teste com lista
    numeros = [1, 2, 3, 4, 5]
    total = processar_lista(numeros)
    print(f"Total: {total}")
    
    # Teste fibonacci
    fib = fibonacci(10)
    print(f"Fibonacci(10): {fib}")
    
    # Teste validação email
    email_valido = validar_email("teste@exemplo.com")
    print(f"Email válido: {email_valido}")

if __name__ == "__main__":
    main() 