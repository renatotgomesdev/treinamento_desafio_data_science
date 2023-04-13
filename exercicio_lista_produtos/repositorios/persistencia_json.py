import json
import os
import uuid

import models.produto as model


class PersistenciaJson:
    def __init__(self, nome_arquivo):
        caminho_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.arquivo = os.path.join(caminho_projeto, "db", nome_arquivo)
        self.produtos = []
        
    def incluir_produto(self, produto):
        produto.id = str(uuid.uuid4()) # Adicionado srt() para converter em string
        self.carregar_dados()
        self.produtos.append(produto.__dict__)
        self.salvar_dados()
        
    def alterar_produto(self, produto):
        self.carregar_dados()
        for i, p in enumerate(self.produtos):
            if p["id"] == produto.id:
                self.produtos[i] = produto.__dict__
                self.salvar_dados()
                break
        
    def excluir_produto(self, id):
        self.carregar_dados()
        self.produtos = [p for p in self.produtos if p["id"] != id]
        self.salvar_dados()
        
    def listar_produtos(self):
        self.carregar_dados()
        lista_instancia_produtos = []
        for p in self.produtos:
            produto = model.Produto(**p)
            lista_instancia_produtos.append(produto)
        return lista_instancia_produtos
        
    def carregar_dados(self):
        try:
            with open(self.arquivo, "r") as f:
                self.produtos = json.load(f)
        except FileNotFoundError:
            self.produtos = []
        
    def salvar_dados(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.produtos, f)
