resultado = 0


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_quadrado(base, altura):
    return base * altura


def area_circulo(diametro):
    pi = 3.14
    raio = diametro / 2
    return pi * raio ** 2


def area_losango(diagonal_maior, diagonal_menor):
    return (diagonal_maior * diagonal_menor) / 2


def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2


while True:
    print("==" * 20)
    print("Menu de Cálculos: ")
    print("1. Área do Triângulo")
    print("2. Área do quadrado")
    print("3. Área do círculo")
    print("4. Área do Losango")
    print("5. Área do Trapézio")
    print("0. Sair")
    opt = int(input("Digite a opção desejada: "))

    if opt not in range(6):
        print("Informe uma opcao valida!")
        continue

    if opt in [1, 2]:
        base = int(input("Informe a base: "))
        altura = int(input("Informe a altura: "))

    if opt == 1:
        resultado= area_triangulo(base, altura)
    elif opt == 2:
        resultado= area_quadrado(base, altura)
    elif opt == 3:
        diametro = int(input("Informe a diametro: "))
        resultado= area_circulo(diametro)
    elif opt == 4:
        diagonal_maior = int(input("Informe a diagonal maior: "))
        diagonal_menor = int(input("Informe a diagonal menor: "))
        resultado= area_losango(diagonal_maior, diagonal_menor)
    elif opt == 5:
        base_maior = int(input("Informe a base maior: "))
        base_menor = int(input("Informe a base menor: "))
        altura = int(input("Informe a altura: "))
        resultado= area_trapezio(base_maior, base_menor, altura)
    else:
        print("Adeus!")
        exit(0)

    print(f"\nO resultado é {resultado}.")
