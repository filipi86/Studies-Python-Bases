from datetime import date
atual = date.today().year
nascimento = int(input('Ano do nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.!!'.format(idade))
if idade <= 9:
    print('Classificacao: \033[33mMIRIM!!\033[m')
elif idade <= 14:
    print('Classificacao: \033[34mINFANTIL!!!\033[m')
elif idade <= 19:
    print('Classicacao: \033[35mJUNIOR!!!\033[m')
elif idade <= 25:
    print('Classificacao: \033[36mSENIOR!!!\033[m')
elif idade > 25:
    print('Classificacao: \033[32mMASTER!!!\033[m')
