""" 28/12/2020 Mapping 
    Mapping tüm programlama dillerinde olan bir terimdir.
    Kelime anlamı haritalamak,eşitlemek şeklindedir.
    Örneğin elimizde K nesnesi olsun ve bu nesnenin isim,soyisim,adres şeklinde özellikleri olsun.
    Bu nesnenin özelliklerini aynı veya farklı şekilde M nesnesine aktarmak için map() komutu kullanılır.

"""
# Bir listenin elemanlarının karesini alıp yeni bir diziye atmanın iki yöntemi vardır.
# for ile dönerek yapabiliriz veya map() ile yapabiliriz.

numbers = [1,2,3,4,5]

numbers_sqrt = list(map(lambda number : number**2,numbers))
numbers2=[]
for x in numbers :
    numbers2.append(x*x)
    
    
print(numbers_sqrt)
print(numbers2)
