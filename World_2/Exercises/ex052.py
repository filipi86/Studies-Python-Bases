num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E Por isso ele eh \033[1;34mPRIMO!!!\033[m')
else:
    print('E por isso ele \033[1;35mNAO eh PRIMO!!\033[m')