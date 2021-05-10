salario = float(input('Qual eh o salario do Funcionario? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R$ \033[1;44m{:.2f}\033[m passa a ganhar R$ \033[1;44m{:.2f}\033[m agora.'.format(salario, novo))