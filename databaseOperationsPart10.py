""" 28/12/2020 Database Connections
    chinook.db dosyasını kendi dizinimize taşıdık ve üzerinden işlemler yapacağız.
    select ,join,insert,update,delete operasyonları toplu halde eklenmiştir.

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

def joinOperations():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select 
                                    	albums.Title,artists.name
                                   from artists
                                   inner join albums on artists.ArtistId = albums.ArtistId
                                   """)                               
    for row in cursor:
        print("Title: "+row[0]+" "+"Name:"+row[1])
        
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

def updateCustomer():
    connection = sqlite3.connect('chinook.db')
    cursor = connection.execute("""
                                 Update Customers set city='Ankara' where city='Prague'                                                     
                                """)
    connection.commit()
    connection.close()
    

    
def deleteCustomer():
    connection = sqlite3.connect('chinook.db')
    cursor = connection.execute("""
                                 delete from Customers  where customerid=60                                                     
                                """)
    connection.commit()
    connection.close()
    
selectOperations()
joinOperations()
insertCustomer()
updateCustomer()
deleteCustomer()
