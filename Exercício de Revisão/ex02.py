idosos = 0
adultos = 0
menores = 0

for i in range(20):
    idade = input(f"Pessoa {i + 1}º: Informe sua idade: ").strip()
    if idade == "":
        continue
    else:
        idade = int(idade)

    if idade >= 60:
        idosos += 1
    elif 18 <= idade < 60:
        adultos += 1
    else:
        menores += 1


print("\nQuantidade de pessoas idosas:", idosos)
print("Quantidade de pessoas adultos:", adultos)
print("Quantidade de pessoas menores de idade:", menores)
