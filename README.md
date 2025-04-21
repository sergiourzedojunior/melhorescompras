# 📦 Projeto SGV - Sistema de Gerenciamento de Vídeos

**FIAP - 1º Ano | Fase 2 - Banco de Dados Relacional**  
**Aluno:** Sergio Urzedo Junior

---

## 🎯 Objetivo

Este projeto simula um sistema de gerenciamento de vídeos de produtos para a empresa fictícia **Melhores Compras LTDA**, abordando práticas de modelagem relacional, comandos DML e DQL, e integração com Python/SQLite para persistência de dados.

---

## 🗂️ Estrutura do Projeto

```
melhorescompras/
├── data/
│   └── melhores_compras.db                # Banco de dados SQLite
├── notebooks/
│   ├── melhorescompras_final.ipynb        # Desenvolvimento principal
│   ├── melhorescompras_final_completo_v2_EVIDENCIA.ipynb
│   └── melhorescompras_final_completo_v3_EVIDENCIA.ipynb
├── requisitos/
│   ├── 1_1_componentes.txt                # Equipe
│   ├── 1_2_comandos_DML.sql               # Comandos de manipulação
│   ├── 1_3_comandos_DQL.sql               # Comandos de consulta
│   ├── 1_5_arquivo_produto.json           # Produtos em JSON
│   └── 1_6_ProgramaSustentabilidade.docx  # Planejamento ESG
├── relatorios/
│   ├── relatorio_funcionarios.csv
│   └── relatorio_funcionarios.pdf
├── streamlit_app.py                       # Visualização de indicadores
├── algoritmo_produto.py                   # Carga automática de produtos
└── README.md                              # Este arquivo
```

---

## 🧱 Componentes implementados

### 📊 Banco de Dados
- Criação de 15 tabelas com integridade referencial
- Inserção de dados (clientes PF/PJ, produtos, SAC, funcionários)
- Normalização com tabelas auxiliares (endereços, categorias)

### 💻 Python + SQLite
- Execução de comandos SQL via `sqlite3` e `pandas`
- Algoritmo de leitura de produtos `.json` com cálculo de ICMS
- Exportação de relatórios em `.csv` e `.pdf`

### 🌐 Interface com o usuário
- Aplicativo `Streamlit` para visualização de:
  - Chamados por status
  - Satisfação média por funcionário

---

## 📄 Evidências

- 📁 [Evidência DML e Criação de Tabelas (v2)](notebooks/melhorescompras_final_completo_v2_EVIDENCIA.ipynb)
- 📁 [Evidência de Tabelas Complementares e Selects (v3)](notebooks/melhorescompras_final_completo_v3_EVIDENCIA.ipynb)
- 🧪 Todos os notebooks executados com `nbconvert` e versão `.html` para submissão

---

## ✅ Entregáveis

| Arquivo                                  | Descrição                                          |
|------------------------------------------|----------------------------------------------------|
| `1_1_componentes.txt`                    | Nome dos integrantes                               |
| `1_2_comandos_DML.sql`                   | Comandos de manipulação (INSERT, UPDATE, DELETE)   |
| `1_3_comandos_DQL.sql`                   | Comandos de consulta (SELECT, JOINs)               |
| `1_5_arquivo_produto.json`               | Produtos em formato JSON com ICMS calculado        |
| `1_6_ProgramaSustentabilidade.docx`      | Planejamento ESG - Ambiental, Social, Governança   |
| `melhores_compras.db`                    | Banco de dados relacional final                    |
| `relatorios/`                            | Evidência de relatórios gerados                    |
| `notebooks/`                             | Execução de scripts com validação e evidência      |

---

## 🚀 Como executar localmente

```bash
cd melhorescompras
python -m venv .venvfiap
source .venvfiap/bin/activate  # ou .venvfiap\\Scripts\\activate no Windows
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 📚 Requisitos

- Python 3.11+
- Jupyter Notebook
- SQLite3
- Streamlit
- Pandas, FPDF, Plotly

---

## 👏 Agradecimentos

Projeto desenvolvido como parte da formação em **Ciência de Dados** da **FIAP**.  
