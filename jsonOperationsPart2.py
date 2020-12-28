""" 27/12/2020 json Operations
    users.json dosyası içerisinden verileri okuyup ,json da farklı nodelara erişip ekrana yazdıran program.


"""

import json

with open('users.json') as users:
    data = json.load(users)
    # print(data)
    
    for x in range(3):
        print(data[x]["userId"])
        print(data[x]["title"])
        print(data[x]["adress"])
        print(data[x]["adress"]["street"])
        print(data[x]["adress"]["geo"]["lat"])
        
