dias = int(input('Quantos dias voce utilizou o carro: '))
km = float(input('Quantos Km rodados? '))
pago = dias * 60 + (km * 0.15)
print('O total a pagar eh R$ {:.2f}.'.format(pago))