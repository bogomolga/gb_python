# 2. Напишите программу для проверки ложности утверждения (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат

# x y z w
# 0 1 0 1
# 1 1 0 0
# 1 1 1 0

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((w and z) or not y or not (x == w)):
                    print(x, y, z, w)



