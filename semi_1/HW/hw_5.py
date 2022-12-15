# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#  https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099

import math
print('Введите x1: ')
x1 = int(input())
print('Введите y1: ')
y1 = int(input())
print('Введите x2: ')
x2 = int(input())
print('Введите y2: ')
y2 = int(input())

print('Расстояние между точками', round((math.sqrt((x2-x1)**2+(y2-y1)**2)), 4))
