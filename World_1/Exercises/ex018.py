import math
angulo = float(input('Digite o Angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('O Angulo de {} tem o SENO de {:.2f}!!'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O Angulo de {} tem o COSSENO de {:.2f}!!'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O Angulo de {} tem a TANGENTE de {:.2f}!!'.format(angulo, tangente))