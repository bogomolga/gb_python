#3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in -> "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out -> {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

from itertools import groupby, chain
from operator import itemgetter

def get_string(s):
    value = input(s)
    if value.isdigit():
        print("Некорректные входные данные")
        return False
    else:
        v_list = []
        new_v_list = []
        v_list = list(value.split())
        for i in range(0, len(v_list)):
            if not v_list[i].isdigit():
                new_v_list.append(v_list[i])
    new_v_list = [list(grp) for _, grp in groupby(sorted(new_v_list), key=itemgetter(0))]
    return new_v_list

def create_dict(name_list):
    new_dict = {}
    for i in range(0, len(name_list)):
        #print(f'{i} = ', name_list[i])
        new_dict.update({name_list[i][0][0] : name_list[i]}) 
    return new_dict

name_list = get_string('Введите имена сотрудников через пробел: ')
print(name_list)
dict = {}
dict = create_dict(name_list)
print("Список имен по алфавиту:", dict)

#Введите имена сотрудников через пробел: маша саша паша сережа маша кирилл федя 
#[['кирилл'], ['маша', 'маша'], ['паша'], ['саша', 'сережа'], ['федя']]
#Список имен по алфавиту: {'к': ['кирилл'], 'м': ['маша', 'маша'], 'п': ['паша'], 'с': ['саша', 'сережа'], 'ф': ['федя']}