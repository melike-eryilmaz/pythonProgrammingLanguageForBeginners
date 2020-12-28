""" 28/12/2020 Database Connections
    chinook.db dosyasını kendi dizinimize taşıdık ve üzerinden işlemler yapacağız.

"""
# Python da sqlite veritabanını kullanabilmek için sqlite3 modülünü import etmeliyiz.
import sqlite3

# sqlite3.connect() komutuyla database e bağlanıyoruz.
connection = sqlite3.connect("chinook.db")


# Göndereceğimiz sorguyu cursor ile connection.execute() ile yazar göndeririz.
# Veritabanından string ifadeler order by asc olarak default gelir.

# Aşağıdaki sorgu Prague da yaşayan ,FistName olarak artan sırada ,FistName aynıysa LastName e göre artan sırada database den verileri getirmemizi sağlar.
"""                            
                               Select FirstName,LastName 
                               from Customers where city='Prague'
                               order by FistName,LastName
"""

cursor = connection.execute("""Select FirstName,LastName 
                               from Customers where city='Prague'
                               order by FistName,LastName
                               """)
for row in cursor:
    print("First Name : "+row[0])
    print("Last Name : "+row[1])
    print('*****************')
    
# connection ı kapatıyoruz.
connection.close()
