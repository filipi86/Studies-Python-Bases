frase = str(input('Digita uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#print('Voce digitou a frase {}'.format(junto))
inverso = ''
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} eh {}!!!'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palindromo!!')
else:
    print('A frase digitada nao eh um Palindromo')
#print(junto, inverso)