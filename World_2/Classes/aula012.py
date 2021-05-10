nome = str(input('Qual eh seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome eh bem popular no Brasil!!')
elif nome in "Ana Claudia Juliana":
    print('Belo Nome Feminino')
else:
    print('Seu nome eh bem simples')
print('Tenha um Bom Dia {}!!'.format(nome))