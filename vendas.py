from Funcoes import *

def principal():
    while(True):
        print("Bem-vindo ao ...\n")
        print("(1) Cadastrar produto")
        print("(2) Ver quantidade de produtos")
        print("(3) Listar produtos")
        print("(4) Vender um produto")
        print("(5) Repor produto")
        print("(6) Historico de vendas\n")

        opcao=int(input("Escolha a opção desejada: "))

        if (opcao == 1):
            cadastrar_produto()
        elif(opcao == 2):
            ver_quantidade_produto()
        elif(opcao == 3):
            listar_produtos()
        elif(opcao == 4):
            vender_produto()
        elif(opcao == 5):
            repor_produto()
        elif(opcao == 6):
            historico_vendas()
        else: print("opção invalida, tente novamente!")




principal()