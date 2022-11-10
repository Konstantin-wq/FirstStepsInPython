
import os


def first_polynom_input(nums=[]):

    elems_of_polynom = []
    num_count = len(nums)-1

    for coef in nums:
        if coef:
            coef = coef if num_count == 0 else '' if coef == 1 else coef
            degree = 'x' if num_count == 1 else '' if num_count == 0 else f'x^{num_count}'
            term = f'{coef}{degree}'
            elems_of_polynom.append(term)
        num_count = num_count-1
    first_equation = ' + '.join(elems_of_polynom) + ' = 0'
    print(first_equation)
    file_result = open('TenthSeminarTask\\polinom1.txt', 'w', encoding='utf8')
    file_result.write(first_equation)
    file_result.write('\n')
    file_result.close()

    return


def second_polynom_input(nums=[]):

    elems_of_polynom = []
    num_count = len(nums)-1

    for coef in nums:
        if coef:
            coef = coef if num_count == 0 else '' if coef == 1 else coef
            degree = 'x' if num_count == 1 else '' if num_count == 0 else f'x^{num_count}'
            term = f'{coef}{degree}'
            elems_of_polynom.append(term)
        num_count = num_count-1
    second_equation = ' + '.join(elems_of_polynom) + ' = 0'
    print(second_equation)
    file_result = open('TenthSeminarTask\\polinom2.txt', 'w', encoding='utf8')
    file_result.write(second_equation)
    file_result.close()

    return
