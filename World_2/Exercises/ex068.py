from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()
    print(f'Voce jogou {jogador} e o Computador {computador}. Total deu {total} ', end='')
    print('e DEU PAR' if total % 2 == 0 else 'e DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU !!')
            v +=1
        else:
            print('Voce PERDEU !!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!!!')
            v += 1
        else:
            print('Voce PERDEU!!!!')
            break
    print('Vamos Jogar novamente')
print(f'GAME OVER - Voce venceu {v} vezes...')
print('PROGRAMA ACABOU!!')