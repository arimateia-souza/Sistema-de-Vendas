def cadastrar_produto():
    print("Você selecionou cadastrar um produto.")
    quantidade_produtos = int (input("Quantos produtos você deseja cadastrar?: "))
    cadastro = 1
    while(cadastro <= quantidade_produtos ):
        print("\nfaça o cadastro do",cadastro,"º produto\n")
        nome = (input("Digite o nome do produto: "))
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        produtos = nome, preco, quantidade
        cadastro = cadastro +1
    print("\ncadastro realizado com sucesso!\n")
    return produtos

def ver_quantidade_produto(todos_produtos):
    print()



def listar_produtos(todos_produtos):
    print('_' * 40)
    print(f'{"LISTA DE PRODUTOS":^40}')
    print('_' * 40)
    #for
        #print(todos_produtos) #falta formatar em tabela

def vender_produto(todos_produtos):
    nome = input("Qual produto voce quer vender?: ")




def repor_produto(todos_produtos):
    nome = input("Qual produto voce quer repor?: ")

def historico_vendas(todos_produtos):
    print("entrou na funçao historico")



