# 3. Задайте список из n чисел, заполненный по формуле (1 + i/n) ** n и выведите на экран их сумму.
# in -> 6
# out -> [1.0, 2.522, 5.619, 11.391, 21.433, 37.971]
# 79.936

my_list = []
n = int(input('Введите длину списка > 0: '))
if n < 0:
    print('Некорректный ввод')
else:
    sum = 0
    for i in range(n):
        num = (1+(i/n))**n
        my_list.append(round(num, 3))
        sum = sum + my_list[i]
    print('Получили список: ')
    print(my_list)
    print(sum)
    
