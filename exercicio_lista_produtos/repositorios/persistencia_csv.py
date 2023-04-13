import csv
import os
import uuid

import models.produto as model


class PersistenciaCsv:
    def __init__(self, nome_arquivo):
        caminho_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.arquivo = os.path.join(caminho_projeto, "db", nome_arquivo)
        self.produtos = []
        
    def incluir_produto(self, produto):
        with open(self.arquivo, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([uuid.uuid4(), produto.nome, produto.quantidade, produto.preco])
        
    def alterar_produto(self, produto):
        with open(self.arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            for p in self.produtos:
                if p[0] == produto.id:
                    writer.writerow([produto.id, produto.nome, produto.quantidade, produto.preco])
                else:
                    writer.writerow(p)
        
    def excluir_produto(self, id):
        with open(self.arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            for p in self.produtos:
                if p[0] != id:
                    writer.writerow(p)
        
    def listar_produtos(self):
        self.carregar_dados()
        lista_instancia_produtos = []
        for p in self.produtos:
            produto = model.Produto(id=p[0], nome=p[1], quantidade=p[2], preco=p[3])
            lista_instancia_produtos.append(produto)
        return lista_instancia_produtos
        
    def carregar_dados(self):
        self.produtos = []
        try:
            with open(self.arquivo, mode='r') as file:
                reader = csv.reader(file)
                next(reader) # ignora a primeira linha (header)
                for row in reader:
                    self.produtos.append(row)
        except FileNotFoundError:
            self.produtos = []
        