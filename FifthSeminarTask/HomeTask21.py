# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


input_text = input('Введите текст: ')

search_symbol = 'абв'
lst = [i for i in input_text.split() if search_symbol not in i]
print(f'Текст после удаления абв : {" ".join(lst)}')
