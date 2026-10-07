i = 1
total = 0

while i < 10:
    print(f"Pessoa {i}")
    idade = int(input("Idade: "))
    alfa = input("É alfabetizado (S/n): ").lower()

    if idade >= 18:
        if alfa == "s":
            print("Pode tirar \x1b[32mCNH\x1b[m")
        else:
            print("Não pode tirar \x1b[31mCNH\x1b[m: Pessoa não alfabetizada!")
    else:
        print("Não pode tirar \x1b[31mCNH\x1b[m: Pessoa menor de Idade!")
    print()
    i += 1
    total += 1

print("Total de aptos a tirar \x1b[33mCNH\x1b[m:", total)