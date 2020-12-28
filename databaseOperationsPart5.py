""" 28/12/2020 Database Connections
    chinook.db dosyasını kendi dizinimize taşıdık ve üzerinden işlemler yapacağız.
    like deyimi

"""
import sqlite3

connection = sqlite3.connect("chinook.db")


"""                            
    like deyimi içerisinde geçen anlamına gelmektedir.Belirli bir karakterle başlayan,biten,ya da içerisinde geçen 
    verileri bulmak için like deyimini kullanabiliriz.                          
"""
# FirstName inde a geçen müşterileri listelemek için
# cursor = connection.execute("""Select FirstName,LastName 
#                                from Customers where firstName like '%a%'
#                                """)
 # FirstName i w ile başlayan müşterileri listeleme
# cursor = connection.execute("""Select FirstName,LastName 
#                                from Customers where firstName like 'w%'
#                                """)
# FirstName i s ile biten müşterileri listeleme
cursor = connection.execute("""Select FirstName,LastName 
                               from Customers where firstName like '%s'
                               """)                               
for row in cursor:
    print("First Name : "+row[0])
    print("Last Name : "+row[1])
    print('*****************')
    
connection.close()
