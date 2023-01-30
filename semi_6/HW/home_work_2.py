# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in -> 100
# out -> [20, 21, 40, 42, 60, 63, 80, 84, 100]
# in -> 424
# out -> [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]


def ask_for_positiv_number(s):
    num = int(input(s))
    if num <= 20:
        return -1
    else:
        return num

k = ask_for_positiv_number('Введите число N (> 20): ')
if k == -1:
    print("Некорректные входные данные")    
else:
    num_list = []
    num_list = [i for i in range(20, k+1) if i % 20 == 0 or i % 21 == 0]
    print(num_list)


