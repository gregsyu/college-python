aprovados = 0
reprovados = 0
recuperacao = 0
maior = 0
media = 0
m_nome = "vazio"

for i in range(20):
    while True:
        nome = input(f"Aluno {i + 1}º Informe seu nome: ").split()[0]
        nota = float(input(f"Aluno {i + 1}º Informe a nota do aluno: "))

        if not (0 <= nota <= 10):
            print("Nota Invalida!")
            continue
        else:
            break

    if i == 0:
        maior = nota
        m_nome = nome
    elif maior < nota:
        maior = nota
        m_nome = nome

    if nota >= 7:
        aprovados += 1
    elif 4 <= nota < 7:
        recuperacao += 1
    elif nota < 4:
        reprovados += 1

    media += nota

media = media / 20
print(f"\nMédia da turma: {media:.2f}")
print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos em recuperacao: {recuperacao}")
print(f"Quantidade de alunos reprovados: {reprovados}")
print(f"Maior nota da turma foi de {m_nome.capitalize()}: {maior}")
