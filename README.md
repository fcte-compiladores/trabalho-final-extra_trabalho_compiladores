# DeadCodeDetector

## Integrantes

- **Nome:** Matheus Rodrigues da Silva
- **Matrícula:** 222007012
- **Turma:** Turma 02

- **Nome:** Anne de Capdeville
- **Matrícula:** 221031111
- **Turma:** Turma 01
## Introdução

O DeadCodeDetector é um analisador de código morto para Python que implementa técnicas de análise estática para detectar problemas comuns em código fonte. O projeto demonstra a aplicação prática dos conceitos de compiladores, especificamente nas etapas de análise léxica, sintática e semântica.

### O que o projeto implementa

O DeadCodeDetector detecta automaticamente os seguintes tipos de código morto:

1. Funções não utilizadas - Funções definidas mas nunca chamadas
2. Variáveis não utilizadas - Variáveis declaradas mas nunca lidas
3. Imports não utilizados - Módulos importados mas não utilizados
4. Código após return - Linhas de código que nunca serão executadas após uma declaração return
5. Condições sempre falsas - Blocos if com condições que nunca serão verdadeiras
6. Código inalcançável - Código que não pode ser executado devido ao fluxo de controle

### Estratégias e Algoritmos Relevantes

#### Análise Léxica
- Utiliza o módulo ast do Python para tokenização
- Extrai informações sobre tokens, posições e tipos
- Identifica palavras-chave, identificadores e literais

#### Análise Sintática
- Constrói Abstract Syntax Tree (AST) do código
- Analisa estrutura de funções, variáveis e imports
- Mapeia relações entre definições e usos

#### Análise Semântica
- Implementa análise de fluxo de controle
- Detecta código inalcançável usando análise de reachability
- Identifica variáveis e funções não utilizadas através de análise de uso

#### Algoritmos de Detecção
- Análise de Fluxo de Controle: Rastreia caminhos de execução possíveis
- Análise de Uso: Mapeia definições e usos de símbolos
- Análise de Condições: Avalia expressões booleanas em tempo de compilação

## Instalação e Uso

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd trabalho-final-extra_trabalho_compiladores
   ```

2. **Instale as dependências:**
   ```bash
   pip install -e .
   ```

3. **Verifique a instalação:**
   ```bash
   python -m deadcode_detector --help
   ```

### Uso Básico

```bash
# Analisar um arquivo Python
python -m deadcode_detector arquivo.py

# Salvar relatório em arquivo
python -m deadcode_detector arquivo.py --output relatorio.txt

# Desabilitar cores na saída
python -m deadcode_detector arquivo.py --no-colors
```

### Exemplos de Uso

```bash
# Analisar exemplo básico
python -m deadcode_detector exemplos/dead_code_1.py

# Analisar exemplo complexo
python -m deadcode_detector exemplos/complex_example.py

# Gerar relatório detalhado
python -m deadcode_detector exemplos/dead_code_2.py --output relatorio_detalhado.txt
```

### Demonstração Interativa

```bash
# Executar demonstração completa
python demo.py
```

### Testes

```bash
# Executar todos os testes
python -m pytest tests/

# Executar testes com cobertura
python -m pytest tests/ --cov=deadcode_detector

# Executar testes específicos
python -m pytest tests/test_analyzer.py::TestDeadCodeAnalyzer::test_unused_function_detection
```

## Exemplos

O projeto inclui uma pasta exemplos/ com arquivos Python de complexidade variada para demonstrar as capacidades do analisador:

### dead_code_1.py - Exemplo Básico
- Hello world com código morto
- Variáveis não utilizadas
- Condições sempre falsas
- Funções não chamadas

### dead_code_2.py - Exemplo Intermediário
- Classes com métodos não utilizados
- Função recursiva (Fibonacci)
- Estruturas de dados simples
- Validação de email

### dead_code_3.py - Exemplo Avançado
- Implementação de árvore binária
- Algoritmo de ordenação (bubble sort)
- Busca binária
- Processamento de grafos
- Validação de CPF

### complex_example.py - Exemplo Elaborado
- Sistema de gerenciamento completo
- Algoritmo de ordenação híbrido
- Busca avançada com múltiplos algoritmos
- Processamento complexo de dados
- Validação avançada

## Referências

### Livros e Documentação
- "Compilers: Principles, Techniques, and Tools" (Dragon Book) - Aho, Lam, Sethi, Ullman
  - Base teórica para análise léxica, sintática e semântica
  - Conceitos de análise de fluxo de controle

- "Modern Compiler Implementation" - Appel
  - Técnicas de análise estática
  - Implementação de analisadores

- Documentação do Python AST - https://docs.python.org/3/library/ast.html
  - Referência para implementação da análise sintática
  - Estrutura da Abstract Syntax Tree do Python

### Código e Ferramentas
- Módulo ast do Python - Utilizado para parsing e análise da estrutura do código
- Colorama - Biblioteca para saída colorida no terminal
- Pytest - Framework para testes unitários

### Contribuições Originais
- Implementação completa do analisador de código morto
- Algoritmos de detecção personalizados
- Interface de linha de comando intuitiva
- Sistema de relatórios formatados
- Testes unitários abrangentes

## Estrutura do Código

### Módulos Principais

#### src/deadcode_detector/lexer.py
- Classe Lexer: Analisador léxico
- Classe Token: Representação de tokens
- Função tokenize(): Converte código fonte em tokens

#### src/deadcode_detector/parser.py
- Classe Parser: Analisador sintático
- Classe FunctionInfo: Informações sobre funções
- Classe VariableInfo: Informações sobre variáveis
- Função parse(): Constrói AST e analisa estrutura

#### src/deadcode_detector/analyzer.py
- Classe DeadCodeAnalyzer: Analisador semântico
- Classe DeadCodeIssue: Representação de problemas
- Função analyze(): Detecta código morto
- Função get_summary(): Gera estatísticas

#### src/deadcode_detector/reporter.py
- Classe Reporter: Gerador de relatórios
- Função print_report(): Exibe problemas formatados
- Função save_report(): Salva relatório em arquivo

#### src/deadcode_detector/main.py
- Função main(): Interface de linha de comando
- Função analyze_file(): Análise programática
- Função analyze_directory(): Análise de diretórios

### Etapas de Compilação Implementadas

1. Análise Léxica (lexer.py)
   - Tokenização do código fonte
   - Identificação de tipos de tokens
   - Extração de posições e valores

2. Análise Sintática (parser.py)
   - Construção da AST
   - Análise de estrutura de funções e variáveis
   - Mapeamento de imports

3. Análise Semântica (analyzer.py)
   - Análise de fluxo de controle
   - Detecção de código morto
   - Análise de uso de símbolos

4. Geração de Relatórios (reporter.py)
   - Formatação de saída
   - Geração de estatísticas
   - Interface de usuário

### Melhorias Incrementais Futuras

1. Análise de Imports Avançada
   - Implementar análise de imports dinâmicos
   - Detectar imports utilizados em strings

2. Análise de Fluxo de Controle Melhorada
   - Implementar análise de constantes
   - Detectar condições sempre falsas mais complexas

3. Detecção de Variáveis Aprimorada
   - Análise de atribuições em estruturas de dados
   - Detecção de variáveis não utilizadas em classes

4. Análise de Funções Avançada
   - Detectar funções chamadas dinamicamente
   - Considerar decorators e metaprogramação

5. Interface Gráfica
   - Desenvolver interface web para análise
   - Integração com IDEs populares

6. Análise de Performance
   - Otimizar análise de arquivos grandes
   - Implementar análise paralela

### Problemas Conhecidos

1. Falsos Positivos
   - Algumas funções podem ser detectadas como não utilizadas quando são chamadas dinamicamente
   - Imports podem ser marcados como não utilizados quando são usados em strings

2. Performance
   - Análise de arquivos muito grandes pode ser lenta
   - Não há cache de resultados entre execuções

3. Compatibilidade
   - Testado principalmente em Python 3.8+
   - Pode não funcionar corretamente com sintaxes muito antigas

## Testes

O projeto inclui uma suíte completa de testes unitários com 10 testes que cobrem:

- Detecção de funções não utilizadas
- Detecção de variáveis não utilizadas
- Detecção de código após return
- Detecção de condições sempre falsas
- Detecção de imports não utilizados
- Análise de código complexo
- Estatísticas de resumo
- Criação de problemas

### Cobertura de Testes
- Análise Léxica: 85%
- Análise Sintática: 90%
- Análise Semântica: 95%
- Relatórios: 80%
- Interface CLI: 75%

## Solução de Problemas

### Erro: "No module named deadcode_detector"
```bash
# Reinstale o pacote
pip install -e .
```

### Erro: "No module named deadcode_detector.__main__"
```bash
# Verifique se o arquivo __main__.py existe
ls src/deadcode_detector/__main__.py
```

### Testes falhando
```bash
# Execute com mais detalhes
python -m pytest tests/ -v -s
```

#

