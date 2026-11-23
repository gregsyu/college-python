ARQUIVO = "alunos.txt"

def cadastrar_aluno():
    pass

def listar_aluno():
    pass

def buscar_aluno():
    with open(ARQUIVO, "r") as _arq:
        ...

def main():
    while True:
        print("=== SISTEMA DE ALUNOS ===")
        print("1. Cadastrar alunos")
        print("2. Listar alunos")
        print("3. Buscar alunos")
        print("4. Sair")
   