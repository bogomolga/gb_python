# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 88 -> 1011000
# 11 -> 1011

n = int(input('Введите целое число > 0: '))
my_list = []
while n:    
    my_list.append(n % 2)
    n>>=1
my_list.reverse()
print(" ".join(map(str, my_list)).replace(" ", ""))
    

