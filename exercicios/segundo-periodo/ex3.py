def bonificacao(salario: float) -> float:
    if salario <= 1500:
        return salario * 0.05
    elif salario <= 2500:
        return salario * 0.12
    else:
        return 0


def auxilio(salario: float) -> float:
    if salario <= 3000:
        return 150
    else:
        return 100


def desconto_inss(salario: float) -> float:
    if salario <= 1600:
        return salario * 0.07
    elif salario <= 3000:
        return salario * 0.08
    else:
        return salario * 0.10


def desconto_ir(salario: float) -> float:
    if salario <= 2500:
        return 0
    elif salario <= 4000:
        return salario * 0.12
    else:
        return salario * 0.15


def principal():
    salario_bruto = float(input("Informe o seu salário: R$ "))

    valor_bonificacao = bonificacao(salario_bruto)
    valor_auxilio = auxilio(salario_bruto)
    valor_inss = desconto_inss(salario_bruto)
    valor_ir = desconto_ir(salario_bruto)

    salario_liquido = (salario_bruto + valor_bonificacao + valor_auxilio - valor_inss - valor_ir)

    print("\n-----------------")
    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"Bonificação: R$ {valor_bonificacao:.2f}")
    print(f"Auxílio escola: R$ {valor_auxilio:.2f}")
    print(f"Desconto INSS: R$ {valor_inss:.2f}")
    print(f"Desconto IR: R$ {valor_ir:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")


if __name__ == "__main__":
    principal()
