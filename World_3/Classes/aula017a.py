num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print(f"I did't find the 4 number")
print(num)
print(f'This list has {len(num)} elements')