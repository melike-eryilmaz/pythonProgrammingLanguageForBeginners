""" 25/12/2020 Object Orianted Programming - Classes"""
"""Ortak özellikleri ve fonksiyonları bir arada tutup erişmemizi sağlarlar."""

"""" 25/12/2020 Object Orianted Programming 
    Classlar genel olarak bakıldığında bir şeyleri organize etmek için kullanılırlar.
    Örneğin uygulamanızda birden fazla yerde kullanmak istediğiniz belirli işlemleri gerçekleştiren 
    fonksiyonlarınız var ve bunlara hemen hızlıca erişmek istiyorsanız class içerisinde birbiriyle ilişkili
    fonksiyonları toplayarak ilgili fonksiyona classlar üzerinden hızlıca erişebiliriz.

"""
class Matematik :
    
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        
    def topla(self,sayi1,sayi2):
        return self.sayi1 + self.sayi2
    
    def cikar(self,sayi1,sayi2):
        return self.sayi1 - self.sayi2
        
    def carp(self,sayi1,sayi2):
        return  self.sayi1 * self.sayi2
    
    def bol(self,sayi1,sayi2):
        return self.sayi1 / self.sayi2
    
    
    
matematik = Matematik(1,2)

print('Toplam :'+ str(matematik.topla(1,4)))

