# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in 5
# out [10, 2, 3, 8, 9]
# 22

# in 4
# out [4, 2, 4, 9]
# 8

import random

def sum_list(my_list: list, odd: bool): # odd=True = нечетные, False = четные
    sum = 0
    for i in range(len(my_list)):      
        if odd and i%2 == 0: 
            sum = sum + my_list[i]
        elif not odd and i%2 != 0:
            sum = sum + my_list[i]
    if odd:        
        print('Сумма нечетных элементов: ', sum)
    else:
        print('Сумма четных элементов: ', sum)

n = int(input('Введите размер списка > 0: '))

my_list=[]
for _ in range(n):
    my_list.append(random.randint(0,10))
print(my_list)

sum_list(my_list, True) # Считаем сумму нечетных элементов

