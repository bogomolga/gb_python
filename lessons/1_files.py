# 1. Работа с файлом. Файл создается в самой верхней папке ..\!Обучение GB\progs\
# Связать файловую переменную с файлом, определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# Пример 1:
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')


# Пример 2_1:
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)  # разделителей не будет
data.close()


# Пример 2_2:
path = 'file.txt'
data = open(path, 'r', encoding="utf8")
for line in data:
    print(line)
data.close()


# Пример 3:
n = open("text_343.txt", 'a', encoding="utf8")
print("Some text", file=n) # print может записывать данные в файл


# Пример 4:
path = 'test.txt'
data = open(path, 'r', encoding="utf8")
row_sum = 0
n = 0
for line in data:
    row_sum += 1
data.close()
data = open(path,'r', encoding="utf8")
s = data.read() 
n = s.count('a')
print("Количество элементов 'а' в файле :", n)
print("Количество строк в файле :", row_sum)
