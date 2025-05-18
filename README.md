# 🛒 Projeto Melhores Compras LTDA – SGV

📘 Projeto acadêmico da FIAP – 1TSCOB – Fase 3  
🎯 Tema: Sistema de Gerenciamento de Vídeos com banco de dados relacional, SQL, Python, ESG e LGPD

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
- **Aplicação de conceitos da LGPD com segurança e anonimização de dados**

---

## 📌 Entregas da Fase 3 (FIAP)

| Desafio | Entregável                                                | Status |
|---------|------------------------------------------------------------|--------|
| 3.1     | `1_2_comandos_DML.sql` – Carga em `sgv_ocorrencia_sac`    | ✅     |
| 3.2     | `1_2_evidencia_execucao.docx` – Tabela preenchida         | ✅     |
| 3.3     | `1_3_comandos_DQL.sql` – Consulta por categoria           | ✅     |
| 3.4     | `1_3_evidencia_categorias.docx` – Quantidade por categoria| ✅     |
| 3.5     | `1_5_Template_Ampliando_Consistencia_LGPD.docx` – LGPD    | ✅     |
| 3.6     | `1_1_componentes.txt` – Membros do grupo                  | ✅     |
| 3.7     | `PBL_1º_Ano_Fase3_MelhoresCompras.zip` – Compactado final | ✅     |

---

## 📂 Estrutura do Projeto

```plaintext
melhorescompras/
├── data/
│   └── melhores_compras.db
├── notebooks/
│   ├── fase3_ocorrencias_sac.ipynb
│   ├── consulta_chamados_categoria.ipynb
│   └── melhorescompras_final_completo_v3_EVIDENCIA.ipynb
├── requisitos/
│   ├── 1_1_componentes.txt
│   ├── 1_2_comandos_DML.sql
│   ├── 1_3_comandos_DQL.sql
│   ├── 1_5_arquivo_produto.json
│   └── 1_6_ProgramaSustentabilidade_atualizado.docx
├── relatorios/
│   ├── 1_2_evidencia_execucao.docx
│   ├── 1_3_evidencia_categorias.docx
│   ├── relatorio_funcionarios.csv
│   └── relatorio_funcionarios.pdf
├── algoritmo_produto.py
├── database_setup.py
├── gerar_relatorios.py
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
- Aplicação prática da LGPD com recomendações e anonimização de dados
- Notebooks com evidências e código rastreável para todas as entregas da fase

---

## 📎 Repositório GitHub

[https://github.com/sergiourzedojunior/melhorescompras](https://github.com/sergiourzedojunior/melhorescompras)
