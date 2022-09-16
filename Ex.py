nota_aluno = input(" informe a nota: ")
nota_aluno = float(nota_aluno)

if nota_aluno >= 9 and nota_aluno <= 10:
    print("parabens voce tem o conceito maximo... A+")
elif nota_aluno >= 7 and nota_aluno <= 8.9:

    print("parabens. Conceito A")
elif nota_aluno >= 6 and nota_aluno <= 6.9:

    print("passou, mas deve estudar mais. Conceito B")
elif nota_aluno >= 4 and nota_aluno <= 5.9:

    print("Reprovado Conceito C")
elif nota_aluno >= 0 and nota_aluno <= 3.9:
    print("Reprovado Conceito D")
else:
    print("O numero que você digito não esta no intervalo de nota de 0 a 10....por favor digite uma nota valida.")

