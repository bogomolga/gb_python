#  2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.


import os
clear = lambda: os.system('cls')
clear()

from random import sample

def words_list (num, word="adc"):
    new_list=[]
    for i in range(num):
        m=sample(word, k=3)
        new_list.append("".join(m))
    return new_list

def find_second (n_list, word):
    if word in n_list and n_list.count(word) > 1:
        c = n_list.index(word)
        print(n_list.index(word, c+1))
    else:
        print(-1)


u = words_list(int(input('Введите количество слов: ')))
print(u)

find_second(u, input('Введите слово: '))






