-- ============================
-- 1_3_comandos_DQL.sql
-- Autor: Sergio Urzedo Junior (RM561396)
-- Projeto SGV - Melhores Compras LTDA
-- ============================

-- a) Categorias e produtos (LEFT JOIN para exibir categorias sem produtos)
SELECT
    c.id_categoria AS codigo_categoria,
    c.nome AS nome_categoria,
    p.id_produto AS codigo_produto,
    p.nome AS descricao_produto,
    p.preco AS valor_unitario,
    'Caixa' AS tipo_embalagem, -- campo fixo simulado
    ROUND((p.preco * 0.30), 2) AS percentual_lucro
FROM categoria c
LEFT JOIN produto p ON p.id_categoria = c.id_categoria
ORDER BY c.nome, p.nome;

-- b) Clientes Pessoa Física com informações detalhadas
-- OBS: Adaptado à estrutura da tabela `cliente` existente no SQLite
SELECT
    id_cliente,
    nome,
    email,
    telefone,
    STRFTIME('%d-%m-%Y', data_cadastro) AS data_nascimento_simulada,
    STRFTIME('%w', data_cadastro) AS dia_semana_simulado,
    CAST(STRFTIME('%Y', 'now') AS INTEGER) - CAST(STRFTIME('%Y', data_cadastro) AS INTEGER) AS anos_vida_simulado,
    'M' AS sexo_biologico,
    '12345678900' AS cpf_simulado
FROM cliente;

-- c) Visualização de vídeos (com nome do produto)
SELECT
    vp.id_produto AS codigo_produto,
    p.nome AS nome_produto,
    vv.data_hora_visualizacao
FROM visualizacao_video vv
JOIN video_produto vp ON vv.id_video = vp.id_video
JOIN produto p ON vp.id_produto = p.id_produto
ORDER BY vv.data_hora_visualizacao DESC;
