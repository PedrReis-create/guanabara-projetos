import random
lista_alunos = []
    
for i in range(4):
    aluno = input('Digite o nome do aluno :')
    lista_alunos.append(aluno)
    
escolhido = (random.choice(lista_alunos))
print(f'O aluno escolhido para apagar o quadro foi {escolhido}!')

