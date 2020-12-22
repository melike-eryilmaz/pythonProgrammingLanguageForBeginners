# 22/12/2020 for iteration example stars


sayi = int(input('Sayi giriniz :'))

yildiz = ''

# Başlangıç değeri dahil ,bitiş tarihi hariç olarak alır.
for x in range(1,sayi+1,1):
    yildiz = yildiz + '*'
    print(yildiz)
    
