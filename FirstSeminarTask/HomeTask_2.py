# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите значение X: ')
x = int(input())
print('Введите значение Y: ')
y = int(input())
print('Введите значение Z: ')
z = int(input())

leftExpression = not (x or y or z)
rightExpression = not x and not y and not z
if leftExpression == rightExpression:
    print(True)
else:
    print(False)