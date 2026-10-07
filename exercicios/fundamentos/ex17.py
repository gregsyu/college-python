alunos = [
    ("Ana", 20, "SIF"),
    ("Carlos", 22, "ADM"),
    ("João", 19, "ADM"),
    ("Beatriz", 22, "SIF"),
    ("Manoel", 19, "ENF"),
    ("Jario", 26, "SIF"),
    ("Daniel", 18, "SIF"),
    ("Ricardo", 17, "SIF"),
]


def maior_idade():
    maior = alunos[0]

    for a in alunos:
        if a[1] > maior[1]:
            maior = a

    print(f"O aluno com a maior idade é: {maior[0]}")


def menor_idade():
    menor = alunos[0]

    for a in alunos:
        if a[1] > menor[1]:
            menor = a

    print(f"O aluno com a maior idade é: {menor[0]}")


def listar_curso(curso):
    encontrado = False

    print(f"Listando alunos de {curso}")

    for a in alunos:
        if a[2] 


# alunes = []
# maior_idade = ["", 0, ""]
# # menor_idade = ["", 0, ""]

# for aluno in alunos:
    # if aluno[1] > maior_idade[1]:
        # maior_idade = aluno[::]
    # alunes.append(maior_idade)
    # alunos.remove
    # # if aluno[1] < menor_idade[1]:
    # # menor_idade = aluno[::]

# print(alunos)
# print(alunes)
