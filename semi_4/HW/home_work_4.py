# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.
# in -> 9 5 3
# out in the file -> 
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in -> 0 -1 4
# out in the file ->
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

import random

def write_to_file(s):
    path = 'poly.txt'
    data = open(path, 'a', encoding="utf8") # 'a' - append, закрывает файл автоматически
    data.write(f"{s}\n")
    #data.close()

def ask_for_positiv_number(s):
    num = int(input(s))
    if num < 0:
        return -1
    else:
        return num

def create_mnogochlen(k):
    equation = {} # словарь
    for i in range(k, -1, -1): # от k до 0 с шагом -1 (по убыванию)
        equation[i] = random.randint(0,100) # для каждого ключа генерим рандомно значения
    #print(equation)
    eq_str = ''
    for k,v in equation.items():
        if k == 1:
            eq_str += f'{v}*x + '
        elif k == 0:
            eq_str += f'{v} + '
        else:
            eq_str += f'{v}*x^{k} + '
    else:
        eq_str = eq_str[:-3]
    eq_str += ' = 0'
    print("многочлен: ", eq_str)
    return eq_str

for i in range(3):
    k = ask_for_positiv_number('Введите максимальную степень > 0: ')
    if k == -1:
        print("Некорректные входные данные")
        break
    elif k == 0:
        print("многочлен: 0 = 0")
    else:
        write_to_file(create_mnogochlen(k))





    



