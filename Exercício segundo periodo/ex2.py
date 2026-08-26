def somar_dois(n1, n2):
    return n1 + n2


def raiz_quadrada(num):
    return num ** (1/2)


def potencia(n1, n2):
    return n1 ** n2


while True:
    print("=============================")
    print("Menu de opções:")
    print("1. Somar dois números.")
    print("2. Raiz quadrada de um número.")
    print("3. Potência de um número")
    print("0. Sair")
    opt = input("Digite a opção desejada: ")

    if opt not in range(4):
        print("Informe uma opcao valida!")
        continue

    if opt == 1:
        n1 = int(input("Informe o primeiro numero: "))
        n2 = int(input("Informe o segundo numero: "))
        resultado = somar_dois(n1, n2)
    elif opt == 2:
        num = int(input("Informe o numero: "))
        resultado = raiz_quadrada(num)
    elif opt == 3:
        n1 = int(input("Informe o primeiro numero: "))
        n2 = int(input("Informe o segundo numero: "))
        resultado = potencia(n1, n2)
    else:
        print("Adeus!")
        exit(0)

    print(f"\nO resultado é {resultado}.")
