from Funcoes import *

def menu():
    print("Bem-vindo ao ...!")
    todos_produtos = []
    while(True):
        print("(1) Cadastrar produto") #ok
        print("(2) Ver quantidade de produtos")
        print("(3) Listar produtos")
        print("(4) Vender um produto")
        print("(5) Repor produto")
        print("(6) Historico de vendas")
        print("(7) Sair")
        opcao=int(input("Escolha a opção desejada: "))
        if (opcao == 1):
            todos_produtos.append(cadastrar_produto)
            print(todos_produtos)


        elif(opcao == 2):
            ver_quantidade_produto(todos_produtos)

        elif(opcao == 3):
            listar_produtos(todos_produtos)

        elif(opcao == 4):
            vender_produto(todos_produtos)

        elif(opcao == 5):
            repor_produto()

        elif(opcao == 6):
            historico_vendas()
        elif (opcao == 7):
            print("O programa foi finalizado") #ok
            break
        else: print("opção invalida, tente novamente!") #ok
menu()

