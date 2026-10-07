for i in range(1, 6):
    print(f"Compra {i}")
    valor = float(input("Valor da Compra (R$): "))

    if valor <= 100:
        percent = "10%"
        desconto = valor * 0.1
    elif 100 < valor <= 500:
        percent = "12%"
        desconto = valor * 0.12
    else:
        percent = "15%"
        desconto = valor * 0.15

    valor_final = valor - desconto
    print(f"==== Situação Compra {i} ====")
    print(f"Valor Original: R${valor:.2f}")
    print(f"Percentual de desconto: R${percent:.2f}")
    print(f"Valor do desconto: R${desconto:.2f}")
    print(f"Valor final: R${valor_final:.2f}")
