from random import randint
from time import sleep
computador = randint(0, 5) #make computer thinking
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente Adivinhas...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) #player try sucess
print('PROCESSANDO..')
sleep(1)
if jogador == computador:
    print('Parabens Voce conseguiu me vencer')
else:
    print('GANHEI, eu pensei no numero {} e nao no {}!'.format(computador, jogador))

