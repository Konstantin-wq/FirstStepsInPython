import mimesis
from mimesis import Person
from mimesis import locales
import random

def create_phone_book():
    print("ТЕЛФОННЫЙ СПРАВОЧНИК ИЗ СЛУЧАЙНО СГЕНЕРИРОВАННЫХ ПЕРСОН")
    print("Перед началом работы необходимо создать справочник")
    amount_of_persons = int(
        input("Введите количество записей, которые вы хотите получить в справочнике: "))



    filename = "Phone_book.csv"
    file = open(filename, "a+")
    file.close

    pers = Person('ru')
    phone_book_string = ''
    GenderList = ['MALE', 'FEMALE']
    for i in range(amount_of_persons):
        if random.choice(GenderList) == 'MALE':
            GenRandom = mimesis.enums.Gender.MALE
            Gender = 'Мужской'
        else:
            GenRandom = mimesis.enums.Gender.FEMALE
            Gender = 'Женский'

        name = pers.full_name(GenRandom)
        email = pers.email(domains=['mail.ru', 'yandex.ru', 'list.ru', 'gmail.com','bk.ru'])
        phone = pers.telephone(mask='+7(9##)#######')

        phone_book_string = f'{name} {Gender} {email} {phone} \n'
        print(phone_book_string)
        file = open(filename, "a+")
        file.write(phone_book_string)

    
        file.close()
    
    return


