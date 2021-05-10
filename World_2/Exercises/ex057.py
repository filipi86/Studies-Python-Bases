sexo = str(input('Informe o seu Sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MmfF':
    sexo = str(input('Dados invalidos. Por favor, informe seu Sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!!'.format(sexo))