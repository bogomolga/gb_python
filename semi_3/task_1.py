# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

# import random
from random import sample

# Функция может быть написана только сверху!
def find_number (amount, user_number):
    new_list = sample(range(1, (amount+1)*2), k=amount) # умножаем на 2 от балды, чтоб были двузначные числа. можно не умножать
    print(new_list)                                     # k отвечает сколько мы возьмем из последовательности
    if user_number in new_list:
        return 'yes'
    return 'no'

res = find_number(int(input('Введите длину списка > 0 (amount): ')),
                  int(input('Введите искомое число (user_number): ')))
print(res)






