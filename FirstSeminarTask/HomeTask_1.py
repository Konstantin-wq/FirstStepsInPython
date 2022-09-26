#Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

print("Введите номер дня недели:")
a = int(input())

DaysOfWeek = {1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6:'Saturday', 7:'Sunday' }
if a in DaysOfWeek:
    if a == 7 or a == 6:
        print('Выходной день ' + DaysOfWeek[a])
    else:
        print ('Рабочий день ' + DaysOfWeek[a])
else:
    print('Вы ввели неверное число')