# Реализуйте алгоритм перемешивания списка.

import random
listLength = int(input("Введите количество элементов списка "))
listNumbers = []
for i in range(listLength):
    i = random.randint(-100, 100)
    listNumbers.append(i)
print('{} {}'.format(
    'Исходный, случайным образом сгенерированный, список: \n ', listNumbers))
newRandomList = listNumbers
random.shuffle(newRandomList)
print('{} {}'.format('Перемешанный исходный список: \n', newRandomList))
    