#Clientes------------------------------------------------
clientes = []#[[nome, cpf, contato, endereco],[],[]]

def cadastrar_cliente():
    print("--- Cadastrar Cliente ---")
    cpf = input("Digite o CPF: ")
    if buscar_cliente(cpf):
        print("Erro ao cadastrar. Tente novamente!")
        return
    else:
        nome = input("Digite o nome do cliente: ")
        contato = input("Informe um contato (email ou telefone): ")
        endereco = input("Informe o endereço atual: ")
        c = [nome, cpf, contato, endereco]
        clientes.append(c)

def buscar_cliente(cpf):
    print("--- Buscar Cliente ---")
    for c in clientes:
        if c[1] == cpf:
            print(f"CPF pertence ao cliente {c[0]} e encontra-se cadastrado na base.")
            return cpf

    print("CPF não encontrado, realize o cadastro!")
    return False

def listar_clientes():
    print("--- Listando Clientes ---")
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
    else:
        for c in clientes:
            print(f"Nome: {c[0]} - CPF: {c[1]}")
            print(f"Contato: {c[2]} - Endereço: {c[3]}")
            print("----------------------------")

def alterar_cliente():
    cpf = input("Digite o CPF: ")
    if buscar_cliente(cpf):
        for c in clientes:
            if c[1] == cpf:
                print("O que deseja alterar?")
                print("1. Nome")
                print("2. Contato")
                print("3. Endereço")
                print("0. Cancelar")
                op = int(input(">> "))

                if op == 1:
                    novoNome = input("Digite o nome correto: ")
                    c[0] = novoNome
                elif op == 2:
                    novoContato = input("Digite o novo do contato: ")
                    c[2] = novoContato
                elif op == 3:
                    novoEnd = input("Digite o novo endereço: ")
                    c[3] = novoEnd
                elif op == 0:
                    print("Operação Cancelada!")
                    return
                else:
                    print("Opção Inválida!")
                    continue

                print("Alteração realizada com sucesso!")

#Produtos ------------------------------------------------------------------
produtos = []


def cadastrar_produto():
    cnpj = input("Informe o CNPJ: ")
    if buscar_produto(cnpj):
        print("Erro!")
    else:
        print("---Cadastrar Produto---")
        nome = input("Informe o nome do produto: ")
        qtd = int(input("Informe a quantidade em estoque: "))
        produto = [nome, cnpj, qtd]
        produtos.append(produto)
        print(f"Produto {nome} cadastrado com sucesso!")


def buscar_produto(cnpj):
    print("---Buscar Produtos---")
    for p in produtos:
        if p[1] == cnpj:
            print(f"Produto {p[0]} está devidamente cadastrado!")
            print(f"Produto: {p[0]} - CNPJ: {p[1]} - Quantidade: {p[2]}")
            return True

    print("Produto não encontrado, realize o cadastro!")
    return False

def listar_produtos():
    print("---Listar Produtos---")
    if len(produtos) == 0:
        print("Não há produtos cadastrados!")
    else:
        for p in produtos:
            print(f"Produto: {p[0]} - CNPJ: {p[1]} - Estoque: {p[2]} ")

def alterar_produtos(cnpj):
    if buscar_produto(cnpj):
        for p in produtos:
            if p[1] == cnpj:
                print("O que você deseja alterar?")
                print("1. Nome")
                print("2. CNPJ")
                print("3. Estoque")
                print("0. Sair")
                op = int(input(">>> "))

                if op == 1:
                    novoNome = input("Informe o novo nome: ")
                    p[0] = novoNome
                elif op == 2:
                    novoCnpj = input("Informe o novo CNPJ: ")
                    p[1] = novoCnpj
                elif op == 3:
                    print("Deseja adicionar ou remover no estoque?")
                    print("1. Adicionar\n2. Remover")
                    op2 = int(input(">>> "))
                    if op2 == 1:
                        novoEstoque = int(input("Quanto vai adicionar ao estoque: "))
                        p[2] += novoEstoque
                    elif op2 == 2:
                        novoEstoque = int(input("Quanto vai remover do estoque: "))
                        p[2] -= novoEstoque
                        if p[2] < 0:
                            p[2] = 0
                    else:
                        print("Operação cancelada!")
                elif op == 0:
                    print("Operação cancelada!")
                    return
                else:
                    print("Opção inválida! Tente novamente...")
                    continue

                print("Dados alterados com sucesso!")

    else:
        print("Impossível realizar alteração!")

#Vendas ---------------------------------------------------------------
vendas = [] #[[cod, cnpj, nome_produto, cpf, nome_cliente, quantidade],[],[]]

def registrar_venda():
    print("=== Registrar Venda ===")
    try:
        cod = len(vendas)+1 #codigo autoincremental

        #Verificação Cliente
        cliente = None #variavel com referencia vazia
        cpf = input("Informe o CPF do cliente: ")
        if buscar_cliente(cpf):
            for c in clientes:
                if c[1] == cpf:
                    cliente = c #guarda a referencia de toda a lista com os dados do cliente
                    break
        else:
            print("Erro: Cliente não cadastrado!")
            return

        #Vericação do Produto
        produto = None
        cnpj = input("Informe o CNPJ do produto: ")
        if buscar_produto(cnpj):
            for p in produtos:
                if p[1] == cnpj:
                    produto = p
        else:
            print("Erro: Produto não existe.")
            return

        quantidade = int(input("Informe a quantidade a ser vendida: "))
        if quantidade <= 0:
            print("Quantidade Inválida!")
            return
        elif quantidade > produto[2]:
            print("Quantidade indisponível no estoque!")
            return

        produto[2] -= quantidade #atualizar o estoque

        #Registro da venda
        venda = [cod, cnpj,produto[0], cpf, cliente[0], quantidade ]
        vendas.append(venda)
        print(f"Venda (Código {cod}) registrada com sucesso!")
        print("\n=== NOTA FISCAL ===")
        print("Código da Venda: ", cod)
        print("CNPJ: ", cnpj)
        print("Produto: ", produto[0])
        print("CPF do cliente: ", cpf)
        print("Nome do Cliete: ", cliente[0])
        print("Quantidade: ", quantidade)

    except IndexError as e:
        print("Erro de índice: ",e)
    except ValueError as a:
        print("Erro de tipo: ", a)
    except Exception as g:
        print("Erro genérico: ", g)
