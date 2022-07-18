def cadastrar_produto():
    print("Você selecionou cadastrar um produto.")
    nome = (input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produto = [nome, preco, quantidade]
    print("\ncadastro realizado com sucesso!\n")
    return produto

def ver_quantidade_produto(todos_produtos):
    print()



def listar_produtos(todos_produtos):
    print('-' * 40)
    print(f'{"LISTA DE PRODUTOS":^40}')
    print('-' * 40)
    print (todos_produtos)

def vender_produto(todos_produtos):
    nome = input("Qual produto voce quer vender?: ")

def repor_produto(todos_produtos):
    nome = input("Qual produto voce quer repor?: ")


def historico_vendas(todos_produtos):
    print("entrou na funçao historico")

