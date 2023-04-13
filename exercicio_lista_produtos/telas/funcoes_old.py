import os
import time



def menu():
    # os.system('clear') # limpa o console
    fnt.limpar_tela()
    print("Sistema Controle de Produtos")
    print("-" * 28)
    print("O que você deseja fazer?")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

def mensagem_com_pausa(msg):
    os.system('clear')
    print(msg)
    time.sleep(2) # espera 2 segundos antes de sair do programa
