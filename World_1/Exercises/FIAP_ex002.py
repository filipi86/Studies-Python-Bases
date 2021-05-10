nome="Filipi Pires"
empresa='FIAP'
qtde_funcionarios=500
mediaMensalidade=856.50
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

nome = str(input('Qual eh seu nome? '))
empresa = str(input('Qual empresa voce trabalha? '))
qtde_funcionarios = float(input('Quando funcionarios a empresa possui? '))
mediaMensalidade = float(input('Qual a media de valores? '))
print('{} trabalha na empresa {} que possui {:.2f} funcionarios e tem o valor medio de {}!!!.'.format(nome, empresa, qtde_funcionarios, mediaMensalidade))