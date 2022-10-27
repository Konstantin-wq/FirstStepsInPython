filename = 'NinethSeminarTaskP2\\Employers_data_base_new.csv'
import csv 

def search_by_id(input_id):
    id_emp = input_id
    data = csv.reader(open(filename,encoding='utf-8'))
    for row in data:
        if str(id_emp) in row[0]:
            searched_row = " ".join(row)+'\n'
             
    return(searched_row)



