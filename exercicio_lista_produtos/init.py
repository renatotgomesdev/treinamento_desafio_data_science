import os

import produtos.funcoes as fnp
import telas.funcoes as fnt

while True:
    fnt.menu()
    opcao = input()

    if opcao == "1":
        fnp.cadastra_produto()
    elif opcao == "2":
        fnp.mostra_produtos()
    elif opcao == "3":
        fnt.mensagem_com_pausa("Encerrando o programa...")
        break
    else:
        fnt.mensagem_com_pausa("Opção inválida. Tente novamente.")


