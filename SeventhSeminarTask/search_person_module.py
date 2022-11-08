
def search_person(): 
    filename = "Phone_book.csv"
    search_data = input("Введите данные для поиска: ") 
    file = open(filename, "r+") 
    person_info = file.readlines() 
      
    found = False 
    for line in person_info: 
        if search_data in line: 
            print("По вашему запросу найден контакт: ", end = " ") 
            print(line) 
            found = True 
            
    if found == False: 
        print(f"{search_data} в справочнике не обнаружен ") 
    
    return 
 