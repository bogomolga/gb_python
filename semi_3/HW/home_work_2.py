# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in -> 4
# out -> [2, 5, 8, 10]
# [20, 40]
# in -> 5
# out -> [2, 2, 4, 8, 8]
# [16, 16, 4]

import random

n = int(input('Введите размер списка > 0: '))
my_list=[]
for _ in range(n):
    my_list.append(random.randint(0,10))
print(my_list)

my_list_new = []
L = len(my_list) - 1
for i in range(L):
    if i != L-i and i < L-i:
        my_list_new.append(my_list[i] * my_list[L-i])
    elif i == L-i and i > L-i:
        my_list_new.append(my_list[i] * my_list[i])
        break

print('Получили список c произведением пар чисел: ')
print(my_list_new)

