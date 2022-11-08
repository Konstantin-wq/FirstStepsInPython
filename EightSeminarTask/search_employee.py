
from variables import filename
from Departments import departments_in_company
import csv

def search_person(): 
    search_data = input("Введите данные для поиска: ") 
    file = open(filename, "r+") 
    person_info = file.readlines() 
      
    found = False 
    for line in person_info: 
        if search_data in line: 
            print("По вашему найден сотрудник: ", end = " ") 
            print(line) 
            lst = line.split(',')
            dp = int(lst[-1])
            print('Место работы сотрудника: ' + departments_in_company.get(dp))
                 
            found = True             
            
    if found == False: 
        print(f"{search_data} в базе не обнаружен ") 
    
    return 


def id_search():
    id_emp = input('Введите ID сотрудника поиска')
    with open(filename, mode = 'r') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            if id_emp == row[0]:
                
                print(row)
    return

    

              