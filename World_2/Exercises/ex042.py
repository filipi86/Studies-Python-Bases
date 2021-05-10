r1 = float(input('\033[1;30mPrimeiro Segmento: \033[m'))
r2 = float(input('\033[1;31mSegundo Segmento: \033[m'))
r3 = float(input('\033[1;32mTerceiro Segmento: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima \033[1;33mPODEM FORMAR TRIANGULO \033[m', end='')
    if r1 == r2 == r3:
        print('\033[1mEQUILATERO!!\033[m')
    elif r1 != r2 != r3 !=r1:
        print('\033[1mESCALENO!!\033[m')
    else:
        print('\033[1mISOSCELES\033[m')
else:
    print('Os Segmentos acima \033[1;34mNAO PODEM FORMAR TRIANGULO!!!\033[m')