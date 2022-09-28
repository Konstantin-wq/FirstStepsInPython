#3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
#Пример:
#1 -> 2.0
#2 -> 4.25
#3 -> 6.62037037037037

a = int(input('Введите число: '))
sum = 0
listNumbers = []
for i in range(1, a+1):
    a = (1 + 1/i)**i
    sum = sum + a
    listNumbers.append(a)
print('{} {} '.format('Список из чисел:', listNumbers))
print('{} {}'.format('Сумма чисел последовательности:',sum))
