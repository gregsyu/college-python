produtos: list[float] = []

for p in range(6):
    print(f"Produto {p + 1}")
    preco = float(input(f"Informe o preco do Produto: {p + 1}"))
    produtos.append(preco)

print(f"O valor total da compra é: R${sum(produtos):.2f}")
print(f"O menor preco digitado é: R${min(produtos):.2f}")

encontrado: bool = False

print("Produtos:")
for i, p in enumerate(produtos):
    if p > 50:
        print(f"Produto {i}")
        encontrado = True

if not encontrado:
    print("Nenhum produto com preco maior que 50 encontrado.")
