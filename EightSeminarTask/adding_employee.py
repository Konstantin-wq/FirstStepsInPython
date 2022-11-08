
from variables import filename
import csv


def input_person():

    id_employee = input("Введите ID")
    full_name = input("Введите имя и фамилию: ")
    gender = input('Введите пол: ')
    degree = input('Введите степень')
    education = input('Введите учебное заведение')
    e_mail = input('Введите адрес электронной почты: ')
    phone_number = input('Введите номер телефона: ')
    id_dept = input('Присвойте код отдела')
    new_contact = (
        f" {id_employee} {full_name} {gender} {e_mail} {phone_number}")
    print(new_contact)
    print('Если данные введены верно нажмите Y, в ином случае нажмите любую клавишу')
    answer = input()
    if answer == 'y':
        with open('EightSeminarTask\\Employers_data_base.csv', mode='a') as csvfile:
            file_writer = csv.writer(
                csvfile, delimiter=",", lineterminator="\r")
            file_writer.writerow(
                [id_employee,full_name, gender, degree, education, e_mail, phone_number, id_dept])
        csvfile.close()
    else:
        print('Ввод отменен')

    return
