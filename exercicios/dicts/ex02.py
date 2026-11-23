empresas = []

def cadastrar_empresas():
    print("--- Cadastro de Empresas ---")
    nome = input("Digite o nome da empresa: ")
    cnpj = input("Digite o CNPJ da empresa: ")


def buscar_empresa(cnpj):
    print("--- Busca de empresa ---")
    for empresa in empresas:
        if empresas["cpnj"] == cnpj:
            return empresa
    print("Empresa nao encontrada")
    return False