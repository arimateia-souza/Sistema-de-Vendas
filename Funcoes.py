produtos = []
def principal():
    print("Bem-vindo ao ...!")
    while(True):

        print("(1) Cadastrar produto")
        print("(2) Ver quantidade de produtos")
        print("(3) Listar produtos")
        print("(4) Vender um produto")
        print("(5) Repor produto")
        print("(6) Historico de vendas")
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

def cadastrar_produto(produtos):
    print("Você selecionou cadastrar um produto.")
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    quantidade = input("Digite a quantidade do produto: ")
    produtos = [(nome), (preco), (quantidade)]
    return produtos

def ver_quantidade_produto():
    print("entrou na funçao quantidade")

def listar_produtos():
    print("entrou na funçao listar")

def vender_produto():
    print("entrou na funçao vender")

def repor_produto():
    print("entrou na funçao repor")
    #produtos.append()
def historico_vendas():
    print("entrou na funçao historico")



cadastrar_produto(produtos)