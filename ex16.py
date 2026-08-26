pessoas: list[str] = []


def menu():
    while True:
        print("=" * 15)
        print("1. Cadastrar")
        print("2. Buscar")
        print("3. Listar")
        print("0. Sair")

        op = int(input("Opção: "))

        if op == 1:
            cadastrar()
        elif op == 2:
            cpf = input("Digite o CPF a ser buscado: ")
            _ = buscar(cpf)
        elif op == 3:
            listar()
        elif op == 0:
            return
        else:
            print("Opção invalida. Tente novamente, seu fudido!")


def cadastrar():
    cpf = input("Digite o CPF: ")
    if buscar(cpf):
        print("Erro ao cadastrar.")
        return

    pessoas.append(cpf)


def buscar(cpf: str) -> str | bool:
    for p in pessoas:
        if cpf == p:
            print("CPF encontrado na base de dados.")
            return cpf

    print("CPF não existe na base de dados. Efetue o cadastro.")
    return False


def listar():
    for i, p in enumerate(pessoas):
        print(f"Indice: {i + 1}, CPF: {p}")


menu()
