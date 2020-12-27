""" 26/12/2020 Python Genel Tekrar
    Burada başlangıçtan bugüne kadar yazılan kodlara ve farklı yöntemlere değinmek adına 
    genel bir tekrar için kodlar eklenmiştir.

"""

# Konsola bir şey yazdırmak için print() fonksiyonunu kullanırız.

print('Merhaba Python')

# Kullanıcıdan bir input değeri almak için input() fonksiyonunu kullanırız.
# Genellikle input alınan değeri bir değişkende saklarız.
# input() fonksiyonu default olarak string türde veri alır.

name = input('Please enter your name : ')
print('Hi!',name)

# Veri tipleri -data types
# Python'da data dinamik tiplerden oluşur ve tipler değişebilir
# Basit data tipleri integers (Tam sayı), floats (Noktalı sayı), strings (Metin), booleans (Mantıksal)
# Pythonda karakter data tipi yoktur

print(type(10))
print(type("10"))
print(type(10.0))
print(type(10.))

# Pythonda noktalı sayılar vardır.
# Noktalı sayılar en fazla 15 haneye duyarlıdır.

number1 = 1.1111111111111113
number2 = 1.1111111111111115
numberssum = number1 + number2
print(len(str(numberssum)))
print(numberssum)

# Python da string veri tipleri '' veya "" arasına yazılır.
stringEx = 'home sweet home'
print(stringEx)

# Python da tipleri birbirine çevirebiliriz.Type casting 
# \t string içerisinde bir tab ileri git anlamına gelir.
print('string to int \t',type(int('34')))
print('int to string \t',type(str(34)))
print('float to int \t',type(int(3.5)))

# print() içerisinde bir ayırıcı belirtilip ona göre ifade ayırılabilir.

print(12,34,56,sep='/')

# print() fonksiyonu default olarak yeni satıra geçer .Eğer bunu istemiyorsak sonunun ne olacağını belirtebiliriz.
print('No new line',end = '\t\t')
print('test')

# Pythonda temel olarak kullanılan matematiksel operatörler aşağıdaki gibidir.

print("5 + 2 =", 5 + 2)

print("5 - 2 =", 5 - 2)

print("5 * 2 =", 5 * 2)

print("5 / 2 =", 5 / 2)

print("5 % 2 =", 5 % 2) # Mod (Kalan)

print("5 ** 4 =", 5 ** 4) # Üs

print("5 // 2 =", 5 // 2) # Tam sayı bölme

#%%%
# Python da math kütüphanesi fonksiyonları çok geniştir.
import math
# Diğer matematik işlemleri
"""
    abs, max, min, pow, ceil, floor, round, exp, log, sqrt 
    sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh
    hypot, radians, degrees
"""

print(math.cos(0))
print(math.sin(math.pi/2))
print(math.sin(math.pi), "= 0")
print(math.cos(math.sin(math.tanh(0))))

print(math.inf) # Infinitive -sonsuz
print(math.inf - math.inf) # Nan-not a number

#%%

#%%
# Python random kütüphanesi kullanarak integer random değerler oluşturabiliriz.
import random
print("Random", random.randint(1, 101)) # random.randint(başlangıç:bitiş)

#%%

#%%
# Conditional Blocks
# Pythonda kıyaslama operatörleri > < == <= >= != şeklindedir.
# Pythonda mantıksal operatörler ise and ,or,not şeklindedir.
# Yaş 5 ten küçükse okul yok,5 ve 6 ya eşit veya arasında ise anaokulu,6 dan büyük 17 ye eşit veya 
# küçük ise yaş-5 ci sınıf hiçbiri değilse lise yazdıralım .
age = 30
if age < 5:
    print("No school")
elif (age >= 5) and (age <= 6):
    print("Primary school")
elif (age > 6) and (age <= 17):
    print((age - 5), ". class ")
else:
    print("High School")

#%%

#%%
# Eğer age 18 den büyükse canVote true olsun aşağıdaki gibide denebilir.
canVote = True if age >= 18 else False
print(canVote)
# Eğer age büyüktür 18 ise yetişkin değilse genç yazdır.
result = "Adult" if age >= 18 else "Young"
print(result)
#%%






































