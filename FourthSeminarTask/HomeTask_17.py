# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


num = int(input('Введите натуральное число '))
list_of_numbers = []

for i in range(2, num + 1):
    if num % i == 0:
        count = 1
        for j in range(2, (i//2 + 1)):
            if (i % j == 0):
                count = 0
                break
        if (count == 1):
            list_of_numbers.append(i)
print(list_of_numbers)
