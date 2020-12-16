#12/12/2020 substring() fonksiyonu

#Python da string ifadeler string dizi olarak tutulur .Yani indisleri vererek string dizi içerisindeki karakterlere veya karakter dizisine erişebiliriz.

message = 'Hello World'

print(message[1])

#Substring metodu string dizisini ayrıma işlemini gerçekleştirir.
#İndis değerlerini aralık olarak verebiliriz.Sadece o aradaki string ifadeyi döndürür.
newMessage = message[2:5]
print(newMessage)

print(message[:4])#Başlangıç değerini vermez isek en baştan verilen indise kadar alır.
print(message[2:])#Bitiş değerini vermezsek verilen indisten en son değere kadar alır.
