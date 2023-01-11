# 5. Множества – Неупорядоченная совокупность элементов

# Пример 1:
a0 = {1, 2, 3, 5, 8}
b0 = {'2', '5', 8, 13, 21}
print(type(a0)) # set
print(type(b0)) # set


# Пример 2:
a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a)) # set
print(type(b)) # set
print(type(c)) # set
a = {1, 1, 1, 1, 1}
print(a) # {1}


# Пример 3:
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()


# Пример 4:
a1 = {1, 2, 3, 5, 8}
b1 = {2, 5, 8, 13, 21}
c1 = a1.copy() # c = {1, 2, 3, 5, 8}
print(c1)
u = a1.union(b1) # u = {1, 2, 3, 5, 8, 13, 21}
print(u)
i = a1.intersection(b1) # i = {8, 2, 5}
print(i)
dl = a1.difference(b1) # dl = {1, 3}
print(dl)
dr = b1.difference(a1) # dr = {13, 21}
print(dr)
q = a1 \
.union(b1) \
.difference(a1.intersection(b1))
print(q)
# {1, 21, 3, 13}


# Пример 5: Неизменяемое множество
a2 = {1, 2, 3, 5, 8}
b2 = frozenset(a2)
print(b2) # frozenset({1, 2, 3, 5, 8})