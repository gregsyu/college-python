from os.path import exists
from filme import codigo_existe, pegar_filmes

SESSOES = "sessoes.txt"


def pegar_sessoes():
    sessoes = []
    if exists(SESSOES):
        with open(SESSOES, "r", encoding="utf-8") as f:
            for linha in f:
                p = linha.strip().split("|")
                if len(p) == 5:
                    sessoes.append(
                        {
                            "codigo": p[0],
                            "codigo_filme": p[1],
                            "sala": p[2],
                            "horario": p[3],
                            "lugares": int(p[4]),
                        }
                    )
    return sessoes


def salvar_sessoes(sessoes):
    with open(SESSOES, "w", encoding="utf-8") as arq:
        for s in sessoes:
            arq.write(
                f"{s['codigo']}|{s['codigo_filme']}|{s['sala']}|"
                + f"{s['horario']}|{s['lugares']}\n"
            )


def menu_sessao():
    while True:
        print("\n---- MENU SESSÃO ----")
        print("1. Cadastrar")
        print("2. Listar Todas")
        print("3. Listar por Filme")
        print("0. Voltar")
        op = input("Opção: ").strip()

        if op == "1":
            cadastrar_sessao()
        elif op == "2":
            listar_sessoes()
        elif op == "3":
            listar_sessoes_por_filme()
        elif op == "0":
            break
        else:
            print("Opção inválida!")


def cadastrar_sessao():
    sessoes = pegar_sessoes()
    filmes = pegar_filmes()

    codigo = input("Código da sessão: ").strip()
    if codigo_existe(sessoes, codigo):
        print("Código de sessão já existe!")
        return

    codigo_filme = input("Código do filme: ").strip()
    if not codigo_existe(filmes, codigo_filme):
        print("Filme não cadastrado!")
        return

    sala = input("Sala: ").strip()
    horario = input("Horário: ").strip()

    for s in sessoes:
        if s['sala'] == sala and s['horario'] == horario:
            print("Já existe uma sessao nessa sala e no mesmo horario")
            return

    try:
        lugares = int(input("Lugares disponiveis (no maximo 100): ").strip())
    except ValueError:
        print("Número de lugares invalido!")
        return

    if lugares > 100 or lugares < 0:
        print("Número de lugares invalido!")
        return

    sessoes.append(
        {
            "codigo": codigo,
            "codigo_filme": codigo_filme,
            "sala": sala,
            "horario": horario,
            "lugares": lugares,
        }
    )
    salvar_sessoes(sessoes)
    print("Sessão cadastrada com sucesso!")


def listar_sessoes():
    sessoes = pegar_sessoes()

    if not sessoes:
        print("Nenhuma sessão cadastrada.")
        return

    print("\n--- Lista de Sessões ---")

    for s in sessoes:
        print(
            f"{s['codigo']} | Filme: {s['codigo_filme']} | "
            + f"Sala: {s['sala']} | {s['horario']} | Lugares: {s['lugares']}"
        )


def listar_sessoes_por_filme():
    sessoes = pegar_sessoes()
    codigo_filme = input("Código do filme: ").strip()
    encontradas = []
    for s in sessoes:
        if s["codigo_filme"] == codigo_filme:
            encontradas.append(s)

    if not encontradas:
        print("Nenhuma sessão encontrada para este filme.")
        return

    print(f"\n--- Sessões do filme {codigo_filme} ---")

    for s in encontradas:
        print(
            f"{s['codigo']} | Sala: {s['sala']} | "
            + f"{s['horario']} | Lugares: {s['lugares']}"
        )
