while True:
    print("==" * 15)
    print("1. Maior numero e Menor numero")
    print("2. Multiplicacao")
    print("3. Média Aritmética")
    print("4. Sair")

    opcao = int(input("Opcao: "))

    if opcao == 4 or opcao == 0:
        print("Encerrando..")
        break

    n1 = int(input("Informe o primeiro numero: "))
    n2 = int(input("Informe o segundo numero: "))

    if opcao == 1:
        if n1 > n2:
            print(f"{n1} é o maior número e {n2} é o menor")
        elif n2 > n1:
            print(f"{n2} é o maior número e {n1} é o menor")
        else:
            print(f"{n1=} e {n2=} são iguais")
    elif opcao == 2:
        mult = n1 * n2
        print(f"{n1}x{n2} = {mult}")
    elif opcao == 3:
        media = (n1 + n2) / 2
        print(f"A média aritmética é {media}")
    else:
        print("Opção invalida!")
    print("")
