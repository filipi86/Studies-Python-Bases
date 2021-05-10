#n = 1
#while n != 0:
#    n = int(input('Digite um valor: '))
#print('FIM')
#r = 'S'
#while r == 'S':
#    n = int(input('Digite um Valor: '))
#    r = str(input('Quer Continuar? [S/N]')).upper()
#print('FIM')
n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um Numero: '))
    if n !=0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares!!!'.format(par, impar))