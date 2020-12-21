#17/12/2020 Setler
"""
Setler de de elemanlar değiştirelemez ve sıralı değillerdir.
Oldukça hızlı çalışırlar.
Set lerde belirli elemanlarına erişmek için bir yöntem yoktur.
"""

studentSet = {'Elif','Adnan','Gülbahar'}
print(studentSet)


for student in studentSet:
    print(student)
    


#Eğer Elif set içerisnde varsa true yoksa false döner.
print('Elif' in studentSet)


if 'Elif' in studentSet:
    print('Listede var')
    

#Setlere eleman eklemek için add() fonksiyonu kullanılır.
studentSet.add('Ali')
print(studentSet)


studentSet.update(['Melisa','Ebru','İklim'])
print(studentSet)


print(len(studentSet))

studentSet.remove('Elif')
print(len(studentSet))

# Üstte Elif elemanını silmiştik altta tekrar olmayan bie elemanı silemeye çalışırsak remove() keyerror hatasını fırlatır.
#Eğer remove işlemi yaparken key yoksa hata vermemesini istersek discard() kullanırız.
# studentSet.remove('Elif')
print(len(studentSet))

#discard() silme işlemi yapar ve  eğer key yoksa hata fırlatmaz.
studentSet.discard('Elif')
print(len(studentSet))


# pop() dizideki en son elemanı siler.Bellek içerisinde en üstte yer alanı siler.
x = studentSet.pop()
print(studentSet)
print(len(studentSet))


# clear() diziyi sıfır elemana ve boş bir sete çevirir.
# clear() fonksiyonu seti oda gibi düşünürsek sadece odanın içini yani setin elemanlarını siler.Set durar.

y = studentSet.clear()
print(studentSet)
print(len(studentSet))

# del ise hem elemanları hem de seti temizler.

del studentSet
print(len(studentSet))

# setler aşağıdaki gibi 2 şekilde tanımlanabilir.
students = {'Elif','Adnan','Gülbahar','Ela'}
students = set('Elvan','Arif')


