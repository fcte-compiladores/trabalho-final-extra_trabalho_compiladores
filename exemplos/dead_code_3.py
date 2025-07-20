"""
Exemplo 3: Problemas avançados de código morto
Complexidade: Avançada
"""

import json  # Import não utilizado
import csv  # Import não utilizado
from datetime import datetime  # Import não utilizado
from collections import defaultdict, Counter  # Imports não utilizados

class ArvoreBinaria:
    """Implementação de árvore binária com código morto"""
    
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 0  # Variável não utilizada
        self.peso = 1  # Variável não utilizada
    
    def inserir(self, valor):
        """Insere valor na árvore"""
        if valor < self.valor:
            if self.esquerda is None:
                self.esquerda = ArvoreBinaria(valor)
            else:
                self.esquerda.inserir(valor)
        else:
            if self.direita is None:
                self.direita = ArvoreBinaria(valor)
            else:
                self.direita.inserir(valor)
    
    def buscar(self, valor):
        """Busca valor na árvore"""
        if self.valor == valor:
            return True
        
        if valor < self.valor and self.esquerda:
            return self.esquerda.buscar(valor)
        elif valor > self.valor and self.direita:
            return self.direita.buscar(valor)
        
        return False
    
    def percorrer_em_ordem(self):
        """Percorre a árvore em ordem"""
        resultado = []
        if self.esquerda:
            resultado.extend(self.esquerda.percorrer_em_ordem())
        resultado.append(self.valor)
        if self.direita:
            resultado.extend(self.direita.percorrer_em_ordem())
        return resultado
    
    def calcular_altura(self):
        """Método não utilizado"""
        altura_esq = self.esquerda.calcular_altura() if self.esquerda else 0
        altura_dir = self.direita.calcular_altura() if self.direita else 0
        return max(altura_esq, altura_dir) + 1

def ordenacao_bolha(lista):
    """Algoritmo de ordenação com código morto"""
    n = len(lista)
    trocas = 0  # Variável não utilizada
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    
    return lista
    print("Ordenação concluída")  # Código morto após return

def busca_binaria(lista, elemento):
    """Busca binária com condição sempre falsa"""
    esquerda = 0
    direita = len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    if False:  # Condição sempre falsa
        print("Elemento não encontrado")  # Código morto
    
    return -1

def processar_grafo(grafo):
    """Processamento de grafo com variáveis não utilizadas"""
    nos_visitados = set()
    fila = []
    profundidade = 0  # Variável não utilizada
    largura = 0  # Variável não utilizada
    
    # BFS simples
    for no in grafo:
        if no not in nos_visitados:
            fila.append(no)
            nos_visitados.add(no)
            
            while fila:
                atual = fila.pop(0)
                for vizinho in grafo[atual]:
                    if vizinho not in nos_visitados:
                        nos_visitados.add(vizinho)
                        fila.append(vizinho)
    
    return list(nos_visitados)

def validar_cpf(cpf):
    """Validação de CPF com código morto"""
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    # Calcula segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    # Verifica se os dígitos estão corretos
    if cpf[-2:] == f"{digito1}{digito2}":
        return True
    
    return False
    print("CPF inválido")  # Código morto após return

# Funções auxiliares não utilizadas
def calcular_distancia(ponto1, ponto2):
    """Função não utilizada"""
    return ((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)**0.5

def converter_para_maiusculas(texto):
    """Função não utilizada"""
    return texto.upper()

def main():
    """Função principal"""
    # Teste árvore binária
    arvore = ArvoreBinaria(10)
    arvore.inserir(5)
    arvore.inserir(15)
    arvore.inserir(3)
    arvore.inserir(7)
    
    print("Árvore em ordem:", arvore.percorrer_em_ordem())
    print("Busca 7:", arvore.buscar(7))
    
    # Teste ordenação
    lista = [64, 34, 25, 12, 22, 11, 90]
    ordenada = ordenacao_bolha(lista.copy())
    print("Lista ordenada:", ordenada)
    
    # Teste busca binária
    lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    posicao = busca_binaria(lista_ordenada, 7)
    print("Posição do 7:", posicao)
    
    # Teste grafo
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    nos = processar_grafo(grafo)
    print("Nós visitados:", nos)
    
    # Teste CPF
    cpf_valido = validar_cpf("123.456.789-09")
    print("CPF válido:", cpf_valido)

if __name__ == "__main__":
    main() 