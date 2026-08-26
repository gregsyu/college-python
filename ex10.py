nomes: list[str] = []
idades: list[int] = []

for i in range(8):
    print(f"\nPessoa {i + 1} ")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    nomes.append(nome)
    idades.append(idade)

media = sum(idades) / len(idades)  # soma/qtd
print(f"A media das idades é {media:.2f}")

menor = idades.index(min(idades))
print(f"A pesoa com a menor idade é {menor}")

print("\n --- Pessoas menores de idade ---")
encontrado = False

for i in enumerate(idades):
    if i[1] < 10:
        indice = idades.index(i)
        print(f"Nome: {nomes[i[0]]} - Idade: {i[1]}")
        encontrado = True

if not encontrado:
    print("Nao ha menores de idade")
