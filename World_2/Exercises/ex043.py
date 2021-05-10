peso = float(input('Qual eh seu peso? (Kg) '))
altura  = float(input('Qual eh sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa eh {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO do peso normal!!')
elif 18.5 <= imc < 25:
    print('Parabens voce esta delicinha!!')
elif 25 <= imc < 30:
    print('Voce esta com SOBREPESO')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE, Cuidado!!!')
elif imc >= 40:
    print('Voce esta com OBESIDADE MORBIDA..SE LIGA!!!')