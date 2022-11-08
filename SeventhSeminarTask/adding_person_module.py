

def input_person():
    filename = "Phone_book.csv"
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    gender = input('Введите пол: ')
    e_mail = input('Введите адрес электронной почты: ')
    phone_number = input('Введите номер телефона: ')
    new_contact = (
        f" {first_name} {last_name} {gender}  {e_mail} {phone_number}")
    myfile = open(filename, "a+")
    myfile.write(new_contact)
    print(f'Новый контакт {new_contact} добавлен в справочник')
    return 

