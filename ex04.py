(soma_total, media, quant) = (0, 0, 0)

while True:
    altura = float(
        input("Informe a altura (em metros): ")
        .lower()
        .replace("m", "")
        )
    quant += 1
    soma_total += altura

    if altura <= 0:
        break
    print("")

media = soma_total / quant
print(f"A quantidade de alturas informadas são \x1b[32;1m{quant}\x1b[m.")
print(f"A média das alturas é \x1b[32;1m{media:.2f}\x1b[m.")
