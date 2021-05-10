from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Qual eh sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A Soma entre {} + {} eh {}!!!!'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} eh {} !!!!!'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valeu eh {} !!!!!'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe numeros novamente!!!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando....')
    else:
        print('Opcao Invalida. TENTE NOVAMENTE')
    print('==+==' * 7)
    sleep(2)
print('Fim do Programa!!! Volte sempre!!!')