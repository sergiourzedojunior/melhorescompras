import json
import sqlite3
import os

# Caminhos
json_path = os.path.join("requisitos", "1_5_arquivo_produto.json")
db_path = os.path.join("data", "melhores_compras.db")

# Conectar ao banco SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Carregar JSON de produtos
with open(json_path, encoding="utf-8") as f:
    dados = json.load(f)

produtos = dados.get("produtos", [])

# Inserir produtos
for p in produtos:
    nome = p["nome"]
    descricao = p["descricao"]
    preco = p["preco"]
    icms = p["icms"]

    preco_com_icms = round(preco + (preco * icms / 100), 2)

    try:
        cursor.execute('''
            INSERT INTO produto (nome, descricao, preco)
            VALUES (?, ?, ?)
        ''', (nome, descricao, preco_com_icms))
        print(f"✅ Produto inserido: {nome} | Preço com ICMS: R$ {preco_com_icms}")
    except sqlite3.IntegrityError:
        print(f"⚠️ Produto já existe: {nome}")

conn.commit()
conn.close()
print("✅ Todos os produtos foram processados.")
