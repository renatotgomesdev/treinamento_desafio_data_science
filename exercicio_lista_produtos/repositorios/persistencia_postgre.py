import psycopg2
import models.produto as model

class PersistenciaPostgre:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except psycopg2.Error as err:
            print("Erro de conexão ao banco de dados:", err)

    def desconectar(self):
        if self.conn is not None and not self.conn.closed:
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
