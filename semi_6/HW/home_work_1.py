# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in -> 9
# out -> [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in -> 10
# out -> [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample

def ask_for_positiv_number(s):
    num = int(input(s))
    if num <= 1:
        return -1
    else:
        return num

k = ask_for_positiv_number('Введите длину списка N (> 1): ')
if k == -1:
    print("Некорректные входные данные")    
else:
    num_list = []
    num_list = sample(range(1, 29), k=k)
    print(num_list)
    num_list = [num_list[x] for x in range(1, len(num_list)) if num_list[x] > num_list[x-1]]
    print(num_list)



