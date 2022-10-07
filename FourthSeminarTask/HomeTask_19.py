# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import os

k = int(input('Введите степень: '))
coefficient_list = []
for i in range(k+1):
    i = random.randint(0, 100)
    coefficient_list.append(i)
print(coefficient_list)

elems_of_polynom = []

for coef in coefficient_list:
    if coef:
        coef = coef if k == 0 else '' if coef == 1 else coef
        degree = 'x' if k == 1 else '' if k == 0 else f'x^{k}'
        term = f'{coef}{degree}'
        elems_of_polynom.append(term)
    k = k-1

final_equation = ' + '.join(elems_of_polynom) + ' = 0'
print(final_equation)

result_dir = 'files'
if not os.path.exists(result_dir):
    os.mkdir(result_dir)

with open(f'{result_dir}\\{"_".join(map(str, coefficient_list))}.txt', 'w', encoding='utf8') as file:
    file.write(final_equation)
