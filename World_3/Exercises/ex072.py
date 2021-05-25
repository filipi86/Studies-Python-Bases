''' Tuples Exercicies 
    Translate Numbers'''

cont = ('zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
print('=+=' * 20)
while True:
    num = int(input('Press one number between 0 at 20: '))
    if 0 < num > 20:
        print('Try again. ', end='')
        continue
    if 0 <= num <= 20:
        print(f'You typed the number {cont[num]}')
        again = str(input('Do you want to continue? S/N: ')).strip().lower()[0]
        if again in 'Ss':
            continue
        if again in 'Nn':
            break
print(f'Program finished')
print('=+=' * 20)
