# 🛒 Melhores Compras LTDA – SGV (Sistema de Gerenciamento de Vídeos)

📘 Projeto acadêmico da FIAP com foco em banco de dados relacional, consultas SQL, manipulação via Python e práticas ESG.

---

## 👤 Autor

- **Nome:** Sergio Urzedo Junior  
- **RA:** RM561396  
- **Turma:** 1TSCOB - 2025/1

---

## 🎯 Objetivo

Simular um sistema corporativo para gerenciamento de produtos, vídeos, atendimentos e auditorias utilizando:

- Banco de dados relacional com **SQLite**
- Execução de **comandos DDL, DML e DQL**
- Geração de relatórios em **.csv** e **.pdf**
- Registro de produtos com **ICMS (18%)**
- Estrutura de práticas **ESG (Ambiental, Social e Governança)**

---

## 🗂️ Estrutura do Projeto

```plaintext
melhorescompras/
├── data/
│   └── melhores_compras.db                     # Banco de dados SQLite
├── notebooks/
│   ├── melhorescompras_final.ipynb             # Desenvolvimento principal
│   ├── melhorescompras_final_completo_v2_EVIDENCIA.ipynb
│   └── melhorescompras_final_completo_v3_EVIDENCIA.ipynb
├── requisitos/
│   ├── 1_1_componentes.txt
│   ├── 1_2_comandos_DML.sql
│   ├── 1_3_comandos_DQL.sql
│   ├── 1_5_arquivo_produto.json
│   └── 1_6_ProgramaSustentabilidade.docx
├── relatorios/
│   ├── relatorio_funcionarios.csv
│   └── relatorio_funcionarios.pdf
├── algoritmo_produto.py                        # Geração de JSON + ICMS
├── database_setup.py                           # Criação + inserção no banco
├── gerar_relatorios.py                         # Geração dos relatórios
├── crud.py                                     # Operações SQL em Python
├── requirements.txt                            # Dependências
└── README.md
