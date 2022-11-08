from adding_person_module import input_person
from search_person_module import search_person


def main_menu():
    file_name = 'Phone_book.csv'
    print("Приступаем к работе, что вы хотите сделать?")
    print("Посмотреть весь справочник  - нажмите 1 ")
    print("Добавить новую запись  - нажмите 2 ")
    print("Поиск по справочнику - нажмите 3")

    choice_num = int(input("Введите № пункта меню: "))

    if choice_num == 1:
        myfile = open(file_name, "r+")
        filecontents = myfile.read()
        print(filecontents)
        main_menu()

    elif choice_num == 2:
        input_person()
        main_menu()

    elif choice_num == 3:
        search_person()
        main_menu()

    return
