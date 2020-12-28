""" 28/12/2020 Database Connections
    chinook.db dosyasını kendi dizinimize taşıdık ve üzerinden işlemler yapacağız.

"""
# Python da sqlite veritabanını kullanabilmek için sqlite3 modülünü import etmeliyiz.
import sqlite3

# sqlite3.connect() komutuyla database e bağlanıyoruz.
connection = sqlite3.connect("chinook.db")


# Göndereceğimiz sorguyu cursor ile connection.execute() ile yazar göndeririz.
# Burada istediğimiz sorguyu gönderebiliriz.
# cursor = connection.execute("Select * from Customers")
# cursor = connection.execute("Select FirstName,LastName from Customers")
cursor = connection.execute("Select FirstName,LastName from Customers where city='Prague'")
for row in cursor:
    print("First Name : "+row[0])
    print("Last Name : "+row[1])
    print('*****************')
    
# connection ı kapatıyoruz.
connection.close()
