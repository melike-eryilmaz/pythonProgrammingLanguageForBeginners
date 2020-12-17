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
