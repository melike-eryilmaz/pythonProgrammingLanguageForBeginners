#12/12/2020 14:30
#Python Değişkenler

#Değişken : Elimizde çeşitli veri türleri bulunmakta ve 
#bu değerlere program içerinde erişmek istiyorsak bunları hafızada değişkenler ile tutabiliriz.
#Uygulama içerisinde değerleri tutucu hafıza olarak düşünülebilir.

#Python da değişkenleri tanımlarken diğer dillerdeki gibi tip belirtmek zorunlu değildir.

sayi = 12
isim = 'Melike'
soyisim = 'Eryılmaz'
tc = '12345678901'
telefonNumarasi = '053683333333'
floatSayi = 12.44


#tc bir string şekilde tanımlanmış değişken olduğu için float tipine dönüştürüp işlem yaptık.
#Eğer floata dönüştürmeden string ifade ile sayıyı toplamaya çalışsaydık hata verirdi.String ile sayı toplanamaz.
print(float(tc)+23)

#type() fonksiyonu geriye değişkenin tipini döndürür.
print(type(floatSayi))

print(type(sayi))

print(type(tc))

#Spyder ıdesinde variable explorer adında yazılan kodların sonuçlarını grid şeklinde bir yapıda gösteren özellik 
#bulunmaktadır.(View-Panes-Variable Explorer)
