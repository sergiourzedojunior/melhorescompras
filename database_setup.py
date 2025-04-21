import sqlite3

# Caminho absoluto do banco (Windows)
db_path = "C:\\FIAP\\melhorescompras\\data\\melhores_compras.db"

# Conexão
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# DROP prévio
tabelas = ["visualizacao_video", "sac", "video_produto", "cliente", "funcionario", "produto", "auditoria_sac"]
for tabela in tabelas:
    cursor.execute(f"DROP TABLE IF EXISTS {tabela}")

# Criação das tabelas
cursor.execute('''
CREATE TABLE produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE video_produto (
    id_video INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    url_video TEXT NOT NULL,
    descricao TEXT,
    status TEXT CHECK (status IN ('A','I')) DEFAULT 'A',
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
)
''')

cursor.execute('''
CREATE TABLE cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    telefone TEXT,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

cursor.execute('''
CREATE TABLE funcionario (
    id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL,
    cargo TEXT NOT NULL,
    departamento TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE visualizacao_video (
    id_visualizacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_video INTEGER NOT NULL,
    id_cliente INTEGER,
    data_hora_visualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_video) REFERENCES video_produto(id_video),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
)
''')

cursor.execute('''
CREATE TABLE sac (
    id_sac INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    id_funcionario INTEGER NOT NULL,
    data_hora_atendimento TIMESTAMP,
    status_chamado TEXT CHECK (status_chamado IN ('A','E','C','F','X')) NOT NULL,
    tipo_chamado TEXT CHECK (tipo_chamado IN ('1','2')) NOT NULL,
    tempo_total_atendimento INTEGER,
    indice_satisfacao INTEGER CHECK (indice_satisfacao BETWEEN 1 AND 100),
    descricao_chamado TEXT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
)
''')

cursor.execute('''
CREATE TABLE auditoria_sac (
    id_log INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sac INTEGER NOT NULL,
    acao TEXT NOT NULL,
    data_log TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_sac) REFERENCES sac(id_sac)
)
''')

# População de dados

# Produto
cursor.execute("INSERT INTO produto (nome, descricao, preco) VALUES ('Smartphone XYZ', 'Modelo de exemplo', 1999.90)")

# Clientes
clientes = [
    ("Alice Silva", "alice@example.com", "(11)99999-1111"),
    ("Bruno Souza", "bruno@example.com", "(21)98888-2222"),
    ("Carla Mendes", "carla@example.com", "(31)97777-3333")
]
cursor.executemany("INSERT INTO cliente (nome, email, telefone) VALUES (?, ?, ?)", clientes)

# Funcionários
funcionarios = [
    ("Marcos Lima", "12345678901", "1985-02-15", "(11)99999-0000", "marcos@empresa.com", "Atendente", "SAC"),
    ("Fernanda Rocha", "10987654321", "1990-07-23", "(11)98888-1111", "fernanda@empresa.com", "Analista", "Ouvidoria")
]
cursor.executemany('''
INSERT INTO funcionario (nome, cpf, data_nascimento, telefone, email, cargo, departamento)
VALUES (?, ?, ?, ?, ?, ?, ?)''', funcionarios)

# SAC - com todos os 9 campos
sacs = [
    (1, 1, 1, None, 'F', '1', 80, 80, 'Produto com defeito'),
    (2, 1, 2, None, 'X', '2', 45, 50, 'Atraso na entrega'),
    (3, 1, 1, None, 'F', '1', 90, 95, 'Dúvida sobre a garantia')
]
cursor.executemany('''
INSERT INTO sac (id_cliente, id_produto, id_funcionario, data_hora_atendimento,
status_chamado, tipo_chamado, tempo_total_atendimento, indice_satisfacao, descricao_chamado)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', sacs)

conn.commit()
conn.close()

print("✅ Banco criado e populado com sucesso.")
