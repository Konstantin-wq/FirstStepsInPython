# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
# Генерируем список
newRandomList = []
a = int(input('Введите размерность списка '))
for i in range(a):
    i = random.randint(-100, 100)
    newRandomList.append(i)
print(newRandomList)


def CountingPairs(inputList):
    multiplyNum = 0
    outputList = []
    for i in range(0, ((len(inputList)+1)//2)):
        multiplyNum = inputList[i]*(inputList[-i-1])
        outputList.append(multiplyNum)
    return outputList


print(CountingPairs(newRandomList))
