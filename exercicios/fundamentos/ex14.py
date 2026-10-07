def soma_imposto(imposto: float, custo: float):
    taxa = imposto / 100.0
    valor = custo + (custo * taxa)
    return valor


def exibir_dados(taxa: float, custo: float, valor: float):
    return f"""O produto custava R${custo}
    Teve {taxa}% de imposto
    Agora custa R${valor}"""


taxa = float(input("Digite a taxa de imposto em %: "))
custo = float(input("Digite o preço de custo do produto: "))
valor = soma_imposto(taxa, custo=custo)

print(exibir_dados(taxa, custo, valor))
