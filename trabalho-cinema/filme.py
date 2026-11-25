from os.path import exists

FILMES = "filmes.txt"


def codigo_existe(lista, codigo):
    for item in lista:
        if item["codigo"] == codigo:
            return True
    return False


def pegar_filmes():
    filmes: list[dict[str, str]] = []

    if exists(FILMES):
        with open(FILMES, "r", encoding="utf-8") as arq:
            for linha in arq:
                p = linha.strip().split("|")
                if len(p) == 4:
                    filmes.append(
                        {
                            "codigo": p[0],
                            "titulo": p[1],
                            "genero": p[2],
                            "duracao": p[3],
                        }
                    )
    return filmes


def salvar_filmes(filmes):
    # "w" reescreve o arquivo do zero
    with open(FILMES, "w", encoding="utf-8") as f:
        for filme in filmes:
            f.write(
                f"{filme['codigo']}|{filme['titulo']}|"
                + f"{filme['genero']}|{filme['duracao']}\n"
            )


def menu_filme():
    while True:
        print("\n---- MENU FILME ----")
        print("1. Cadastrar")
        print("2. Buscar por Código")
        print("3. Listar Todos")
        print("0. Voltar")
        op = input("Opção: ").strip()

        if op == "1":
            cadastrar_filme()
        elif op == "2":
            buscar_filme()
        elif op == "3":
            listar_filmes()
        elif op == "0":
            break
        else:
            print("Opção inválida!")


def cadastrar_filme():
    filmes = pegar_filmes()
    codigo = input("Código do filme: ").strip()

    if codigo_existe(filmes, codigo):
        print("Código já existe!")
        return

    titulo = input("Título: ").strip()
    genero = input("Gênero: ").strip()
    duracao = input("Duração (minutos): ").strip()
    filmes.append(
        {"codigo": codigo, "titulo": titulo,
            "genero": genero, "duracao": duracao}
    )
    salvar_filmes(filmes)
    print("Filme cadastrado com sucesso!")


def buscar_filme():
    filmes = pegar_filmes()
    codigo = input("Código do filme: ").strip()

    for f in filmes:
        if f["codigo"] == codigo:
            print(f"\nCódigo: {f['codigo']}")
            print(f"Título: {f['titulo']}")
            print(f"Gênero: {f['genero']}")
            print(f"Duração: {f['duracao']} min")
            return
    print("Filme não encontrado.")


def listar_filmes():
    filmes = pegar_filmes()

    if not filmes:
        print("Nenhum filme cadastrado.")
        return

    print("\n--- Lista de Filmes ---")

    for f in filmes:
        print(
            f"{f['codigo']} | {f['titulo']} | "
            + f"{f['genero']} | {f['duracao']} min"
        )
