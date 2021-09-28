values = []
for cont in range(0, 5):
    values.append(int(input('Typing a Value: ')))
for c,v in enumerate(values):
    print(f'In the position {c} found the value {v}!')
print(f'Arrived at the end of the list!!!')
print('=+=' * 15)
print (f'Creating list  * PS * - Ligation between list when you use " = "')
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'List A: {a}!')
print(f'List B: {b}!')
print('=+=' * 15)

#Results Printed
#=+==+==+==+==+==+==+==+==+==+==+==+==+==+==+=
#List A: [2, 3, 8, 7]!
#List B: [2, 3, 8, 7]!
#=+==+==+==+==+==+==+==+==+==+==+==+==+==+==+=

print(f'Creating list * PS * - Coping the List')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'List A: {a}!')
print(f'List B: {b}!')
print('=+=' * 15)

#Results Printed
#=+==+==+==+==+==+==+==+==+==+==+==+==+==+==+=
#List A: [2, 3, 4, 7]!
#List B: [2, 3, 8, 7]!
#=+==+==+==+==+==+==+==+==+==+==+==+==+==+==+=