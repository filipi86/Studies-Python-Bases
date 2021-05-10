salario = float(input('Qual eh o salario do Funcionario? R$ '))
novo = salario + (salario * 15 / 100)
print('Um Funcionario que ganhava R$ {:.2f}, com 15% de aumento, para a receber R$ {:.2f}.'.format(salario, novo))