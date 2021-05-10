from random import randint
computador = randint(0, 1)
print('Sou seu Computador...Acabei de pensar em um numero entre 0 e 10!!')
print('Sera que voce consegue avinhar qual foi??? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual eh o seu Palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS..tente um numero maiior...')
        elif jogador > computador:
            print('Menos...Tente um numero menor..')
if palpites == 1:
    print('CARAMBA, VOCE acertou de PRIMEIRA!!!')
else:
    print('ACERTOU com {} Tentativas. PARABENS!!!'.format(palpites))