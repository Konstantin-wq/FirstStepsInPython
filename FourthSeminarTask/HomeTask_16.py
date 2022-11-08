#   Вычислить число c заданной точностью d
#     Пример:
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

from cmath import pi
import random

# Вариант для числа Пи

accuracy = int(input('Введите значение знаков числа Пи после запятой '))
str_pi = str(pi)
pi_number = []
for i in range(accuracy+2):
    pi_number.append(str(str_pi[i]))

output_str = ''
for i in pi_number:
    output_str += i
print(output_str)

# Вариант для случайно-сгенирированного числа

accuracy_second = input('Задайте точность:').count('0')
round_number = random.uniform(0, 10)
print(round_number)

print(f'число {round_number} с заданной точностью {accuracy_second} = {round(round_number, accuracy_second)} ')
