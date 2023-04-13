import os
import time

import models.produto as models
import telas.funcoes as fnt

# import repositorios.persistencia_postgre as repo
# repoInstancia = repo.PersistenciaPostgre("localhost", "desafio_data_science", "postgres", "admin")

import repositorios.persistencia_sqlserver as repo
repoInstancia = repo.PersistenciaSQLServer("NOTE-RENATOGOME\\MSSQLSERVER2", "desafio_data_science")

# import repositorios.persistencia_mysql as repo
# repoInstancia = repo.PersistenciaMySQL("localhost", "desafio_data_science", "root", "")

# import repositorios.persistencia_sqlite as repo
# repoInstancia = repo.PersistenciaSQLite("produtos.sqlite")

# import repositorios.persistencia_csv as repo
# repoInstancia = repo.PersistenciaCsv("produtos.csv")

# import repositorios.persistencia_json as repo
# repoInstancia = repo.PersistenciaJson("produtos.json")

# import repositorios.persistencia_xml as repo
# repoInstancia = repo.PersistenciaXML("produtos.xml")

def cadastra_produto():
    # os.system('clear')
    fnt.limpar_tela()
    print("Cadastro de Produtos\n")
    produto = models.Produto()
    produto.nome = input("Digite o nome: ")
    produto.quantidade = input("Digite a quantidade: ")
    produto.preco = input("Digite o preço: ")
    
    repoInstancia.incluir_produto(produto)
    fnt.mensagem_com_pausa("\nProduto cadastrado com sucesso!")
    #print("\nProduto cadastrado com sucesso!")
    #time.sleep(2) # espera 2 segundos antes de voltar para o menu
    

def mostra_produtos():
    produtos = repoInstancia.listar_produtos()
    
    # os.system('clear')
    fnt.limpar_tela()
    print("Lista de Produtos\n")
    if len(produtos) == 0:
        #print("Não há produtos cadastrados.")
        fnt.mensagem_com_pausa("Não há produtos cadastrados.")
    else:
        for produto in produtos:
            print("-" * 20)
            retorno = produto_formatado(produto)
            print(retorno)
    input("\nPressione Enter para voltar ao menu...")

def produto_formatado(produto):
    # return f"Id: {produto.id}\nNome: {produto.nome}\nQuantidade: {produto.quantidade}\nPreço: {produto.quantidade}"
    return f"""
    Id: {produto.id}
    Nome: {produto.nome}
    Quantidade: {produto.quantidade}
    Preço: {produto.preco}
    """
