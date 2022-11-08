from generator import employers_gen
from variables import filename
from search_employee import search_person,id_search
from adding_employee import input_person

def main_menu():
    
    print("БАЗА СОТРУДНИКОВ ПРЕДПРИЯТИЯ")
    print("Приступаем к работе, что вы хотите сделать?")
    print("Создать базу данных сотрудников  - нажмите 1 ")
    print("Посмотреть всю базу данных  - нажмите 2 ")
    print("Добавить новую запись  - нажмите 3 ")
    print("Поиск сотрудника - нажмите 4")
    print("Для поиска сотрудника по ID - нажмите 5")
    print("Закончить работу с базой - нажмите 6")
    
    choice_num = int(input("Введите № пункта меню: "))

    if choice_num == 1:
        employers_gen()
        main_menu()
    elif choice_num == 2:
        myfile = open(filename, "r+")
        filecontents = myfile.read()
        print(filecontents)
        main_menu()

    elif choice_num == 3:
        input_person()
        main_menu()

    elif choice_num == 4:
        search_person()
        main_menu()
    elif choice_num == 5:
        id_search()
        main_menu()
    if choice_num == 6:
        exit()
    else: 
        print("Неверное значение, попробуйте еще раз")
        main_menu()

    return
