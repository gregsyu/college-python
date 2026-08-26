pi = 3.14

while True:
    print("""========================
    Menu de Cálculos:
    1. Área do Triângulo
    2. Área do quadrado
    3. Área do círculo
    0. Sair
    ==========================""")
    opcao = int(input("Digite a opção desejada: "))

    if opcao not in range(1, 4):
        break

    if opcao == 1:
        prompt = "Triângulo"
        base = int(input("Informe a base do Triângulo: "))
        altura = int(input("Informe a altura do Triangulo: "))
        resultado = (base * altura) / 2
    elif opcao == 2:
        prompt = "Quadrado"
        base = int(input("Informe a base do Quadrado: "))
        altura = int(input("Informe a altura do Quadrado: "))
        resultado = base * altura
    elif opcao == 3:
        prompt = "Círculo"
        base = int(input(f"Informe a base do Circulo: "))
        altura = int(input(f"Informe a altura do Circulo: "))
        resultado = pi * (base / 2) ** 2

    print(f"\nA Área do {prompt} é: {resultado}")
