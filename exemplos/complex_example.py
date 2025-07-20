"""
Exemplo 4: Problemas complexos de código morto
Complexidade: Elaborada - Algoritmo de ordenação e busca avançada
"""

import heapq  # Import não utilizado
import itertools  # Import não utilizado
from functools import lru_cache  # Import não utilizado
from typing import List, Tuple, Optional, Dict, Set  # Imports não utilizados

class SistemaGerenciamento:
    """Sistema complexo de gerenciamento com múltiplos problemas"""
    
    def __init__(self):
        self.usuarios = {}
        self.produtos = {}
        self.pedidos = []
        self.configuracoes = {}  # Variável não utilizada
        self.logs = []  # Variável não utilizada
        self.estatisticas = {}  # Variável não utilizada
    
    def cadastrar_usuario(self, id_usuario: int, nome: str, email: str) -> bool:
        """Cadastra um novo usuário"""
        if id_usuario in self.usuarios:
            return False
        
        self.usuarios[id_usuario] = {
            'nome': nome,
            'email': email,
            'ativo': True,
            'data_cadastro': '2024-01-01'  # Valor hardcoded não utilizado
        }
        return True
    
    def cadastrar_produto(self, id_produto: int, nome: str, preco: float) -> bool:
        """Cadastra um novo produto"""
        if id_produto in self.produtos:
            return False
        
        self.produtos[id_produto] = {
            'nome': nome,
            'preco': preco,
            'estoque': 0,
            'categoria': 'geral'  # Valor padrão não utilizado
        }
        return True
    
    def fazer_pedido(self, id_usuario: int, id_produto: int, quantidade: int) -> Optional[int]:
        """Realiza um pedido"""
        if id_usuario not in self.usuarios or id_produto not in self.produtos:
            return None
        
        if quantidade <= 0:
            return None
        
        pedido = {
            'id': len(self.pedidos) + 1,
            'usuario': id_usuario,
            'produto': id_produto,
            'quantidade': quantidade,
            'status': 'pendente',
            'valor_total': self.produtos[id_produto]['preco'] * quantidade
        }
        
        self.pedidos.append(pedido)
        return pedido['id']
    
    def buscar_pedidos_usuario(self, id_usuario: int) -> List[Dict]:
        """Busca todos os pedidos de um usuário"""
        return [pedido for pedido in self.pedidos if pedido['usuario'] == id_usuario]
    
    def calcular_total_vendas(self) -> float:
        """Calcula o total de vendas"""
        total = 0
        for pedido in self.pedidos:
            if pedido['status'] == 'concluido':  # Status não verificado
                total += pedido['valor_total']
        return total
    
    def relatorio_vendas(self) -> Dict:
        """Gera relatório de vendas"""
        vendas_por_produto = {}
        vendas_por_usuario = {}
        
        for pedido in self.pedidos:
            # Produto
            id_produto = pedido['produto']
            if id_produto not in vendas_por_produto:
                vendas_por_produto[id_produto] = 0
            vendas_por_produto[id_produto] += pedido['valor_total']
            
            # Usuário
            id_usuario = pedido['usuario']
            if id_usuario not in vendas_por_usuario:
                vendas_por_usuario[id_usuario] = 0
            vendas_por_usuario[id_usuario] += pedido['valor_total']
        
        return {
            'por_produto': vendas_por_produto,
            'por_usuario': vendas_por_usuario,
            'total': sum(pedido['valor_total'] for pedido in self.pedidos)
        }
    
    def limpar_dados_antigos(self):
        """Método não utilizado"""
        # Lógica para limpar dados antigos
        pass

def algoritmo_ordenacao_avancada(lista: List[int]) -> List[int]:
    """Algoritmo de ordenação híbrido com código morto"""
    if len(lista) <= 1:
        return lista
    
    if len(lista) <= 10:
        # Ordenação por inserção para listas pequenas
        return ordenacao_insercao(lista)
    else:
        # Quicksort para listas grandes
        return quicksort(lista)

def ordenacao_insercao(lista: List[int]) -> List[int]:
    """Ordenação por inserção"""
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

def quicksort(lista: List[int]) -> List[int]:
    """Quicksort com código morto"""
    if len(lista) <= 1:
        return lista
    
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    
    resultado = quicksort(menores) + iguais + quicksort(maiores)
    return resultado
    print("Quicksort concluído")  # Código morto

def busca_avancada(lista: List[int], elemento: int) -> Tuple[bool, int]:
    """Busca avançada com múltiplos algoritmos"""
    if not lista:
        return False, -1
    
    # Busca binária para listas ordenadas
    if lista == sorted(lista):
        return busca_binaria_avancada(lista, elemento)
    
    # Busca linear para listas não ordenadas
    return busca_linear_avancada(lista, elemento)

def busca_binaria_avancada(lista: List[int], elemento: int) -> Tuple[bool, int]:
    """Busca binária avançada"""
    esquerda, direita = 0, len(lista) - 1
    comparacoes = 0  # Variável não utilizada
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1
        
        if lista[meio] == elemento:
            return True, meio
        elif lista[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1
    
    return False, -1

def busca_linear_avancada(lista: List[int], elemento: int) -> Tuple[bool, int]:
    """Busca linear avançada"""
    for i, valor in enumerate(lista):
        if valor == elemento:
            return True, i
    return False, -1

def processar_dados_complexos(dados: List[Dict]) -> Dict:
    """Processamento complexo de dados com variáveis não utilizadas"""
    resultado = {
        'total': 0,
        'media': 0,
        'maximo': float('-inf'),
        'minimo': float('inf'),
        'valores_unicos': set()
    }
    
    contador = 0  # Variável não utilizada
    soma_quadrados = 0  # Variável não utilizada
    
    for item in dados:
        valor = item.get('valor', 0)
        resultado['total'] += valor
        resultado['maximo'] = max(resultado['maximo'], valor)
        resultado['minimo'] = min(resultado['minimo'], valor)
        resultado['valores_unicos'].add(valor)
    
    if dados:
        resultado['media'] = resultado['total'] / len(dados)
    
    return resultado

def validar_dados_avancados(dados: Dict) -> Tuple[bool, List[str]]:
    """Validação avançada de dados com condições sempre falsas"""
    erros = []
    
    # Validações básicas
    if 'nome' not in dados:
        erros.append("Nome é obrigatório")
    
    if 'idade' in dados and dados['idade'] < 0:
        erros.append("Idade deve ser positiva")
    
    if 'email' in dados and '@' not in dados['email']:
        erros.append("Email inválido")
    
    # Condições sempre falsas
    if False:
        erros.append("Erro crítico no sistema")  # Código morto
    
    if 1 == 2:
        erros.append("Erro impossível")  # Código morto
    
    return len(erros) == 0, erros

# Funções auxiliares não utilizadas
def calcular_estatisticas_avancadas(dados: List[float]) -> Dict:
    """Função não utilizada"""
    if not dados:
        return {}
    
    media = sum(dados) / len(dados)
    variancia = sum((x - media) ** 2 for x in dados) / len(dados)
    desvio_padrao = variancia ** 0.5
    
    return {
        'media': media,
        'variancia': variancia,
        'desvio_padrao': desvio_padrao
    }

def exportar_dados(dados: List[Dict], formato: str) -> str:
    """Função não utilizada"""
    if formato == 'json':
        import json
        return json.dumps(dados, indent=2)
    elif formato == 'csv':
        import csv
        # Lógica para CSV
        return "dados.csv"
    else:
        return "formato não suportado"

def main():
    """Função principal com testes complexos"""
    # Teste sistema de gerenciamento
    sistema = SistemaGerenciamento()
    
    # Cadastra usuários e produtos
    sistema.cadastrar_usuario(1, "João", "joao@email.com")
    sistema.cadastrar_usuario(2, "Maria", "maria@email.com")
    sistema.cadastrar_produto(1, "Notebook", 2500.0)
    sistema.cadastrar_produto(2, "Mouse", 50.0)
    
    # Faz pedidos
    sistema.fazer_pedido(1, 1, 1)
    sistema.fazer_pedido(2, 2, 2)
    
    # Testa relatório
    relatorio = sistema.relatorio_vendas()
    print("Relatório de vendas:", relatorio)
    
    # Teste ordenação avançada
    lista_desordenada = [64, 34, 25, 12, 22, 11, 90, 45, 78, 23]
    lista_ordenada = algoritmo_ordenacao_avancada(lista_desordenada.copy())
    print("Lista ordenada:", lista_ordenada)
    
    # Teste busca avançada
    encontrado, posicao = busca_avancada(lista_ordenada, 45)
    print(f"Elemento 45 encontrado: {encontrado} na posição {posicao}")
    
    # Teste processamento de dados
    dados_teste = [
        {'valor': 10}, {'valor': 20}, {'valor': 15}, {'valor': 25}
    ]
    resultado_processamento = processar_dados_complexos(dados_teste)
    print("Resultado processamento:", resultado_processamento)
    
    # Teste validação avançada
    dados_validacao = {
        'nome': 'Teste',
        'idade': 25,
        'email': 'teste@email.com'
    }
    valido, erros = validar_dados_avancados(dados_validacao)
    print(f"Dados válidos: {valido}, Erros: {erros}")

if __name__ == "__main__":
    main() 