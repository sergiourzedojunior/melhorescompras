```markdown
# 🛒 Projeto Melhores Compras - SGV (FIAP)

Este projeto tem como objetivo simular o gerenciamento de vídeos e atendimentos da empresa fictícia **Melhores Compras LTDA**, integrando conceitos de banco de dados relacionais, SQL, Python e práticas ESG.

---

## 👤 Autor

- **Nome**: Sergio Urzedo Junior  
- **RA**: RM561396  
- **Turma**: Data Science - Graduação - 1TSCOB - 2025/1

---

## 📁 Estrutura do Projeto

```plaintext
melhorescompras/
├── data/
│   └── melhores_compras.db                # Banco de dados SQLite
├── notebooks/
│   └── melhorescompras_final.ipynb        # Notebook com consultas e visualizações
├── relatorios/
│   ├── relatorio_funcionarios.csv         # Relatório em formato CSV
│   └── relatorio_funcionarios.pdf         # Relatório em formato PDF
├── requisitos/
│   ├── 1_1_componentes.txt                 # Componentes do sistema
│   ├── 1_5_arquivo_produto.json            # Produtos com cálculo de ICMS
│   └── 1_6_ProgramaSustentabilidade.docx   # Documento ESG
├── algoritmo_produto.py                   # Algoritmo de inserção com ICMS
├── database_setup.py                      # Script para criação e popular dados no banco
├── gerar_relatorios.py                    # Script para geração de CSV/PDF
├── crud.py                                # Operações básicas de inserção e consulta
├── requirements.txt                       # Dependências do projeto
└── README.md                              # Este arquivo
```

---

## 🚀 Funcionalidades

- Criação automatizada do banco SQLite com tabelas normalizadas
- Execução de comandos SQL (DDL, DML e DQL)
- Consultas complexas com filtros, joins, agregações e visualização de dados
- Algoritmo Python que insere produtos com cálculo automático de ICMS
- Relatórios de desempenho por funcionário em formatos CSV e PDF
- Simulação de práticas ESG com estrutura de auditoria e documentação

---

## 🧰 Como executar

1. **Ative o ambiente virtual:**
```bash
.\.venvfiap\Scripts\activate
```

2. **Crie o banco de dados e popular dados de exemplo:**
```bash
python database_setup.py
```

3. **Execute o algoritmo de ICMS:**
```bash
python algoritmo_produto.py
```

4. **Gere os relatórios:**
```bash
python gerar_relatorios.py
```

---

## ✅ Desafios atendidos (FIAP)

| Desafio | Descrição |
|---------|-----------|
| 1.1     | Arquivo `1_1_componentes.txt` com os componentes da arquitetura |
| 1.2     | Comandos DML de inserção, atualização e deleção implementados |
| 1.3     | Consultas SQL com `JOIN`, `GROUP BY`, `AVG`, `COUNT`, `DISTINCT`, etc. |
| 1.4     | Algoritmo em Python que calcula e insere produtos com ICMS |
| 1.5     | JSON de produtos com atributos fiscais + documento ESG |
| 1.6     | Relatórios salvos em `.csv` e `.pdf` com base no banco de dados |

---

## 📎 Repositório GitHub

- [https://github.com/sergiourzedojunior/melhorescompras](https://github.com/sergiourzedojunior/melhorescompras)

---

## 🟢 Status

**Projeto finalizado, testado e pronto para entrega.**
