from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opcoes sao:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual eh sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!!')
print('=+=' * 10)
print('O Computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador]))
print('=+=' * 10)
if computador == 0: # Computer play PEDRA
    if jogador == 0:
        print('\033[1;34mEMPATE!!!\033[m')
    elif jogador == 1:
        print('\033[1;35mJOGADOR VENCE!!\033[m')
    elif jogador == 2:
        print('\033[1;35mCOMPUTADOR VENCE!!\033[m')
    else:
        print('JOGADA INVALIDA!!')
elif computador == 1: #Computer play PAPEL
    if jogador == 0:
        print('\033[1;36mCOMPUTADOR VENCE!!\033[m')
    elif jogador == 1:
        print('\033[1;34mEMPATE!!!\033[m')
    elif jogador == 2:
        print('\033[1;35mJOGADOR VENCE!!\033[m')
    else:
        print('JOGADA INVALIDA!!')
elif computador == 2: #Computer play TESOURA
    if jogador == 0:
        print('\033[1;35mJOGADOR VENCE!!\033[m')
    elif jogador == 1:
        print('\033[1;36mCOMPUTADOR VENCE!!\033[m')  
    elif jogador == 2:
        print('\033[1;34mEMPATE!!!\033[m')
    else:
        print('JOGADA INVALIDA!!')