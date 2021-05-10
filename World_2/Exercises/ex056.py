somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('\033[1;33m -------- {} PESSOA --------\033[m'.format(p))
    nome = str(input('\033[1;32mNOME: \033[m')).strip()
    idade = int(input('\033[1;33mIdade: \033[m'))
    sexo = str(input('\033[1;34mSexo [M/F]: \033[m')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 +=1
mediaidade = somaidade / 4
print('A media de idade do grupo eh de {} anos'.format(mediaidade))
print('O Homem mais velho tem {} e se chama {} !!' .format(maioridadehomem, nomevelho))
print('Ao Todo sao {} mulheres com 20 anos'.format(totmulher20))