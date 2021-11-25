import csv


def add_to_db(web:str,email:str,password:str):
        
    with open("./data.csv","a+",newline="") as ncsvFile:
        data =  (web,email,password)
        add_new = csv.writer(ncsvFile)
        add_new.writerow(data)
        



def search_from_db (query):
    with open("./data.csv","r",newline="") as ncsvFile:
        data = csv.reader(ncsvFile)
        for d in data:
            if d[0] == query :
                return d

        

 

    
    



