	# 1. Задайте строку из набора чисел. Напишите программу,
	#    которая покажет большее и меньшее число.
	#    В качестве символа-разделителя используйте пробел.
    # in -> 1,6. 8,9!-3 59
    # out -> min=1 max=59
    # in -> 7ц 5 у 0 каап rfgg34
    # out -> некорректные данные

def check(): # фильтрация символов в строке
	enter_list = input("Введите числа через пробел: ").split() # по пробелам разобьет строку на элементы списка    
	right_list = []
	for i in range(len(enter_list)):
	    enter_list[i] = enter_list[i].strip(".!,;-")
	    if enter_list[i].isdigit:
	        right_list.append(enter_list[i])
	print(right_list)
	return right_list

def max_min_finder(any_list): # возвращает кортеж: ('6', '4')
    if any_list: # Если список не пустой то выполняем:
        return max(any_list, key=int), min(any_list, key=int) # параметр key=int говорит: воспринимай элемент как целочисленный!
    return [] # возвращаем пустой список чтоб не было None в ответ на пустой список

#my_list = input("Введите числа через пробел: ").split()
#print(my_list)

print(*max_min_finder(check())) # * - распаковка: 6 4. Без * не будет распаковки: ('6', '4')






