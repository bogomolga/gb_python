# 3. Напишите программу, которая будет на вход принимать
#    число N и выводить числа от -N до N


print('Введите n')
n=int(input())

print(*range(-n,n+1), sep=", ") # * оператор распаковки