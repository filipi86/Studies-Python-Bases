number = (int(input('Type the number: '))),(int(input('Type other number: '))),(int(input('Type another number: '))),(int(input('Type the last number: ')))
print(f'You typed the value {number}')
print(f'The value 9 appers {number.count(9)} times')
if 3 in number:
    print(f'The value 3 appers {number.index(3)+1} position')
else:
    print(f'The value 3 did not appers in any position!')
print(f'The values pairs typed were: ', end='')
for n in number:
    if n % 2 == 0:
        print(n, end=' ')
print(f'\nThe program finished')
