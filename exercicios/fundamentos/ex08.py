carros: list[str] = []
consumos: list[float] = []

for i in range(5):
    print(f"Carro {i + 1}:")
    modelo = input("Informe o modelo do carro: ")
    consumo = float(input("Informe o consumo de caro (km): "))
    print("")

    carros.append(modelo)
    consumos.append(consumo)


indice = consumos.index(max(consumos))
print(f"O carro mais economico é {carros[indice]}")
