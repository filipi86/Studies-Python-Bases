#a = 3
#b = 5
#print('Os valores sao \033[1;32;46m{}\033[m e \033[1;31;46m{}\033[m!!!'.format(a, b))

nome = 'Guanabara'
cores = {'limpa':'\033[m', 'azul':'\033[32m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;40m'}
print('Ola, Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))


