# 22/12/2020 for iteration example

# Girilen sayının asal sayı olup olmadığını belirten program kodu yer almaktadır.

sayi = int(input('Sayı giriniz :'))

asalMi = True

for x in range(2,sayi):
    if(sayi % x == 0):
        asalMi == False
        break
    

if(asalMi==True):
    print('Asal Sayı')
else:
    print('Asal sayı değil')
    
