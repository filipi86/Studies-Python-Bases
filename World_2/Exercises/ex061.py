print('GERADOR de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <=10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('ACABOU')