# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
# Генерируем список
newRandomList = []
a = int(input('Введите размерность списка '))
for i in range(a):
    i = round(random.uniform(0, 2), 2)
    newRandomList.append(i)

print(newRandomList)

# Находим дробные части и вычисляем разницу между max и min


def CountingFractionalPart(inputList):
    fractionalPart = 0
    FractionalPartList = []
    for i in range(len(inputList)):
        fractionalPart = inputList[i] % 1
        FractionalPartList.append(fractionalPart)
    print('{} {}' .format('Список из дробных частей: \n', FractionalPartList))
    diff = round((max(FractionalPartList) - min(FractionalPartList)), 2)
    return diff


print('{} {}' .format('Разница между максимальным и минимальным значением: \n',
      CountingFractionalPart(newRandomList)))
