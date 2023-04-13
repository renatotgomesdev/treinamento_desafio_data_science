import os
import sqlite3
import uuid

import models.produto as model


class PersistenciaSQLite:
    def __init__(self, nome_banco):
        caminho_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.arquivo = os.path.join(caminho_projeto, "db", nome_banco)
        self.conexao = sqlite3.connect(self.arquivo)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()
        
    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco TEXT NOT NULL
            )
        """)
        self.conexao.commit()
        
    def incluir_produto(self, produto):
        produto.id = str(uuid.uuid4())
        self.cursor.execute("""
            INSERT INTO produto (id, nome, quantidade, preco)
            VALUES (?, ?, ?, ?)
        """, (produto.id, produto.nome, produto.quantidade, produto.preco))
        self.conexao.commit()
        
    def alterar_produto(self, produto):
        self.cursor.execute("""
            UPDATE produto
            SET nome = ?, quantidade = ?, preco = ?
            WHERE id = ?
        """, (produto.nome, produto.quantidade, produto.preco, produto.id))
        self.conexao.commit()
        
    def excluir_produto(self, id):
        self.cursor.execute("DELETE FROM produto WHERE id = ?", (id,))
        self.conexao.commit()
        
    def listar_produtos(self):
        self.cursor.execute("SELECT * FROM produto")
        lista_instancia_produtos = []
        for p in self.cursor.fetchall():
            produto = model.Produto(id=p[0], nome=p[1], quantidade=p[2], preco=p[3])
            lista_instancia_produtos.append(produto)
        return lista_instancia_produtos
