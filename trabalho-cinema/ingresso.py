from filme import codigo_existe
from sessao import pegar_sessoes, salvar_sessoes
from os.path import exists
import csv

INGRESSOS = "ingressos.csv"


def pegar_ingressos():
    ingressos = []
    if exists(INGRESSOS):
        with open(INGRESSOS, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                ingressos.append(linha)
    return ingressos


def salvar_ingresso(ingresso):
    existe = exists(INGRESSOS)
    with open(INGRESSOS, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["codigo", "codigo_sessao", "nome", "cpf"]
        )
        if not existe:
            writer.writeheader()
        writer.writerow(ingresso)


def menu_ingresso():
    while True:
        print("\n---- MENU INGRESSO ----")
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
    sessoes = pegar_sessoes()
    ingressos = pegar_ingressos()

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
    ingressos = pegar_ingressos()
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
    ingressos = pegar_ingressos()
    codigo_sessao = input("Código da sessão: ").strip()
    encontrados = []
    for i in ingressos:
        if i["codigo_sessao"] == codigo_sessao:
            encontrados.append(i)

    if not encontrados:
        print("Nenhum ingresso encontrado para esta sessão.")
        return
    print(f"\n--- Ingressos da sessão {codigo_sessao} ---")
    for i in encontrados:
        print(f"{i['codigo']} | {i['nome']} | CPF: {i['cpf']}")


def listar_ingressos():
    ingressos = pegar_ingressos()
    if not ingressos:
        print("Nenhum ingresso vendido.")
        return
    print("\n--- Todos os Ingressos ---")
    for i in ingressos:
        print(
            f"{i['codigo']} | Sessão: {i['codigo_sessao']} | " +
            f"{i['nome']} | CPF: {i['cpf']}"
        )
