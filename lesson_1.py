# Типы данных
# int, float, boolean, str, list, None

value=None
a=123
b=1.23
print(type(a))
print(type(b))
print(type(value))

value=1234
print(type(value))

s='qwerty "hello world \nПривет'
print(s)
s='qwerty'

print(a,b,'---', s)
print('{} - {} - {}'.format(a,b,s)) #форматированный вывод
print(f'{a} - {b} - {s}') #интерполяция
print('{1} - {2} - {0}'.format(a,b,s)) #поменять местами вывод переменных по индексу

f=False
print(f)

list1 = [1, 2.55, '3', True] #лучше хранить в списке данные одного типа, а не разных
print(list1)

print('Введите a')
a1=int(input())
print('Введите b')
b1=float(input())
print(a1,'+',b1,'=',a1+b1)


#Логические операции

a2=1<4 and 5>2
print(a2) #true

b2='qwe'
c2='qwe'
print(b2 == c2) #true

d2=[1,2]
e2=[1,2]
print(d2 == e2) #true. сравниваем списки

func=1
T=4
x=123
print(func<T>x) #False. Тройные неравенства

f=1>2 or 4<6
print(f) #true.

f1=[1,2,3,4]
print(f)
print('2 in f1 : ', 2 in f1) #true. Потому что 2 содержится в списке f
print('not 2 in f1 : ', not 2 in f1) #False

is_odd = f1[0] % 2 == 0 #Проверка на четность - вариант 1
print('is_odd', is_odd) #False. 
is_odd = not f1[0] % 2 #Проверка на четность - вариант 2


if a1>b1:
    print ('max = ', a1)
else:
    print('max = ', b1)


username = input('Введите имя (Маша,Марина,Ильнар): ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)


original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print('inverted = ', inverted)


original1 = 23
inverted1 = 0
while original1 != 0:
    inverted1 = inverted1 * 10 + (original1 % 10)
    original1 //= 10
else:
    print('Пожалуй')
    print('хватит )')
print('inverted1 = ', inverted1)
# Пожалуй
# хватит )
# 32

for i in 1, -2, 3, 14, 5:
    print(i)
# 1
# -2
# 3
# 14
# 5

list2=[1, -2, 3, 14, 5]
for i in list2:
    print(i)

r=range(10)
print('range: ')
for i in r:      #от 0 до 9 ( for i in range(10) )
    print(i)

print('нечетные числа: ')
for i in range(1,10,2):  #нечетные числа
    print(i)  

for i in 'разбивка по буквам':  #разбивка строк по буквам
    print(i)


line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)


text = 'съешь ещё этих мягких французских булок'
print(text)
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #

help(text.istitle) # встроенная подсказка. что такое text.istitle

print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...


#СПИСКИ

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]

ran=range(1,6)
print(type(ran))        # <class 'range'>
numbers = list(ran)     # Приведение типа range к типу list !!!
print(type(numbers))    # <class 'list'>

print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

numbers.append(777) # добавить в конец
print('numbers : ', numbers) 
print(numbers == ['red', 'green', 'blue', '777']) # False
numbers.remove(2) #del numbers[0] # удалить элемент
print('numbers : ', numbers)  
del numbers[0]
print('numbers : ', numbers) 

#ФУНКЦИИ

#def f(x):
#    return x**2

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1  # <class 'str'>
arg = 2.3  # <class 'int'>
#arg = 2  # <class 'NoneType'>
print(f(arg))  # вызов функции f
print(type(f(arg))) # тип значения, которое возвращает функция f