#nome = str(input('Qual eh seu nome? '))
#print('Prazer em te Conhecer {:=^20}!!!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A some vale {},\no multiplicacao eh {} \ne a divisao eh {:.3f}'.format(s, m, d))
print('Divisao inteira {}\ne a Potencia {}'.format(di, e))