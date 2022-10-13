# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, 
# список повторяемых и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

from enum import unique
import random

numbers_in_list = int(input('Введите размерность списка: '))
input_list = []
for i in range(numbers_in_list):
    i = random.randint(1,10)
    input_list.append(i)
print(f'Выводим случайный список \n{input_list}')

#Последовательность без повторов
clean_sequence = []
[clean_sequence.append(i) for i in input_list if i not in clean_sequence]
print(f'Выводим последовательность элементов без повторов:\n{clean_sequence}') 

#Последовательнрость из повторяющихся элементов
doubled_numbers = []
[doubled_numbers.append(i) for i in input_list if input_list.count(i)>1 and i not in doubled_numbers]
print(f'Выводим повторяющиеся элементы:\n{doubled_numbers}')

#Последовательность уникальных элементов без повторов
unique_numbers = []
[unique_numbers.append(i) for i in input_list if input_list.count(i)==1]
print(f'Выводим уникальные элементы:\n{unique_numbers}')