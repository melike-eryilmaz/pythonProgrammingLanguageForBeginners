""" 28/12/2020 Database Connections
    chinook.db dosyasını kendi dizinimize taşıdık ve üzerinden işlemler yapacağız.
    update operasyonu

"""
import sqlite3

# Şehri Prague olan customerların şehrini Ankara olarak güncelleme.
def updateCustomer():
    connection = sqlite3.connect('chinook.db')
    cursor = connection.execute("""
                                 Update Customers set city='Ankara' where city='Prague'                                                     
                                """)
    connection.commit()
    connection.close()
    
    

updateCustomer()
