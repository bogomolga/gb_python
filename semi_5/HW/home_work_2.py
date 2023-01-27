# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# https://fb.ru/article/369240/algoritm-rle-opisanie-osobennosti-pravila-i-primeryi
# in -> Enter the name of the file with the text: 'text_words.txt'
# Enter the file name to record: 'text_code_words.txt'
# Enter the name of the file to decode: 'text_code_words.txt'

# out in file -> 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

#import pathlib
#from os import path
from pathlib import Path
from itertools import groupby  

path = Path("semi_5", "HW", "text_words.txt") 
print(str(path))

try:
    my_abs_path = path.resolve(strict=True)
except FileNotFoundError:
    print('файла нет')  # doesn't exist
else:
    data = open(path,'r', encoding="utf8")
    s = data.read() 
    #n = s.count('a')
    print('Содержимое файла: ' + s)

"""     my_list = list(s)
    print(my_list)
    kolvo = 0
    for key, group in groupby(my_list, lambda x: x[0]):
        for thing in group:
             kolvo +=1
        print(kolvo + thing % (my_list[1], key))
        print() """

Относительный путь к файлу:
        gb_python\semi_5\HW\home_work_2.py

Файл text_words.txt лежит в этом же каталоге HW

Программа не находит файл:
PS C:\Users\Olga\Documents\!Обучение GB\progs> & C:/Users/Olga/AppData/Local/Microsoft/WindowsApps/python3.10.exe "c:/Users/Olga/Documents/!Обучение GB/progs/gb_python/semi_5/HW/home_work_2.py"
semi_5\HW\text_words.txt
файла нет

Несколько дней назад находила.
Устала! Не знаю как пути к файлам задавать так чтоб работало везде