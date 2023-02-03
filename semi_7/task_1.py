# Файлы

fluffy = open ('text_22.txt', 'r', encoding='utf8')
#print(fluffy.read().split('\n')) # разбиваем строки в файле на слова 

#print(fluffy.readline())

#print(fluffy.readlines()) # метод возвращает список строк

#for i in fluffy: # for при работе с файлами становится итератором, т.е. может вытягивать значения i - одна строка
#    print(i, end="") # end="" убирает пустые строки при выводе (убрали \n)

print(*[i for i in fluffy], sep="") # list comprehensions

fluffy.close()