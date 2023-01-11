# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности в том же порядке.
# in -> 7
# out -> [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in -> 
# -1 
# out -> Negative value of the number of numbers!
# []
# in -> 10
# out -> [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

import random

n = int(input('Введите количество чисел в последовательности > 0: '))
my_list = []
temp = []

if n <= 0:
    print("Некорректный ввод")
else:
    for _ in range(n):
        my_list.append(random.randint(0, 9))
    print(my_list)

    for i in my_list:
        if i not in temp:
            temp.append(i)
    my_list = temp
    print(my_list)  # Отсортированный список


