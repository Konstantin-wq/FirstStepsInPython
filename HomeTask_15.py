# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]




k = int(input('Введите коэффициент: '))

def FibonacciNumbers(x):
    fibonacciLst = []
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        firstNumber = 1
        secondNumber = 1
        nextNumber = 0
        for i in range(x):
            fibonacciLst.append(firstNumber)
            nextNumber = firstNumber + secondNumber
            firstNumber = secondNumber
            secondNumber = nextNumber
        firstNumber = 0
        secondNumber = 1
        for i in range(x+1):
            fibonacciLst.insert(0, firstNumber)
            nextNumber = firstNumber - secondNumber
            firstNumber = secondNumber
            secondNumber = nextNumber

        return fibonacciLst


print(FibonacciNumbers(k))

