list = ('Pencil', 1.75, 'Rubber', 2, 'Notebook', 15.90, 'Backpack', 120.32, 'Pens', 22.30, 'Book', 34.90)
print('--' * 20)
print(f'{"PRICE LIST":^40}')
print('--' * 20)
for item in range(0, len(list)):
    if item % 2 == 0:
        print(f'{list[item]:.<30}', end='')
    else:
        print(f'R$ {list[item]:>7.2f}')
print('--' * 20)