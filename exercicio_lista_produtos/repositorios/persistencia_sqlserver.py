import pyodbc
import models.produto as model

class PersistenciaSQLServer:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.conn = None

    def conectar(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';Trusted_Connection=yes;')
        except pyodbc.Error as err:
            print("Erro de conexão ao banco de dados:", err)

    def desconectar(self):
        if self.conn is not None and not self.conn.closed:
            self.conn.close()

    def incluir_produto(self, produto):
        self.conectar()
        cursor = self.conn.cursor()
        query = "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)"
        values = (produto.nome, produto.quantidade, produto.preco)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        self.desconectar()

    def alterar_produto(self, produto):
        self.conectar()
        cursor = self.conn.cursor()
        query = "UPDATE produtos SET nome = ?, quantidade = ?, preco = ? WHERE id = ?"
        values = (produto.nome, produto.quantidade, produto.preco, produto.id)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        self.desconectar()

    def excluir_produto(self, id):
        self.conectar()
        cursor = self.conn.cursor()
        query = "DELETE FROM produtos WHERE id = ?"
        values = (id,)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        self.desconectar()

    def listar_produtos(self):
        self.conectar()
        cursor = self.conn.cursor()
        query = "SELECT id, nome, quantidade, preco FROM produtos"
        cursor.execute(query)
        produtos = []
        for id, nome, quantidade, preco in cursor:
            produto = model.Produto(id, nome, quantidade, preco)
            produtos.append(produto)
        cursor.close()
        self.desconectar()
        return produtos
