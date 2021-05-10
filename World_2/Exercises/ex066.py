soma = cont= 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A Soma dos valores foi {soma} e a quantidade de numeros digitados foi {cont}!!!')
print('ACABOU!!!')