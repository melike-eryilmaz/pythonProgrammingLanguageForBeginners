# 21/12/2020 conditional blocks workshop


sayi1 = int(input('İlk sayıyı giriniz:'))

sayi2 = int(input('İkinci sayıyı giriniz:'))

sayi3 = int(input('Üçüncü sayıyı giriniz:'))

if sayi1 > sayi2 and sayi1 > sayi3:
    enbuyuksayi = sayi1
elif sayi2 > sayi1 and sayi2 > sayi3:
    enbuyuksayi = sayi2
else:
    enbuyuksayi = sayi3


print('En büyük sayi:',enbuyuksayi)
