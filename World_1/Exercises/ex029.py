velocidade = float(input('Qual eh a velocidade do Carro? '))
if velocidade > 80:
    print('MULTADO !!! Voce excedeu o limite que eh de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com Seguranca!')
