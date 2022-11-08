# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from itertools import count
import random


a_length = int(input('Введите длину последовательности '))
rand_lst_sequence = []
for i in range(a_length):
    i = random.randint(1, 10)
    rand_lst_sequence.append(i)
print(rand_lst_sequence)

uniqe_sequence = []
for i in rand_lst_sequence:
    num = rand_lst_sequence.count(i)
    if num == 1:
        uniqe_sequence.append(i)
    else:
        continue
if uniqe_sequence == []:
    print('Уникальных элементов нет')
else:
    print(uniqe_sequence)


# uniqe_sequence = []
# for num in rand_lst_sequence:
#     if num not in uniqe_sequence:
#         uniqe_sequence.append(num)
# print(uniqe_sequence)
