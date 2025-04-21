import sqlite3
import pandas as pd
from fpdf import FPDF

# Caminho para o banco de dados
db_path = "C:\\FIAP\\melhorescompras\\data\\melhores_compras.db"
conn = sqlite3.connect(db_path)

# Consulta dos dados
query = '''
SELECT f.nome AS funcionario,
       COUNT(s.id_sac) AS total_chamados,
       ROUND(AVG(s.tempo_total_atendimento), 2) AS tempo_medio,
       ROUND(AVG(s.indice_satisfacao), 2) AS satisfacao_media
FROM sac s
JOIN funcionario f ON s.id_funcionario = f.id_funcionario
WHERE s.status_chamado IN ('F','X')
GROUP BY f.nome
'''

df = pd.read_sql_query(query, conn)
conn.close()

# Caminho para salvar os arquivos
csv_path = "C:\\FIAP\\melhorescompras\\relatorios\\relatorio_funcionarios.csv"
pdf_path = "C:\\FIAP\\melhorescompras\\relatorios\\relatorio_funcionarios.pdf"

# Exportar CSV
df.to_csv(csv_path, index=False)
print("✅ CSV gerado com sucesso.")

# Criar PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Relatório de Atendimento por Funcionário", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", "B", 10)
col_widths = [60, 40, 40, 40]
headers = ["Funcionário", "Total Chamados", "Tempo Médio", "Satisfação Média"]

# Cabeçalhos
for i, header in enumerate(headers):
    pdf.cell(col_widths[i], 10, header, border=1, align="C")
pdf.ln()

# Dados
pdf.set_font("Arial", "", 10)
for _, row in df.iterrows():
    pdf.cell(col_widths[0], 10, str(row["funcionario"]), border=1)
    pdf.cell(col_widths[1], 10, str(row["total_chamados"]), border=1, align="C")
    pdf.cell(col_widths[2], 10, str(row["tempo_medio"]), border=1, align="C")
    pdf.cell(col_widths[3], 10, str(row["satisfacao_media"]), border=1, align="C")
    pdf.ln()

# Salvar PDF
pdf.output(pdf_path)
print("✅ PDF gerado com sucesso.")
