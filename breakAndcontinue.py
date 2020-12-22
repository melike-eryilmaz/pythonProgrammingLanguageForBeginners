# 22/12/2020 break continue
# break bağlı bulunulan döngü için döngüyü bitirmek demektir.
# Örnek kullanım olarak :Uygulamanıza bir veri geldi ,eğer o veri gelirse bir sonraki adımları
# çalıştırmak istemiyorsanız ,uygulamayı orda kırmak için break kullanırız.

sehirler = ['Ankara','İstanbul','İzmir']


# Aşağıdaki gibi gelen veri İstanbul olunca işlemlere devam etmek istemiyorsak kullanırız.
# Dikkat for iteration sonlandı diğer sehir için dönmedi.
for sehir in sehirler :
    if sehir == 'İstanbul':
        break
     
    print('Şehir :',sehir)
    print('*************')


# continue ise döngüde sadece o anki değerde işlemleri geçip diğerlerinde devam eder.
# break te karşılaşılan değerden sonra diğer değerlere bakılmamıştı ,continue da değerler tek tek değerlendirilir.

# Yani break döngüyü tamamen sonlandırırken continue sadece o anki loopu sonlandırır.
for sehir in sehirler :
    if sehir == 'İstanbul':
        continue
     
    print('Şehir :',sehir)
    print('*************')
