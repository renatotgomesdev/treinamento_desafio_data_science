import mysql.connector
from mysql.connector import errorcode
import models.produto as model

class PersistenciaMySQL:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erro de acesso ao banco de dados. Verifique as credenciais de acesso.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
            else:
                print(err)

    def desconectar(self):
        if self.conn is not None and self.conn.is_connected():
            self.conn.close()

    def incluir_produto(self, produto):
        self.conectar()
        cursor = self.conn.cursor()
        query = "INSERT INTO produtos (nome, quantidade, preco) VALUES (%s, %s, %s)"
        values = (produto.nome, produto.quantidade, produto.preco)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        self.desconectar()

    def alterar_produto(self, produto):
        self.conectar()
        cursor = self.conn.cursor()
        query = "UPDATE produtos SET nome = %s, quantidade = %s, preco = %s WHERE id = %s"
        values = (produto.nome, produto.quantidade, produto.preco, produto.id)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        self.desconectar()

    def excluir_produto(self, id):
        self.conectar()
        cursor = self.conn.cursor()
        query = "DELETE FROM produtos WHERE id = %s"
        values = (id)
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
