lunch = ('Hamburguer', 'Juice', 'Pizza', 'Pudim', 'Salada',)
#Tuples are immutable
print(lunch)
print(lunch[:2])
print(lunch[::2])
print(lunch[-3])

for food in lunch:
    print(f'I will eat {food}')
print('I ate a looot!!!!')