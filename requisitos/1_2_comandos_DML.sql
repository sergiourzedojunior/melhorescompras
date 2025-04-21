-- ============================
-- 1_2_comandos_DML.sql
-- Autor: Sergio Urzedo Junior (RM561396)
-- Projeto SGV - Melhores Compras LTDA
-- ============================

-- a) Inserir 1 CLIENTE PESSOA FÍSICA
INSERT INTO cliente (nome, email, telefone, data_cadastro)
VALUES ('João da Silva', 'joao.silva@email.com', '(11)99999-1111', CURRENT_TIMESTAMP);

-- a) Inserir 1 CLIENTE PESSOA JURÍDICA
INSERT INTO cliente (nome, email, telefone, data_cadastro)
VALUES ('Empresa XPTO Ltda.', 'contato@xpto.com.br', '(11)22222-2222', CURRENT_TIMESTAMP);

-- b) Tentativa de inserir cliente com email duplicado
-- Este comando deve gerar erro se a constraint UNIQUE estiver correta
-- Resultado esperado: erro de duplicidade de email
INSERT INTO cliente (nome, email, telefone, data_cadastro)
VALUES ('Carlos Repetido', 'joao.silva@email.com', '(11)88888-0000', CURRENT_TIMESTAMP);

-- c) Atualizar cargo e salário de funcionário específico
UPDATE funcionario
SET cargo = 'Gerente de Produtos',
    telefone = '(11)97777-9999'
WHERE nome = 'Fernanda Alves';

-- d) Atualizar um endereço de cliente e definir status inativo
-- (simulado via update da data de cadastro, por exemplo)
UPDATE cliente
SET data_cadastro = '2024-09-08 00:00:00'
WHERE nome = 'João da Silva';

-- e) Tentativa de deletar um produto que está vinculado a SAC
-- Resultado esperado: falha por integridade referencial (se ON DELETE RESTRICT)
DELETE FROM produto
WHERE id_produto = 1;

-- f) Tentativa de atualizar produto com status inválido
-- (simulado com campo 'status' que aceita apenas 'A' ou 'I')
UPDATE video_produto
SET status = 'X'
WHERE id_video = 1;

-- g) Confirmar as alterações
COMMIT;
