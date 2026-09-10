[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://github.com/asessagit/python-lab)
[![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange?logo=jupyter)](https://github.com/asessagit/python-lab/tree/master/Algoritmos/Estrutura_Seleção_Repetição_Multipla_Escolha)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://github.com/asessagit/python-lab/tree/master/.devcontainer)
[![DevContainer](https://img.shields.io/badge/devcontainer-ready-green?logo=docker)](https://github.com/asessagit/python-lab/tree/master/.devcontainer)
[![License](https://img.shields.io/badge/license-MIT-yellow)](https://github.com/asessagit/python-lab/blob/master/LICENSE)

# 🐍 Python Lab — Fundamentos e Lógica de Programação

Espaço dedicado a experimentos, estudos e pequenos projetos em Python. Reúne exemplos práticos, exercícios e implementações simples para explorar conceitos fundamentais da linguagem — estruturas de controle, funções, manipulação de dados e lógica de programação.

Os algoritmos estão organizados por **tópico de estudo**, dentro da pasta `Algoritmos/`.

## 📂 Estrutura do repositório

```
python-lab/
├── .devcontainer/                                    # Ambiente de desenvolvimento containerizado (Docker + VS Code)
│   ├── Dockerfile
│   └── devcontainer.json
├── .gitignore
├── LICENSE                                            # Licença MIT do projeto
├── requirements.txt                                   # Dependências Python do projeto
└── Algoritmos/
    ├── Estrutura_Conjunto_Dados/                       # Listas, vetores e matrizes
    │   ├── Vetores/
    │   │   ├── advinha_vetor.py          # Jogo de adivinhação com histórico de chutes (vetor)
    │   │   ├── vecmedia.py               # Média de notas de alunos usando vetores
    │   │   ├── vecnegativo.py            # Geração de aleatórios e substituição de negativos
    │   │   ├── vecpar.py                 # Verificação de números pares e multiplicação por 2
    │   │   └── vecvendas.py              # Variação de estoque de produtos usando vetores
    │   └── Matrizes/
    │       ├── matmultiplica.py                  # Multiplicação de matriz 5x5 — versão inicial
    │       ├── matmultiplica_dinamico.py         # Multiplicação de matriz — tamanho definido pelo usuário
    │       ├── matmultiplica_refatorado.py       # Multiplicação de matriz 5x5 — com list comprehension
    │       ├── matsoma.py                        # Soma de matriz 4x2 — versão inicial
    │       ├── matsoma_condicao_10.py            # Soma condicional: +2 aos elementos de matriz 4x4 > 10
    │       ├── matsoma_condicao_10_dinamico.py   # Soma condicional dinâmica, com estatísticas e tabela formatada
    │       ├── matsoma_condicao_10_refat.py      # Soma condicional 4x4, refatorada com estatísticas
    │       ├── matsoma_dinamico.py               # Soma, média, maior e menor elemento de matriz NxM
    │       └── matsoma_refatorado.py             # Soma de matriz 4x2 — com validação de entrada
    ├── Estrutura_Seleção_Repetição_Multipla_Escolha/   # Condicionais, laços e múltipla escolha
    │   ├── Lab.ipynb                     # Notebook Jupyter com experimentos e anotações de estudo
    │   ├── advinha.py                    # Jogo de adivinhação — versão inicial (while)
    │   ├── advinha_for.py                # Jogo de adivinhação — refatorado para usar for/else
    │   ├── advinha_for_refatorado.py     # Jogo de adivinhação — versão comentada linha a linha
    │   └── lab.py                        # Resolução de equações do 2º grau (raízes reais e complexas)
    └── Modularizacao/                                  # Funções e procedimentos reutilizáveis
        ├── func_calcular_media.py            # Função que calcula a média de uma lista de números
        ├── func_calcular_media_refat.py       # Versão refatorada, com validação de entrada e mais estatísticas
        ├── proc_calcular_valor.py             # Procedimento que aplica desconto por faixa de valor
        └── proc_calcular_valor_refat.py       # Versão refatorada, com validação de entrada e ternário
```

## 🎮 Estrutura Conjunto de Dados

Algoritmos que trabalham com **listas, vetores e matrizes**.

### Jogo de adivinhação (evolução progressiva)
Os quatro arquivos `advinha*` implementam o mesmo jogo — o programa sorteia um número entre 0 e 100 e o jogador tenta acertar em até 10 tentativas — em estágios diferentes de refatoração. Só `advinha_vetor.py` usa de fato uma estrutura de dados (por isso está em `Estrutura_Conjunto_Dados/Vetores/`); os outros três moram em `Estrutura_Seleção_Repetição_Multipla_Escolha/`, pois praticam apenas laços e condicionais:

| Arquivo | Pasta | Conceito praticado |
|---|---|---|
| `advinha.py` | Seleção/Repetição | Laço `while`, controle manual do contador de chances |
| `advinha_for.py` | Seleção/Repetição | Laço `for` com `range()` decrescente e cláusula `for...else` |
| `advinha_for_refatorado.py` | Seleção/Repetição | Mesma lógica do `for`, totalmente comentada linha a linha (fins didáticos) |
| `advinha_vetor.py` | Conjunto de Dados → Vetores | Uso de lista (vetor) para guardar o histórico de chutes e evitar repetições |

### Vetores
- **`vecmedia.py`** — Lê duas notas de 60 alunos, calcula a média individual de cada um e a média geral da turma.
- **`vecvendas.py`** — Compara o estoque anterior e atual de 5 produtos e informa entradas, saídas ou estabilidade no estoque.
- **`vecnegativo.py`** — Gera 10 números aleatórios entre -10 e 10 e substitui os valores negativos por 1.
- **`vecpar.py`** — Lê números digitados pelo usuário (até que 0 seja informado) e multiplica por 2 os que forem pares.

### Matrizes — Multiplicação
Os três arquivos `matmultiplica*` resolvem o mesmo problema — multiplicar uma matriz por um número inteiro — em estágios diferentes de refatoração:

| Arquivo | Conceito praticado |
|---|---|
| `matmultiplica.py` | Matriz 5x5 de tamanho fixo, preenchida e multiplicada com laços `for` aninhados tradicionais |
| `matmultiplica_dinamico.py` | Tamanho da matriz definido pelo usuário (linhas/colunas), preenchimento com list comprehension |
| `matmultiplica_refatorado.py` | Matriz 5x5 fixa, reescrita com list comprehension dupla e totalmente comentada |

### Matrizes — Soma
Os seis arquivos `matsoma*` exploram a soma de elementos de uma matriz, em duas famílias — soma simples e soma condicional — cada uma evoluindo em complexidade:

| Arquivo | Conceito praticado |
|---|---|
| `matsoma.py` | Matriz 4x2 fixa, soma calculada com laços `for` aninhados tradicionais |
| `matsoma_refatorado.py` | Matriz 4x2, versão refatorada com validação de entrada (aceita vírgula decimal) e exibição em tabela |
| `matsoma_dinamico.py` | Matriz NxM dinâmica, com validação de entrada, soma, média, maior/menor elemento e tabela formatada |
| `matsoma_condicao_10.py` | Matriz 4x4, soma condicional (+2 aos elementos maiores que 10) |
| `matsoma_condicao_10_refat.py` | Matriz 4x4 com regra condicional, refatorada com estatísticas (soma, média, máximo, mínimo) |
| `matsoma_condicao_10_dinamico.py` | Matriz NxM com regra condicional, validação de entrada, estatísticas, soma por linha/coluna e tabela formatada |

## 🔀 Estrutura Seleção, Repetição, Múltipla Escolha

Algoritmos que trabalham com **condicionais, laços e múltipla escolha**, sem depender de uma estrutura de dados para funcionar.

- **`advinha.py`**, **`advinha_for.py`**, **`advinha_for_refatorado.py`** — ver tabela do jogo de adivinhação acima.
- **`lab.py`** — Resolve equações do 2º grau (Bhaskara) usando o módulo `cmath`, tratando tanto raízes reais quanto complexas, com validação de entrada (coeficiente `a` não pode ser zero).
- **`Lab.ipynb`** — Espaço de experimentação interativa em Jupyter para testar trechos de código e anotações de estudo.

## 🧩 Modularização

Algoritmos que separam a lógica em **funções e procedimentos reutilizáveis**, em vez de código sequencial solto.

| Arquivo | Conceito praticado |
|---|---|
| `func_calcular_media.py` | Função `calcular_media()` que recebe uma lista e retorna a média, com tratamento de lista vazia |
| `func_calcular_media_refat.py` | Função de leitura validada (`ler_numero()`) + função `calcular_estatisticas()` retornando soma, média, máximo e mínimo |
| `proc_calcular_valor.py` | Procedimento `calcular_desconto()` que aplica desconto por faixa de valor (0%, 10%, 20%) |
| `proc_calcular_valor_refat.py` | Mesma lógica de desconto, refatorada com validação de entrada e operador ternário |

## 🚀 Como executar

### Opção 1 — Dev Container (recomendado)
O projeto já vem com um ambiente Docker pronto (`.devcontainer/`), baseado em `python:3.11-slim`, com as dependências instaladas automaticamente.

1. Abra a pasta no VS Code com a extensão **Dev Containers** instalada.
2. Selecione **"Reopen in Container"**.
3. O ambiente já sobe com as extensões `ms-python.python` e `ms-toolsai.jupyter` e com as dependências de `requirements.txt` instaladas.

### Opção 2 — Ambiente local
```bash
git clone https://github.com/asessagit/python-lab.git
cd python-lab
python3 -m venv .venv
source .venv/bin/activate      # Linux/macOS
pip install -r requirements.txt
```

Depois, execute qualquer script individualmente a partir da pasta correspondente, por exemplo:
```bash
cd Algoritmos/Estrutura_Conjunto_Dados/Vetores
python3 advinha_vetor.py
```

## 📦 Dependências

```
numpy
pandas
matplotlib
seaborn
scipy
jupyter
notebook
```

## 🤝 Contribuindo
Este é um repositório pessoal de estudo. Para sugestões, abra uma *Issue*.

## 📄 Licença
Este projeto está licenciado sob os termos da [Licença MIT](https://github.com/asessagit/python-lab/blob/master/LICENSE).

---
Última atualização: 2026-09-10
Autor: [asessagit](https://github.com/asessagit) (Alex Sessa)