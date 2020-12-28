""" 28/12/2020 Database Connections
    chinook.db dosyasını kendi dizinimize taşıdık ve üzerinden işlemler yapacağız.
    select operasyonlarını function haline getirme ve insert operasyonları

"""
import sqlite3

def selectOperations():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""Select FirstName,LastName 
                                   from Customers where firstName like '%s'
                                   """)                               
    for row in cursor:
        print("First Name : "+row[0])
        print("Last Name : "+row[1])
        print('*****************')
        
    connection.close()

def insertCustomer():
    connection = sqlite3.connect('chinook.db')
    cursor = connection.execute("""
                                insert into customers(FirstName,LastName,Email) 
                                values('Melike','Eryılmaz','default@gmail.com')                                                      
                                """)
    # veriyi insert etmek için commit() etmeliyiz..
    connection.commit()
    connection.close()
    

    
    
selectOperations()
insertCustomer()
