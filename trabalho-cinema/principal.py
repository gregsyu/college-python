from filme import menu_filme
from sessao import menu_sessao
from ingresso import menu_ingresso


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


if __name__ == "__main__":
    menu_principal()
