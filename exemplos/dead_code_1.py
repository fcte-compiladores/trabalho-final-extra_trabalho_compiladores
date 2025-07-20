"""
Exemplo 1: Problemas básicos de código morto
Complexidade: Básica
"""

import os  # Import não utilizado
import sys  # Import não utilizado

def hello_world():
    """Função simples com código morto"""
    print("Hello, World!")
    return "Hello"
    print("Esta linha nunca será executada")  # Código morto após return

def exemplo_variaveis():
    """Exemplo com variáveis não utilizadas"""
    x = 10  # Variável não utilizada
    y = 20
    print(f"Valor de y: {y}")
    return y

def exemplo_condicao_falsa():
    """Exemplo com condição sempre falsa"""
    if False:
        print("Esta linha nunca será executada")  # Código morto
    
    if 1 == 2:
        print("Esta também nunca será executada")  # Código morto
    
    return "OK"

# Função não utilizada
def funcao_nao_chamada():
    """Esta função nunca é chamada"""
    return "nunca usada"

# Código principal
if __name__ == "__main__":
    hello_world()
    exemplo_variaveis()
    exemplo_condicao_falsa() 