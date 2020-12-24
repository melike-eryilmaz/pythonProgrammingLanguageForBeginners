# 24/12/2020 Faktoriyel hesaplama 
# Kullanıcıdan alınan sayının faktöriyelini hesaplayan programı yazınız.
#  Örneğin 6! = 1*2*3*4*5*6 şeklindedir.
# Negatif sayıların faktoriyeli alınamamaktadır.


sayi = int(input('Faktoriyeli alınacak sayıyı giriniz : '))
faktoriyel = 1

if sayi < 0:
    print('Negatif sayıların faktoriyeli alınamaz.')

elif sayi == 0:
    print(faktoriyel)

else:
    for x in range(1,sayi+1,1):
        faktoriyel = faktoriyel * x
    print(faktoriyel)

