salario_liquido = 0
desconto = 0

for i in range(10):
    # salario bruto
    s = int(input(f"Pessoa {i + 1}º Informe o seu sálario bruto: "))

    if s <= 1_500:
        desconto = 1
    elif 1_500 < s <= 2_000:
        desconto = 0.10
    elif 2_000 < s <= 3_500:
        desconto = 0.15
    else:
        desconto = 0.20

    salario_liquido = s - (s * desconto)

    print(f"\nO desconto do INSS: {desconto:.2f}")
    print(f"O salario liquido {salario_liquido:.2f}")
