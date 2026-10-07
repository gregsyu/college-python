def calc_media(nota1: float, nota2: float):
    media = (nota1 + nota2) / 2
    return media


def status(media: float):
    msg = f"Media: {media:.2f}\n"
    if media >= 7:
        msg += "Aprovado por media"
    elif media >= 3:
        msg += "Prova Final"
    else:
        msg += "Reprovado"

    return msg


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = calc_media(n1, n2)
print("\n", status(media), sep="")
