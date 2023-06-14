total = 0
cont = 0
turmas = int(input('Insira a quantidade de turmas: '))
for c in range(1, turmas+1):
    alunos = int(input(f'Quantos alunos tem na {c}º turma? '))
    while alunos > 40:
        alunos = int(input(f'O maximo de alunos por turma é 40! Quantos alunos tem na {c}º turma? '))
    total = total + alunos
print(total)