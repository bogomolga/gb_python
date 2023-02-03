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



my_list2 = [2, 3, 5, 9, 3, 10, 22, 2, 26, 5, 44]
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



#Чтоб избежать Out of range, использовать надо  так:
my_list2 = [2, 3, 5, 9, 3, 10, 22, 2, 26, 5, 44]
my_list3 = [2, 3, 5, 9, 3, 10, 22, 2, 26, 5, 44]
my_list2 = [my_list2[x] for x in range(1, len(my_list2)) if my_list2[x] > my_list2[x-1]]
my_list3 = [my_list2[x] for x in range(0, len(my_list2) - 1) if my_list2[x] > my_list2[x+1]]
print("my_list2: ", my_list2)
print("my_list3: ", my_list3)



# Сортировка списка
my_list4 = [2, 3, 5, 9, 3, 10, 22, 2, 26, 5, 44]
dict_1 = {}
y = 0
for i in sorted(my_list4): # цикл по отсортированному списку
    y += 1
    dict_1.update({y : i}) # добавляем в словарь отсортированные элементы списка
my_list4 = sorted(my_list4) # сортируем список
print("my_list4: ", my_list4)
print("dict_1: ", dict_1)  