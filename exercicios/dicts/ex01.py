cidades = []
eleitores = []
 
proximo_codigo = 1

def cadastrar_cidade():
    global proximo_codigo
 
    nome = input("Nome da cidade: ").strip()
    estado = input("Estado (UF): ").strip().upper()
 
    if not nome or not estado:
        print("Nome e estado são obrigatórios!")
        return
 
    cidade = {
        "codigo": proximo_codigo,
        "nome": nome,
        "estado": estado
    }
 
    cidades.append(cidade)
 
    print(f"Cidade cadastrada com sucesso! Código: {proximo_codigo}")
    proximo_codigo += 1



def buscar_cidade():
    try:
        codigo = int(input("Digite o código da cidade: "))
    except ValueError:
        print("Código inválido!")
        return
 
    for cidade in cidades:
        if cidade["codigo"] == codigo:
            print("\nCidade encontrada:")
            print(f"Código: {cidade['codigo']}")
            print(f"Nome: {cidade['nome']}")
            print(f"Estado: {cidade['estado']}")
            return
 
    print("Cidade não encontrada!")



def listar_cidades():
    if not cidades:
        print("Nenhuma cidade cadastrada.")
        return
 
    print("\n=== LISTA DE CIDADES ===")
 
    for cidade in cidades:
        print(
            f"Código: {cidade['codigo']} | "
            f"Nome: {cidade['nome']} | "
            f"Estado: {cidade['estado']}"
        )
 
 
 
def cadastrar_eleitor():
    nome = input("Nome do eleitor: ").strip()
    titulo = input("Número do título de eleitor: ").strip()
 
    if not nome or not titulo:
        print("Nome e título são obrigatórios!")
        return
 
 
    for eleitor in eleitores:
        if eleitor["titulo"] == titulo:
            print("Já existe um eleitor com esse título!")
            return
 
    if not cidades:
        print("Cadastre uma cidade antes de cadastrar eleitores.")
        return
 
    listar_cidades()
 
    try:
        codigo = int(input("Digite o código da cidade do eleitor: "))
    except ValueError:
        print("Código inválido!")
        return
 
    cidade_encontrada = None
 
    for cidade in cidades:
        if cidade["codigo"] == codigo:
            cidade_encontrada = cidade
            break
 
    if cidade_encontrada is None:
        print("Cidade não encontrada!")
        return
 
    eleitor = {
        "nome": nome,
        "titulo": titulo,
        "cidade": cidade_encontrada["nome"]
    }
 
    eleitores.append(eleitor)
 
    print("Eleitor cadastrado com sucesso!")
 
 
 
def listar_eleitores():
    if not eleitores:
        print("Nenhum eleitor cadastrado.")
        return
 
    print("\n=== LISTA DE ELEITORES ===")
 
    for eleitor in eleitores:
        print("-" * 40)
        print(f"Nome: {eleitor['nome']}")
        print(f"Título: {eleitor['titulo']}")
        print(f"Cidade: {eleitor['cidade']}")
 
 
 
def buscar_eleitor():
    titulo = input("Digite o número do título: ").strip()
 
    for eleitor in eleitores:
        if eleitor["titulo"] == titulo:
            print("\nEleitor encontrado:")
            print(f"Nome: {eleitor['nome']}")
            print(f"Título: {eleitor['titulo']}")
            print(f"Cidade: {eleitor['cidade']}")
            return
 
    print("Eleitor não encontrado!")
 
 
 
def listar_eleitores_por_cidade():
    if not cidades:
        print("Nenhuma cidade cadastrada.")
        return
 
    listar_cidades()
 
    try:
        codigo = int(input("Digite o código da cidade: "))
    except ValueError:
        print("Código inválido!")
        return
 
    cidade_encontrada = None
 
    for cidade in cidades:
        if cidade["codigo"] == codigo:
            cidade_encontrada = cidade
            break
 
    if cidade_encontrada is None:
        print("Cidade não encontrada!")
        return
 
    print(f"\n=== ELEITORES DE {cidade_encontrada['nome']} ===")
 
    encontrados = 0
 
    for eleitor in eleitores:
        if eleitor["cidade"] == cidade_encontrada["nome"]:
            print(
                f"Nome: {eleitor['nome']} | " +
                f"Título: {eleitor['titulo']}"
            )
            encontrados += 1
 
    if encontrados == 0:
        print("Não existem eleitores cadastrados nessa cidade.")



def main():
    while True:
        print("\n===== SISTEMA DE CONTROLE DE ELEITORES =====")
        print("1 - Cadastrar cidade")
        print("2 - Buscar cidade pelo código")
        print("3 - Listar todas as cidades")
        print("4 - Cadastrar eleitor")
        print("5 - Listar todos os eleitores")
        print("6 - Buscar eleitor pelo título")
        print("7 - Listar eleitores por cidade")
        print("0 - Sair")
 
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            cadastrar_cidade()
        elif opcao == "2":
            buscar_cidade()
        elif opcao == "3":
            listar_cidades()
        elif opcao == "4":
            cadastrar_eleitor()
        elif opcao == "5":
            listar_eleitores()
        elif opcao == "6":
            buscar_eleitor()
        elif opcao == "7":
            listar_eleitores_por_cidade()
        elif opcao == "0":
            print("Sistema encerrado!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
