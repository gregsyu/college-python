ap, rc, rp = 0, 0, 0
nota1, nota2 = 0.0, 0.0


for i in range(1, 6):
    print(f"Aluno {i}")

    while True:
        nota1 = float(input("Informe a primeira nota: "))
        if nota1 >= 0 and nota1 <= 10:
            break

    while True:
        nota2 = float(input("Informe a segunda nota: "))
        if nota2 >= 0 and nota2 <= 10:
            break

media = (nota1 + nota2) / 2
print(f"Média: {media:.1f}")
if media >= 7:
    print("Aprovado!")
    ap += 1
elif 3 <= media < 7:
    print("Recuperacao Final!")
    rc += 1
else:
    print("Reprovado!")
    rp += 1

print(" === PARONAMA GERAL === ")
