#1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in -> Number of words: 10
# out -> авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in -> Number of words: 6
# out -> ваб вба абв ваб бва абв
# ваб вба ваб бва
# in -> Number of words: -1
# out -> The data is incorrect


import random
import re

def words_list (num, word="абв"):
    my_list=[]
    my_str=''
    for i in range(num):
        m=random.sample(word, k=3)
        my_list.append("".join(m))
        my_str = " ".join(my_list)
    print('Получили строку: ' + my_str)
    return my_list #my_str 

string_as_list = words_list(int(input('Введите количество слов: ')))
fragment = ['абв']
final_list = [word for word in string_as_list if word not in fragment]  # list comprehensions
final_string = ' '.join(final_list)
print("Удалили 'абв': " + final_string)


# Вариант 2:
#my_str = re.sub(r'абв+\s?', '', my_str).strip()
#print(my_str)

