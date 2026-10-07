nomes = []
n_tempos = []
tempos = []

for i in range(10):
    nome = input("Insira o nome: ")
    tempo = int(input("Insira o tempo (em horas): "))

    if tempo > 10:
        n_tempos.append(nome)

    tempos.append(tempo)
    nomes.append(nome)


indice = tempos

print(max(tempos))
