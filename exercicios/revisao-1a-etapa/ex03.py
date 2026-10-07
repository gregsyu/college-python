i, media, menor, maior = 1, 0, 0, 0

while True:
    idade = int(input(f"Pessoa {i}º: Insira sua idade: "))

    if idade == -1:
        break
    elif i == 1:
        maior = idade
        menor = idade
    elif maior < idade:
        maior = idade
    elif menor > idade:
        menor = idade

    media += idade
    i += 1

media = media / i
print("\nMaior idade:", maior)
print("Menor idade:", menor)
print("Média:", media)
