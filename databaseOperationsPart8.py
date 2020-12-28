""" 28/12/2020 Database Connections
    chinook.db dosyasını kendi dizinimize taşıdık ve üzerinden işlemler yapacağız.
    delete operasyonu

"""
import sqlite3

# customerid si 60 olan müşteiriyi silelim.
def deleteCustomer():
    connection = sqlite3.connect('chinook.db')
    cursor = connection.execute("""
                                 delete from Customers  where customerid=60                                                     
                                """)
    connection.commit()
    connection.close()
    
    

deleteCustomer()
