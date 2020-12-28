""" 28/12/2020 Database Connections
    chinook.db dosyasını kendi dizinimize taşıdık ve üzerinden işlemler yapacağız.

"""
import sqlite3

connection = sqlite3.connect("chinook.db")

""" Aşağıdaki sorguda  şehirlere göre gruplayarak en çok müşteri olan şehri ve müşteri sayısını buluyoruz.Azalan sırada getiriyoruz."""

"""                            
                              Select city,count(*) 
                               from Customers 
                               group by city
                               having count(*)>1
                               order by count(*) desc
"""

cursor = connection.execute("""Select city,count(*) 
                               from Customers 
                               group by city
                               having count(*)>1
                               order by count(*) desc
                               """)
for row in cursor:
    print("City : "+row[0])
    print("Count : "+str(row[1]))
    print('*****************')
    
# connection ı kapatıyoruz.
connection.close()
