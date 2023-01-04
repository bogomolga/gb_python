# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях (не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

my_list = []
n = int(input('Введите целое число > 0: '))
p1 = int(input('Введите позицию 1 (> 0): '))
p2 = int(input('Введите позицию 2 (> 0): '))
if n < 0 or p1 < 0 or p2 < 0:
    print('Некорректный ввод')
else:
    for i in range(-n, n+1):
        my_list.append(i)
    print('Получили список: ')
    print(my_list)
    print(f'На позиции {p1}: ', my_list[p1-1])
    print(f'На позиции {p2}: ', my_list[p2-1])
    print('Произведение= ', my_list[p1-1]*my_list[p2-1])
