from menu import *
from model import *

def principal():
    while True:
        try:
            menu_principal()
            op = int(input(">> "))

            if op == 1:
                while True:
                    menu_cliente()
                    op2 = int(input(">> "))

                    if op2 == 1:
                        cadastrar_cliente()
                    elif op2 == 2:
                        cpf = input("Informe um CPF:")
                        buscar_cliente(cpf)
                    elif op2 == 3:
                        listar_clientes()
                    elif op2 == 4:
                        alterar_cliente()
                    elif op2 == 0:
                        print("Saindo do módulo de cliente...")
                        break
                    else:
                        print("Opção Inválida!")
            elif op == 2:
                while True:
                    menu_produto()
                    op2 = int(input("Digite a opção desejada\n>>> "))
                    if op2 == 1:
                        cadastrar_produto()
                    elif op2 == 2:
                        cnpj = input("Informe um CNPJ: ")
                        buscar_produto(cnpj)
                    elif op2 == 3:
                        listar_produtos()
                    elif op2 == 4:
                        cnpj = input("Informe um CNPJ: ")
                        alterar_produtos(cnpj)
                    elif op2 == 0:
                        print("Saindo do menu de produtos...")
                        break
                    else:
                        print("Opção inválida!")
            elif op == 3:
                while True:
                    menu_vendas()
                    op3 = int(input("Digite a opção desejada\n>>> "))
                    if op3 == 1:
                        registrar_venda()
                    elif op3 == 2:
                        cod = int(input("Informe o codigo da venda: "))
                        buscar_venda(cod)
                    elif op3 == 3:
                        listar_vendas()
                    elif op3 == 4:
                        cpf = input("Informe um CPF: ")
                        listar_vendas_cliente(cpf)
                    elif op3 == 5:
                        cnpj = input("Informe um CNPJ: ")
                        listar_vendas_produto(cnpj)
                    elif op3 == 0:
                        print("Saindo do menu de produtos...")
                        break
                    else:
                        print("Opção Inválida!")
            elif op == 0:
                print("Saindo do programa...")
                return
            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite Valores Inteiros!")

principal()
