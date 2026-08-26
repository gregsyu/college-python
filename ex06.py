alunos = ["Ana", "Bruno", "Carla", "Diego"]

print(
    alunos[0],
    alunos[-1]
)

alunos.append("Marina")

alunos.insert(1, "Felipe")

alunos.remove("Bruno")

alunos.sort()

for k, v in enumerate(alunos):
    print(k + 1, v)
