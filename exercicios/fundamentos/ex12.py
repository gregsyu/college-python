ap: list[str] = []
rp: list[float] = []
soma = 0

for n in range(1, 6):
    print(f"Aluno {n}")
    nome = input("Digite o nome: ")

    for n in range(1, 4):
        nota = float(input(f"Digite a {n}: "))
        soma += nota

    media = soma / 3

    if media >= 7:
        ap.append((nome, media))
    else:
        rp.append((nome, media))


    if media >= 7:
        notas.append(nome)