[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://github.com/asessagit/python-lab)
[![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange?logo=jupyter)](https://github.com/asessagit/python-lab/blob/master/Lab.ipynb)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://github.com/asessagit/python-lab/tree/master/.devcontainer)
[![DevContainer](https://img.shields.io/badge/devcontainer-ready-green?logo=docker)](https://github.com/asessagit/python-lab/tree/master/.devcontainer)
[![License](https://img.shields.io/badge/license-MIT-yellow)](https://github.com/asessagit/python-lab/blob/master/LICENSE)

# 🐍 Python Lab — Fundamentos e Lógica de Programação

Espaço dedicado a experimentos, estudos e pequenos projetos em Python. Reúne exemplos práticos, exercícios e implementações simples para explorar conceitos fundamentais da linguagem — estruturas de controle, funções, manipulação de dados e lógica de programação.

## 📂 Estrutura do repositório

```
python-lab/
├── .devcontainer/              # Ambiente de desenvolvimento containerizado (Docker + VS Code)
│   ├── Dockerfile
│   └── devcontainer.json
├── .gitignore
├── Lab.ipynb                   # Notebook Jupyter com experimentos e anotações de estudo
├── advinha.py                  # Jogo de adivinhação — versão inicial (while)
├── advinha_for.py              # Jogo de adivinhação — refatorado para usar for/else
├── advinha_for_refatorado      # Jogo de adivinhação — versão comentada linha a linha
├── advinha_vetor.py            # Jogo de adivinhação — versão com histórico de chutes (vetor)
├── lab.py                      # Resolução de equações do 2º grau (raízes reais e complexas)
├── requirements.txt            # Dependências Python do projeto
├── vecmedia.py                 # Cálculo da média de notas de alunos usando vetores
└── vecvendas.py                # Cálculo da variação de estoque de produtos usando vetores
```

## 🎮 Scripts

### Jogo de adivinhação (evolução progressiva)
Os quatro arquivos `advinha*` implementam o mesmo jogo — o programa sorteia um número entre 0 e 100 e o jogador tenta acertar em até 10 tentativas — mas em estágios diferentes de refatoração, pensados como exercício de evolução de código:

| Arquivo | Conceito praticado |
|---|---|
| `advinha.py` | Laço `while`, controle manual do contador de chances |
| `advinha_for.py` | Laço `for` com `range()` decrescente e cláusula `for...else` |
| `advinha_for_refatorado` | Mesma lógica do `for`, totalmente comentada linha a linha (fins didáticos) |
| `advinha_vetor.py` | Uso de lista (vetor) para guardar o histórico de chutes e evitar repetições |

### Manipulação de dados com vetores
- **`vecmedia.py`** — Lê duas notas de 60 alunos, calcula a média individual de cada um e a média geral da turma.
- **`vecvendas.py`** — Compara o estoque anterior e atual de 5 produtos e informa entradas, saídas ou estabilidade no estoque.

### Matemática
- **`lab.py`** — Resolve equações do 2º grau (Bhaskara) usando o módulo `cmath`, tratando tanto raízes reais quanto complexas, com validação de entrada (coeficiente `a` não pode ser zero).

### Notebook
- **`Lab.ipynb`** — Espaço de experimentação interativa em Jupyter para testar trechos de código e anotações de estudo.

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

Depois, execute qualquer script individualmente, por exemplo:
```bash
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
Última atualização: 2026-09-07
Autor: [asessagit](https://github.com/asessagit) (Alex Sessa)
