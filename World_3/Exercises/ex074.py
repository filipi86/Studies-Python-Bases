import builtins
from random import randint
number = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('The numbers drews it was: ', end='')
for n in number:
    print(f'{n} ', end='')
print(f'\nThe major number drew it was {max(number)}')
print(f'The minor number drew it was {min(number)}')
