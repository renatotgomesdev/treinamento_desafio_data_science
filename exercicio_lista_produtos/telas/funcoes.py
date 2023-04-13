import os
import time


def menu():
    # os.system('clear') # limpa o console
    limpar_tela()
    print("Sistema Controle de Produtos")
    print("-" * 28)
    print("O que você deseja fazer?")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

def limpar_tela():
    

    # Verifica qual o sistema operacional está sendo executado o python
    if os.name == 'nt': # Windows
        #print('Executando no Windows')
        # os.system('cls')

        # Verifica se estou executando o python pelo Git Bash ou pelo CMD no Windows
        if 'MSYSTEM' in os.environ:
            #print('Executando no Git Bash')
            os.system('clear')
        else:
            #print('Executando no CMD do Windows')
            os.system('cls')
            
    else:  # Linux/Unix/MacOS
        #print('Executando no Linux/Unix/MacOS')
        os.system('clear')


def mensagem_com_pausa(msg):
    # os.system('clear')
    limpar_tela()

    # Exibe a mensagem
    print(msg)
    time.sleep(2) # espera 2 segundos antes de sair do programa