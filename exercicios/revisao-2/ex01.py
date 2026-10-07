from datetime import datetime


def main():
    veiculos: list[list[str | int]] = []
    i = 1

    while True:
        print("=" * 25)
        print(f"\tVEICULO º{i}")
        print("=" * 25)

        veiculo: list[str | int] = [i]
        veiculo.extend(cadastrar_veiculo())
        veiculos.append(veiculo)

        continuar = input("\n\x1b[32mDeseja cadastrar mais um?\x1b[m ").strip().lower()
        if continuar in ["sim", "s", "y", "1"]:
            print()
        else:
            break

        i += 1

    print("-" * 25)

    for v in veiculos:
        nasc = int(v[2])
        idade = calc_idade(nasc)
        km: int = int(v[3])

        print(f"VEICULO º{v[0]} - {v[1]}")
        print(classificar_pela_idade(idade))
        print(classificar_pelo_uso(idade, km))
        print(classificar_pela_quilometragem(km))
        print("-" * 25)


def cadastrar_veiculo() -> list[str | int]:
    modelo = input("Informe modelo: ")
    nasc = int(input("Informe o ano de fabricacao: "))
    km = int(input("Informe a quilometragem atual: "))

    return [modelo, nasc, km]

def calc_idade(nasc: int) -> int:
    ano_atual = datetime.now().year
    return abs(nasc - ano_atual)

def classificar_pela_idade(idade: int) -> str:
    match idade:
        case _ if idade <= 3:
            resultado = "Novo"
        case _ if 4 <= idade <= 10:
            resultado = "Seminovo"
        case _ if idade > 10:
            resultado = "Antigo"
        case _:
            pass
    
    return f"O veiculo é {resultado.lower()}."

def classificar_pelo_uso(idade: int, km: int) -> str:
    match (idade, km):
        case _ if idade <= 5 and km > 80_000:
            resultado = "veiculo de uso intenso"
        case _ if idade > 5 and km < 50_000:
            resultado = "veiculo de uso leve"
        case _:
            resultado = "veiculo de uso regular"

    return f"É um {resultado}."

def classificar_pela_quilometragem(km: int) -> str:
    match km:
        case _ if km <= 30_000:
            resultado = "Baixa quilometragem"
        case _ if 30_000 < km <= 100_000:
            resultado = "Quilometragem media"
        case _ if km > 100_000:
            resultado = "Alta quilometragem"
        case _:
            pass

    return f"O veiculo tem {resultado.lower()}."


if __name__ == "__main__":
    main()
