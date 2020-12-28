""" 28/12/2020 Iterators 

iterator
Elinizde bir tane liste var ise ve elemanlarını tek tek dolaşmak istiyorsak iterator yöntemini kullanabiliriz.
Kendi iteratorlerimizi yazabiliriz.
iter() fonksiyonu ile kendi ıteratorümüzü oluştururuz..
next() ile tüm elemanları dolaşabiliriz.
next() sırasıyla elemanları dolaşır.
"""
cities = ['Ankara','İstanbul','Van']


iterator = iter(cities)
# next() ile her seferinde bir sonraki elemana erişiriz.
# Eğer bir sonraki eleman yoksa hata alırız.
print(next(iterator))
print(next(iterator))
print(next(iterator))


# for döngüsünde arka planda iteratorler kullanılır.
for city in cities:
    print(city)
