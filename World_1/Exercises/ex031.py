distancia = float(input('Qual eh a distancia da sua viagem? '))
print('Voce esta prester a comecar uma viagem de {}Km.'.format(distancia))
'''if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45'''
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o Preco da sua passagem ser de R${:.2f}'.format(preco))