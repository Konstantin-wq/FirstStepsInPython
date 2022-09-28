#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

a = int(input('Введите число:'))
listNumbers = []
for i in range(-a,a+1):
    listNumbers.append(i)
print(listNumbers)

x = int(input("Введите индекс первого элемента списка "))
y = int(input("Введите индекс второго элемента списка "))

if len(listNumbers) > x and len(listNumbers) > y:
    multiplyNumbers = listNumbers[x]*listNumbers[y]
    print(multiplyNumbers)
else:
    print('Заданных индексов в списке не существует')

summaryFile = open('task.txt','w')
summaryFile.write('List of elements: ')
summaryFile.write('\n')
for elem in listNumbers:
    summaryFile.write(str(elem))
    summaryFile.write('\n')
summaryFile.write('{} {}'.format('Multiply of chosen elementes' , str(multiplyNumbers)))    
summaryFile.close()


