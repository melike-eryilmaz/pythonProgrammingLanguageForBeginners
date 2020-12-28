""" 28/12/2020 Mapping 
    reduce() fonksiyonu
    Kümülatif işlemler yapıp bir sonuca ulaşmak için reduce() fonksiyonunu kullanabiliriz.

"""
from functools import reduce 


numbers = [1,2,3,4,5]
# x her seferinde x*y ye eşit olur.Çarpa çarpa gider.
# Toplama,çıkarma,bölme gibi işlemlerde yapılabilir.
numbersFact= reduce(lambda x,y : x*y,numbers)

print(numbersFact)



