import os
import time

def menu_db():
    # os.system('clear') # limpa o console
    limpar_tela()
    print("+ " + "-" * 29 + "+")
    print("| Sistema Controle de Produtos |")
    print("+ " + "-" * 29 + "+")
    print("\nSelecione a forma de armazenamento dos dados?")
    print("-" * 45)
    print("1 - PostGre")
    print("2 - SQL Server")
    print("3 - MySQL")
    print("4 - SQLite")
    print("5 - CSV")
    print("6 - JSON")
    print("7 - XML")

def menu():
    # os.system('clear') # limpa o console
    limpar_tela()
    print("+ " + "-" * 29 + "+")
    print("| Sistema Controle de Produtos |")
    print("+ " + "-" * 29 + "+")
    print("\nO que você deseja fazer?")
    print("-" * 24)
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