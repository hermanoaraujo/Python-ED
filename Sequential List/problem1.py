from problem1_Class import *
from random import randint
import time

lista = ListaSeq()

def menu(tela):
    if (tela == "tela1"):
        print('''
            Editor de Lista - Hermano A.
            -----------------------------
            1 – Exibir Lista
            2 – Inserir
            3 – Remover
            4 – Exibir elemento
            5 – Exibir posição
            6 – Esvaziar lista
            7 - Mais Opções - Questão 2
            0 – Sair
            ''')
    elif (tela == "tela2"):
        print('''
            Mais Opções - Questão 2
            ----------------------------
            1 – Inserir na 1 posição
            2 – Inserir na ultima posição
            3 – Modificar Elemento
            4 – Remover Primeiro Elemento
            5 – Remover Último Elemento
            6 – Remover Todos Elementos Iguais
            7 - Questão 3
            0 – Voltar
            ''')

while True:
    menu("tela1")
    option = int(input("Digite sua opção:"))


    if (option == 1):
        lista.exibirLista()
    elif (option == 2):
        elemento = int(input("Digite o elemento:"))
        posicao = int(input("Digite a posicao:"))
        lista.inserir(posicao,elemento)
        print(f"Elemento:{elemento} adicionado na posição {posicao}!")
    elif (option == 3):
        posicao = int(input("Digite a posicao:"))
        lista.remover(posicao)
        print(f"Elemento da posição {posicao} removido!")
    elif (option == 4):
        posicao = int(input("Digite a posicao:"))
        print(f'Elemento: {lista.exibirElemento(posicao)}')
    elif (option == 5):
        valor_elemento = int(input("Digite o valor do elemento:"))
        print(f'Posição[index]: {lista.exibirPosicao(valor_elemento)}')
    elif (option == 6):
        confirma = input("Tem certeza que deseja esvaziar a lista? [S/N]:")
        if (confirma.upper()=="S"):
            lista.esvaziar()
            print("Lista esvaziada com sucesso!")
        else:
            continue
    elif (option == 7):
        menu("tela2")
        option = int(input("Digite sua opção:"))
        if(option == 0):
            continue
        elif(option == 1):
            valor_elemento = int(input("Digite o valor do elemento:"))
            lista.inserirPrimeira(valor_elemento)
            print(f"{valor_elemento} inserido com sucesso!")
        elif (option == 2):
            valor_elemento = int(input("Digite o valor do elemento:"))
            lista.inserirUltima(valor_elemento)
            print(f"{valor_elemento} inserido com sucesso!")
        elif (option == 3):
            posicao = int(input("Digite a posicao:"))
            valor_elemento = int(input("Digite o valor do elemento:"))
            lista.modificarElemento(posicao,valor_elemento)
            print("Modificado com sucesso!")
        elif (option == 4):
            lista.removerPrimeiro()
            print("1 elemento removido com sucesso!")
        elif (option == 5):
            lista.removerUltimo()
            print("Ultimo elemento removido com sucesso!")
        elif (option == 6):
            valor_elemento = int(input("Digite o valor do elemento:"))
            lista.removerTodosIguais(valor_elemento)
            print("Elementos iguais removido com sucesso!")
        elif (option == 7):
            l1 = ListaSeq()
            l2 = ListaSeq()
            l3 = ListaSeq()
            l4 = ListaSeq()
            print("\nCriando Listas L1,L2,L3 e L4 ... (ok)")
            time.sleep(2)
            print("\nInserindo 10 números aleatórios na lista L1:")
            time.sleep(0.5)
            for i in range(10):
                valor = randint(0, 99)
                l1.inserir(i+1,valor)
                time.sleep(0.5)
                print(f"Valor {i+1}: {valor}")
            print("\nInserindo 10 números aleatórios na lista L2:")
            for i in range(10):
                valor = randint(0, 99)
                l2.inserir(i + 1, valor)
                time.sleep(0.5)
                print(f"Valor {i+1}: {valor}")

            print("\nConcatenando L1 e L2 em L3:")

            l3.concatenar(l1.getLista())
            l3.concatenar(l2.getLista())
            l4.concatenar(l3.getLista())

            time.sleep(2)
            print("Concatenação:", l3.getLista())

            print("\n Invertendo conteúdo de L4:")
            time.sleep(2)
            l4.inverter()
            print("Lista Invertida:", l4.getLista())

            print("\n----------------------")
            print("Lista 1:",l1.getLista())
            print("Lista 2:", l2.getLista())
            print("Lista 3:", l3.getLista())
            print("Lista 4:", l4.getLista())


    elif (option == 0):
        print("Programa finalizado..")
        exit()
    else:
        print("Opção Inválida! Digite novamente")

