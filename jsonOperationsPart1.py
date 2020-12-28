""" 28/12/2020 json 

    Veri sistemleri içerisinde verilerin konuşabilmesi için belirlenen formatlar vardır.xml,json gibi.
    JSON (JavaScript Object Notation – JavaScript Nesne Notasyonu) 
    insanlar için okunabilir olan bilgi saklama ve alışveriş formatıdır. 
    Bir JSON dosyası sadece metin kapsar ve .json uzantısını kullanır.

"""

import json

# string den json oluşturmqk için ..
stringData = '{"firstName" : "ece","lastName" :"eren"}'

jsonData = json.loads(stringData)

# print(type(jsonData))

print(jsonData["firstName"])
print(jsonData["lastName"])


# Dictionary den json oluşturmak için..
Users =  {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": "false"
  }

userJson = json.dumps(Users)

# print(type(userJson))

print(json.dumps("ece"))
