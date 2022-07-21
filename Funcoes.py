def cadastrar_produto():
    print("Você selecionou cadastrar um produto.")
    nome = (input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produto = [nome, preco, quantidade]
    print("\nCadastro realizado com sucesso!\n")
    return produto


def ver_quantidade_produto(todos_produtos):
    nome = str(input(" Qual produto você deseja verificar a quantidade ? "))
    for produto in todos_produtos:
        if ( nome == produto[0]):
            print ( "O produto que você pesquisou é : " , nome , " e possui ", produto [2] , " unidades. ")
            break
        else:
            print("Seu produto não foi encontrado")


def listar_produtos(todos_produtos):
    print("-" * 45)
    print("LISTA DE PRODUTOS")
    print("-" * 45)
    for i in todos_produtos:
        print("| Nome:",i[0], " | Preco:",i[1], " | Quantidade:",i[2], "|")
        print("-" * 40)

def vender_produto(todos_produtos):
    nome = input("Qual produto você deseja vender? ")
    quantidade = int(input("Quantos você deseja vender ? "))
    for produto in todos_produtos:
        if (nome == produto[0]):
            if (quantidade <= produto[2]):
                print("Seu produto foi vendido com sucesso")
                produto[2] = produto[2] - quantidade
                return todos_produtos

            elif (quantidade >= produto[2]):
                print("Quantidade insuficiente no estoque ")
                quantidade = int(input("Digite novamente sua quantidade : "))
                produto[2] = produto[2] - quantidade
                print("Seu produto foi vendido com sucesso ")
        else:
            print(" Você digitou o nome do produto errado")


def repor_produto(todos_produtos):
    nome = input("Qual produto voce quer repor?: ")
    quantidade = int(input("Quantas unidades você deseja repor ?"))
    for produto in todos_produtos:
        if(nome == produto[0]):
            produto[2] = quantidade + produto[2]
            print(" Sua reposição foi feita com sucesso")
            break
        elif(nome != produto[0]):
            print("Seu produto não foi identificado, refaça a operação!")



def historico_vendas(total_produtos):
    print("a")