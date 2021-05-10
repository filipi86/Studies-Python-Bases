casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do do comprador: R$ '))
anos = int(input('Quantos anos de Financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' A Prestacao sera de {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser APROVADO')
else:
    print('Emprestimo NEGADO')
