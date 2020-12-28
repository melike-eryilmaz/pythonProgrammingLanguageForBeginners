""" 28/12/2020 Database Connections
    chinook.db dosyasını kendi dizinimize taşıdık ve üzerinden işlemler yapacağız.
    join operasyonu

"""

import sqlite3

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

joinOperations()
