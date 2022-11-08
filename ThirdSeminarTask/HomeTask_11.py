# Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random
#Генерируем случайный список заданной размерности
newRandomList = []
a = int(input('Введите размерность списка '))
for i in range(a):
    i = random.randint(-100, 100)
    newRandomList.append(i)
print(newRandomList)

#Считаем элементы на нечетных индексах
def SumOfElements(lst):
    sum = 0
    for i in range(1, len(lst), 2):
        sum += lst[i]
    return sum


print(SumOfElements(newRandomList))
