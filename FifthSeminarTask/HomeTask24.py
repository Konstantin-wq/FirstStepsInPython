#Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import count
from unicodedata import digit


with open('inputRLE', 'w') as data:
    data.write('WJHKKKLSSSSSOPPPPPNNNNNBMMMMMMAAAAADDDDDWQWWWWWQQQQQQLLLLLL')


with open('inputRLE', 'r') as data:
    str_input = data.readline()
print(str_input)
data.close()

def code_RLE(input_str):
    code_str = ''
    i = 0
    while i < len(input_str):
        count = 1
        while i + 1 <len(input_str) and input_str[i] == input_str[i+1]:
            count = count+1
            i = i + 1 
        code_str = code_str + str(count) + input_str[i]
        i = i + 1
    return code_str

def decode_RLE(coded_string):
    decode_string = ''
    count = ''
    i = 0
    while i < len(coded_string):
        if coded_string[i].isdigit():
            count = count + coded_string[i]            
        else:
            decode_string = decode_string + coded_string[i]*int(count)
            count = ''
        i = i+1
    return decode_string





with open('inputRLE', 'r') as data:
    str_input = data.readline()
print(f'Начальная строка: \n{str_input}\n')
data.close()
coded_string = code_RLE(str_input)
print(f'Закодированная строка:\n{coded_string}\n')

decoded_string = decode_RLE(coded_string)
print(f'Декодированная строка: \n{decoded_string}\n')

outputRLE = open('outputRLE.txt', 'w')
outputRLE.write(decoded_string)
outputRLE.close()
