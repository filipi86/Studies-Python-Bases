print('=' * 30)
print('{:^30}'.format('BANCO FILIPI PIRES <3!'))
print('=' * 30)
valor = int(input('Que valor voce quer Sacar: R$ '))
total = valor
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= cedula
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedular de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('VOLTE SEMPRE AO BANCO FILIPI')
print('=' * 30)