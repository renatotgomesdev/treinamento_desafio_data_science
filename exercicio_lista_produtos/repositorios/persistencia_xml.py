import os
import uuid
import xml.etree.ElementTree as ET

import models.produto as model


class PersistenciaXML:
    def __init__(self, nome_arquivo):
        caminho_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.arquivo = os.path.join(caminho_projeto, "db", nome_arquivo)
        self.root = ET.Element("produtos")
        self.tree = ET.ElementTree(self.root)
        
    def incluir_produto(self, produto):
        produto_element = ET.SubElement(self.root, "produto")
        produto_element.set("id", str(uuid.uuid4()))
        nome_element = ET.SubElement(produto_element, "nome")
        nome_element.text = produto.nome
        quantidade_element = ET.SubElement(produto_element, "quantidade")
        quantidade_element.text = str(produto.quantidade)
        preco_element = ET.SubElement(produto_element, "preco")
        preco_element.text = str(produto.preco)
        self.tree.write(self.arquivo)
        
    def alterar_produto(self, produto):
        for produto_element in self.root.iter("produto"):
            if produto_element.get("id") == produto.id:
                nome_element = produto_element.find("nome")
                nome_element.text = produto.nome
                quantidade_element = produto_element.find("quantidade")
                quantidade_element.text = str(produto.quantidade)
                preco_element = produto_element.find("preco")
                preco_element.text = str(produto.preco)
                self.tree.write(self.arquivo)
        
    def excluir_produto(self, id):
        for produto_element in self.root.findall("produto"):
            if produto_element.get("id") == id:
                self.root.remove(produto_element)
                self.tree.write(self.arquivo)
        
    def listar_produtos(self):
        self.carregar_dados()
        lista_instancia_produtos = []
        for produto_element in self.root.findall("produto"):
            id = produto_element.get("id")
            nome_element = produto_element.find("nome")
            nome = nome_element.text
            quantidade_element = produto_element.find("quantidade")
            quantidade = int(quantidade_element.text)
            preco_element = produto_element.find("preco")
            preco = float(preco_element.text)
            produto = model.Produto(id=id, nome=nome, quantidade=quantidade, preco=preco)
            lista_instancia_produtos.append(produto)
        return lista_instancia_produtos
        
    def carregar_dados(self):
        try:
            self.tree.parse(self.arquivo)
        except (ET.ParseError, FileNotFoundError):
            self.tree.write(self.arquivo)
