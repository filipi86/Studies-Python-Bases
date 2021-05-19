lunch = ('Hamburguer', 'Juice', 'Pizza', 'Pudim', 'Salada',)

for cont in range(0, len(lunch)):
    print(f'I will eat {lunch[cont]} in position {cont}')
print('I ate a looot!!!!\n')

for food in lunch:
    print(f'I will eat {food}')
print('I ate a looot!!!!\n')

for pos, food in enumerate(lunch):
    print(f'I will eat {food} in position {pos}')
print('I ate a loot!!!\n')

print('END Program')

