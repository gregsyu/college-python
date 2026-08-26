original: list[int] = list()
lista2: list[int] = list()
qtd = 0

for i in range(10):
    numero = int(input(f"Digite o {i + 1}o número: "))
    lista2.append(numero)


print("Lista original")
for n in original:
    print(n)
    if n > 50:
        lista2.append(n)
    elif n < 10:
        qtd += 1

if len(lista2) > 0:
    print("Numeros maiores que 50:")
    for n in lista2:
        print(n)
else:
    print("Nao ha numeros maiores que 50 na lista.")

print(f"A quantidade de numeros menores que 10 é: {qtd}")
