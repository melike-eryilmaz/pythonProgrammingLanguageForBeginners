""" 04/01/2021 Basic Operations"""

import numpy as np
a = np.array([20,30,40,50])
b = np.arange(4)

print("a dizisi :",a)
print("b dizisi :",b)

c = a-b #İki diziye birbirinden çıkarabiliriz.Aynı indislerde işlem yapar.
print("c dizisi :",c)

d = b**3 #Dizinin kübünü alır.
print("d dizisi :",d)

e = 10 * np.sin(a) #Dizinin sinüsünü alıp 10 ile çarpar.
print("e dizisi :",e)

# Elemanlar 7 den küçük mü bakar küçükse true değilse false şeklinde yeni bir dizi oluşturur.
print("e dizisi küçük 7 :",e<7)
# İki diziyi çarpar.
print("a*b dizisi :",a*b)
# Matris çarpımı için @ kullanılır.
print("a@b dizisi :",a@b)

print("a.dot(b) dizisi :",a.dot(b))

f = np.ones((2,4))
print("f dizisi :",f)

g = np.zeros((2,4))
print("g dizisi :",g)

h = np.random.random((2,4))
print("h dizisi :",h)

i = np.sum(b)
print("i dizisi :",i)

print("b.sum() dizisi :",b.sum())

j = np.min(b)
print("j dizisi :",j)

k = np.max(b)
print("k dizisi :",k)

l = np.sqrt(a)
print("l dizisi :",l)
