import code
from encodings import utf_8
import mimesis
from mimesis import Person
from mimesis import locales
import random
import csv


def employers_gen():
    
    amount_of_persons = int(
        input("Введите количество записей, которые вы хотите получить в справочнике: "))

    filename = "EightSeminarTask\\Employers_data_base.csv"    
    file = open(filename, "a+")
    file.close

    with open('EightSeminarTask\\Employers_data_base.csv', mode = 'w', encoding='utf-8') as csvfile:
        file_writer = csv.writer(csvfile, delimiter = ",", lineterminator="\r")
        file_writer.writerow(["ID сотрудника\t", "Имя\t", "Пол\t", "Степень\t" , "Образование\t", "Email\t", "Телефон\t", "ID отдела\t"])
        file.close
            
    id_increment = 0
    pers = Person('ru')
    employers_string = ''
    GenderList = ['MALE', 'FEMALE']
    for i in range(amount_of_persons):
        id_increment+=1
        if random.choice(GenderList) == 'MALE':
            GenRandom = mimesis.enums.Gender.MALE
            Gender = 'Мужской'
        else:
            GenRandom = mimesis.enums.Gender.FEMALE
            Gender = 'Женский'

        name = pers.full_name(GenRandom)
        degree = pers.academic_degree()
        education = pers.university()
        email = pers.email(
            domains=['mail.ru', 'yandex.ru', 'list.ru', 'gmail.com', 'bk.ru'])
        phone = pers.telephone(mask='+7(9##)#######')
        department_id = random.randint(1, 9)

        employers_string = f'{id_increment}, {name}, {Gender}, {degree}, {education}, {email}, {phone}, {department_id} \n'
        print(employers_string)
        with open('EightSeminarTask\\Employers_data_base.csv', mode = 'a',encoding='utf-8') as csvfile:
            file_writer = csv.writer(csvfile, delimiter = ",", lineterminator="\r")
            file_writer.writerow([id_increment,name, Gender, degree, education, email, phone, department_id])
            
               
       

        csvfile.close()

    return



