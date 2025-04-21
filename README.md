# 🛒 Projeto Melhores Compras LTDA – SGV

📘 Projeto acadêmico da FIAP – 1TSCOB – Fase 2  
🎯 Tema: Sistema de Gerenciamento de Vídeos com banco de dados relacional, SQL, Python e ESG

---

## 👤 Autor

- **Nome:** Sergio Urzedo Junior  
- **RM:** 561396  
- **Turma:** 1TSCOB - 2025/1

---

## 🎯 Objetivo Geral do Projeto

Desenvolver uma solução completa para gerenciamento de vídeos, produtos, atendimentos e satisfação de clientes, aplicando:

- **Banco de Dados Relacional (SQLite)**
- **Comandos SQL (DDL, DML, DQL)**
- **Manipulação e automação via Python**
- **Integração com arquivos JSON**
- **Geração de relatórios em CSV e PDF**
- **Simulação de práticas ESG (Ambiental, Social, Governança)**

---

## 📌 Desafios Atendidos (FIAP)

| Desafio | Entregável                                      | Status |
|---------|--------------------------------------------------|--------|
| 1.1     | `1_1_componentes.txt` com identificação do grupo | ✅     |
| 1.2     | `1_2_comandos_DML.sql` – DMLs com simulações     | ✅     |
| 1.3     | `1_3_comandos_DQL.sql` – Consultas SQL completas | ✅     |
| 1.4     | `algoritmo_produto.py` – Inserção com cálculo de ICMS | ✅     |
| 1.5     | `1_5_arquivo_produto.json` + `1_6_ProgramaSustentabilidade.docx` | ✅     |
| 1.6     | Relatórios em `.csv` e `.pdf`                    | ✅     |

---

## 📂 Estrutura do Projeto

```plaintext
melhorescompras/
├── data/
│   └── melhores_compras.db
├── notebooks/
│   ├── melhorescompras_final.ipynb
│   ├── melhorescompras_final_completo_v2_EVIDENCIA.ipynb
│   ├── melhorescompras_final_completo_v3_EVIDENCIA.ipynb
│   └── *.html (gerado via nbconvert para submissão)
├── requisitos/
│   ├── 1_1_componentes.txt
│   ├── 1_2_comandos_DML.sql
│   ├── 1_3_comandos_DQL.sql
│   ├── 1_5_arquivo_produto.json
│   └── 1_6_ProgramaSustentabilidade.docx
├── relatorios/
│   ├── relatorio_funcionarios.csv
│   └── relatorio_funcionarios.pdf
├── algoritmo_produto.py
├── database_setup.py
├── gerar_relatorios.py
├── crud.py
├── requirements.txt
└── README.md
```

---

## 🚀 Como Executar o Projeto

```bash
# Ativar o ambiente virtual
.\.venvfiap\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Criar banco e inserir dados iniciais
python database_setup.py

# Executar algoritmo de produtos com ICMS
python algoritmo_produto.py

# Gerar relatórios CSV e PDF
python gerar_relatorios.py
```

---

## 📊 Funcionalidades

- Criação e normalização do banco de dados em SQLite
- Inserções com tratamento de erro e integridade referencial
- Consultas SQL com JOIN, filtros, agregações e ordenações
- Algoritmo em Python para geração e ingestão de produtos com ICMS
- Exportação de relatórios analíticos por funcionário
- Planejamento ESG com base em práticas ambientais, sociais e de governança
- Notebooks com evidências para verificação dos dados e comandos

---

## 📎 Repositório GitHub

[https://github.com/sergiourzedojunior/melhorescompras](https://github.com/sergiourzedojunior/melhorescompras)
