# 6. Списки – пронумерованная, изменяемая коллекция объектов одного типа

# Пример 1:
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]


# Пример 2:
colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент


#sample сам возвращает список
from random import sample
n3 = int(input())
x3 = sample(range(1, n3), k=(n3 - 1))
print("x3=", x3) # x3= [1, 3, 2]



my_list2 = [2,3,5,9,3]
count2 = 0
for i in range(1,len(my_list2),2):
    count2+= my_list2[i]
print("count2 = ", count2) # Сумма четных элементов в списке: 3+9=12

new_list = [my_list2[i] for i in range(len(my_list2)) if i%2] # Запись четных элементов в новый список
    #new_list = [my_list[i] for i in range(1, len(my_list), 2)] # можно так
print("new_list: ", new_list, sum(new_list)) # new_list:  [3, 9] 12


# фильтрация символов в строке
enter_list = input("Введите числа через пробел: ").split() # по пробелам разобьет строку на элементы списка    
right_list = []
for i in range(len(enter_list)):
	enter_list[i] = enter_list[i].strip(".!,;-")
	if enter_list[i].isdigit:
	    right_list.append(enter_list[i])
print(right_list)

splited = map(str,right_list)
print("splited: ", splited) # -> splited:  <map object at 0x00000264B56A3DF0>