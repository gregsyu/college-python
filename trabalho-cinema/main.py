import os
import csv

# Arquivos
FILMES_ARQ = "filmes.txt"
SESSOES_ARQ = "sessoes.txt"
INGRESSOS_ARQ = "ingressos.csv"

# ---------- Funções auxiliares ----------
def carregar_filmes():
    filmes = []
    if os.path.exists(FILMES_ARQ):
        with open(FILMES_ARQ, "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split("|")
                if len(partes) == 4:
                    filmes.append({
                        "codigo": partes[0],
                        "titulo": partes[1],
                        "genero": partes[2],
                        "duracao": partes[3]
                    })
    return filmes

def salvar_filmes(filmes):
    with open(FILMES_ARQ, "w", encoding="utf-8") as f:
        for filme in filmes:
            f.write(f"{filme['codigo']}|{filme['titulo']}|{filme['genero']}|{filme['duracao']}\n")

def carregar_sessoes():
    sessoes = []
    if os.path.exists(SESSOES_ARQ):
        with open(SESSOES_ARQ, "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split("|")
                if len(partes) == 5:
                    sessoes.append({
                        "codigo": partes[0],
                        "codigo_filme": partes[1],
                        "sala": partes[2],
                        "horario": partes[3],
                        "lugares": int(partes[4])
                    })
    return sessoes

def salvar_sessoes(sessoes):
    with open(SESSOES_ARQ, "w", encoding="utf-8") as f:
        for s in sessoes:
            f.write(f"{s['codigo']}|{s['codigo_filme']}|{s['sala']}|{s['horario']}|{s['lugares']}\n")

def carregar_ingressos():
    ingressos = []
    if os.path.exists(INGRESSOS_ARQ):
        with open(INGRESSOS_ARQ, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for row in leitor:
                ingressos.append(row)
    return ingressos

def salvar_ingresso(ingresso):
    existe = os.path.exists(INGRESSOS_ARQ)
    with open(INGRESSOS_ARQ, "a", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=["codigo", "codigo_sessao", "nome", "cpf"])
        if not existe:
            escritor.writeheader()
        escritor.writerow(ingresso)

def codigo_existe(lista, codigo, chave="codigo"):
    return any(item[chave] == codigo for item in lista)

# ---------- Menus de Filme ----------
def menu_filme():
    while True:
        print("\n=== MENU FILME ===")
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
    filmes = carregar_filmes()
    codigo = input("Código do filme: ").strip()
    if codigo_existe(filmes, codigo):
        print("Código já existe!")
        return
    titulo = input("Título: ").strip()
    genero = input("Gênero: ").strip()
    duracao = input("Duração (minutos): ").strip()
    filmes.append({"codigo": codigo, "titulo": titulo, "genero": genero, "duracao": duracao})
    salvar_filmes(filmes)
    print("Filme cadastrado com sucesso!")

def buscar_filme():
    filmes = carregar_filmes()
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
    filmes = carregar_filmes()
    if not filmes:
        print("Nenhum filme cadastrado.")
        return
    print("\n--- Lista de Filmes ---")
    for f in filmes:
        print(f"{f['codigo']} | {f['titulo']} | {f['genero']} | {f['duracao']} min")

# ---------- Menus de Sessão ----------
def menu_sessao():
    while True:
        print("\n=== MENU SESSÃO ===")
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
    sessoes = carregar_sessoes()
    filmes = carregar_filmes()

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
    try:
        lugares = int(input("Lugares disponíveis: ").strip())
    except ValueError:
        print("Número de lugares inválido!")
        return

    sessoes.append({
        "codigo": codigo,
        "codigo_filme": codigo_filme,
        "sala": sala,
        "horario": horario,
        "lugares": lugares
    })
    salvar_sessoes(sessoes)
    print("Sessão cadastrada com sucesso!")

def listar_sessoes():
    sessoes = carregar_sessoes()
    if not sessoes:
        print("Nenhuma sessão cadastrada.")
        return
    print("\n--- Lista de Sessões ---")
    for s in sessoes:
        print(f"{s['codigo']} | Filme: {s['codigo_filme']} | Sala: {s['sala']} | {s['horario']} | Lugares: {s['lugares']}")

def listar_sessoes_por_filme():
    sessoes = carregar_sessoes()
    codigo_filme = input("Código do filme: ").strip()
    encontradas = [s for s in sessoes if s["codigo_filme"] == codigo_filme]
    if not encontradas:
        print("Nenhuma sessão encontrada para este filme.")
        return
    print(f"\n--- Sessões do filme {codigo_filme} ---")
    for s in encontradas:
        print(f"{s['codigo']} | Sala: {s['sala']} | {s['horario']} | Lugares: {s['lugares']}")

# ---------- Menus de Ingresso ----------
def menu_ingresso():
    while True:
        print("\n=== MENU INGRESSO ===")
        print("1. Vender Ingresso")
        print("2. Buscar por Código")
        print("3. Listar por Sessão")
        print("4. Listar Todos")
        print("0. Voltar")
        op = input("Opção: ").strip()

        if op == "1":
            vender_ingresso()
        elif op == "2":
            buscar_ingresso()
        elif op == "3":
            listar_ingressos_por_sessao()
        elif op == "4":
            listar_ingressos()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

def vender_ingresso():
    sessoes = carregar_sessoes()
    ingressos = carregar_ingressos()

    codigo = input("Código do ingresso: ").strip()
    if codigo_existe(ingressos, codigo):
        print("Código de ingresso já existe!")
        return

    codigo_sessao = input("Código da sessão: ").strip()
    sessao = None
    for s in sessoes:
        if s["codigo"] == codigo_sessao:
            sessao = s
            break

    if sessao is None:
        print("Sessão não cadastrada!")
        return

    if sessao["lugares"] <= 0:
        print("Sessão esgotada! Não é possível vender mais ingressos.")
        return

    nome = input("Nome do cliente: ").strip()
    cpf = input("CPF: ").strip()

    # Diminui os lugares
    sessao["lugares"] -= 1
    salvar_sessoes(sessoes)

    # Salva o ingresso
    salvar_ingresso({
        "codigo": codigo,
        "codigo_sessao": codigo_sessao,
        "nome": nome,
        "cpf": cpf
    })
    print("Ingresso vendido com sucesso!")
    if sessao["lugares"] == 0:
        print("Atenção: esta sessão agora está esgotada.")

def buscar_ingresso():
    ingressos = carregar_ingressos()
    codigo = input("Código do ingresso: ").strip()
    for i in ingressos:
        if i["codigo"] == codigo:
            print(f"\nCódigo: {i['codigo']}")
            print(f"Sessão: {i['codigo_sessao']}")
            print(f"Cliente: {i['nome']}")
            print(f"CPF: {i['cpf']}")
            return
    print("Ingresso não encontrado.")

def listar_ingressos_por_sessao():
    ingressos = carregar_ingressos()
    codigo_sessao = input("Código da sessão: ").strip()
    encontrados = [i for i in ingressos if i["codigo_sessao"] == codigo_sessao]
    if not encontrados:
        print("Nenhum ingresso encontrado para esta sessão.")
        return
    print(f"\n--- Ingressos da sessão {codigo_sessao} ---")
    for i in encontrados:
        print(f"{i['codigo']} | {i['nome']} | CPF: {i['cpf']}")

def listar_ingressos():
    ingressos = carregar_ingressos()
    if not ingressos:
        print("Nenhum ingresso vendido.")
        return
    print("\n--- Todos os Ingressos ---")
    for i in ingressos:
        print(f"{i['codigo']} | Sessão: {i['codigo_sessao']} | {i['nome']} | CPF: {i['cpf']}")

# ---------- Menu Principal ----------
def menu_principal():
    while True:
        print("\n========== CINEMA ==========")
        print("1. Filme")
        print("2. Sessão")
        print("3. Ingresso")
        print("0. Sair")
        op = input("Opção: ").strip()

        if op == "1":
            menu_filme()
        elif op == "2":
            menu_sessao()
        elif op == "3":
            menu_ingresso()
        elif op == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida!")

# Inicia o programa
if __name__ == "__main__":
    menu_principal()