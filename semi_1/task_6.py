# 6. Пример проверки ложности утверждения (x ≡ z ) ∨ (x → (y ∧ z))

# x y z
# 1 0 0
# 1 1 0

print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x==z or x <=y and z):
                print(x,y,z)