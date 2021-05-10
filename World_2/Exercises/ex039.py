from datetime import date
atual = date.today().year
nome = str(input('Qual seu  nome: '))
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('''Meu sexo eh: 
[ 1 ] Homem 
[ 2 ] Mulher
[ 3 ] Nao informar''')
Opcao = str(input('Sua opcao: '))
if Opcao == 1:
    print('Quem nasceu em {} ten {} anos em {}'.format(nascimento, idade, atual))
    if idade == 18:
        print('Voce tem que se alistar IMEDIATAMENTE!!')
    elif idade < 18:
        saldo = 18 - idade
        print('Voce ainda nao tem 18 anos!!. Ainda faltam {} anos para o alistamento!'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento sera em {}!!'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Voce ja deveria ter se alistado a {} anos!!.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamente foi em {}'.format(ano))
elif Opcao == 2:
    print('Voce nao precisa realizar o ALISTAMENTO!!')
elif Opcao ==3:
    print ('Infelizmente nao conseguindo confirmar se voce pode ou nao se alistar!!!')