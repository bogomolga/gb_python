# 4. Напишите программу, которая будет принимать на вход дробь
#    и показывать первую цифру дробной части числа.
# 3.678 -> 6

print('Введите вещественное число n')
n=float(input())
print(int(n*10%10))