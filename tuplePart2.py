#17/12/2020 Tuple
"""
Python tuple
Tuple lar read only yani sadece okunabilir sistemlerdir.
Perfomans gerektiren sistemlerde tuple veri yapısı tercih edilebilir.
Tuple içerisinde diziler,tuple lar eleman olarak yer alabilir.
  """
tupleListe = (1,2,'Hello',(1,'melike',1.2),[])
liste = [1,2,3,'Hello',(1,2,'a'),[2]]


#Listelerde elemanlar değişebiliyorken tupleListe lerde değişiklik yapılamaz.
#
liste[2]='yeni'
# tupleListe[3] = 'êlma'  #Tuple object does not support assigment hatası verir.

tupleDeger = ('Melek',)
print(type(tupleDeger))

#Tuple listelerde 1:2 belirtildiğinde  1.index ten 2.ye kadar 2.dahl değil şeklinde alınır.
print(tupleListe[1:2])
print(liste[1:2])

#-2 inci index ler sağdan 2. anlamına gelir.
#Diziler ve tuple larda aynı şekildedir.
print(tupleListe[-2])

print(liste[-2])

print(type(tupleListe))
print(type(liste))

print(tupleListe)
print(liste)
