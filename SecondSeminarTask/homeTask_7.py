#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

a = int(input('Введите число '))
listNumbers = []
multiplyNumber = 1
for i in range(1, a+1):
    multiplyNumber = multiplyNumber*i
    listNumbers.append(multiplyNumber) 
print('{} {}'.format('Искомая последовательность чисел: ' , listNumbers))

