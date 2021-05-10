n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.2f} e {:.2f}, a media do aluno eh {:.2f} !!'.format(n1, n2, media))
if media < 5.0:
    print('O Aluno esta \033[32mREPROVADO!!!\033[m')
elif media >= 5 and media < 7:
    print('O Aluno esta em \033[34mRECUPERACAO!!!!\033[m')
#elif 7 > media >= 5:
    #print('O Aluno esta em \033[34mRECUPERACAO!!!\033[m')
elif media >= 7:
    print('O Aluno esta \033[35mAPROVADO!!!\033[m')
else:
    print('Final do Programa')
