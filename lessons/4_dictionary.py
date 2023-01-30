# 4. Словари – Неупорядоченные коллекции произвольных объектов с доступом по ключу

# Пример 1:
dictionary = {}
dictionary = \
{
'up': '↑',
'left': '←',
'down': '↓',
'right': '→'
}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться


# Пример 2:
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
    # up: ↑
    # down: ↓
    # right: →

# Пример 3:
new_dict = {}
for z in range(1, 21):
    new_dict = {z : z**2 }
    y = z + 1
    new_dict.update({y : y**2})

print(new_dict)
#На выходе получается:
#{20: 400, 21: 441}


#Дан словарь, удалите из него все элементы со значениями None. Например:
a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} # -> {'b': 1, 'c': 2, 'e': 3}
a = {i: j for i, j in a.items() if j!=None }
print("dict a= ", a)

#2й вариант удаления:
b = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
for j in b.copy():
    if b[j] == None:
        b.pop(j)
print("dict b= ", b) # -> {'b': 1, 'c': 2, 'e': 3}

val = b.values()
print(val) # -> dict_values([1, 2, 3])
print(type(val)) # -> <class 'dict_values'>