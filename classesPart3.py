""" 25/12/2020 Object Orianted Programmimng -Class -İnit functions and self details
    
    Class lar çağrıldığı zaman her zaman arkada çalışan bir constructor bloğu bulunur.
    Python da constructor init fonksiyonudur.
    Constructor içerisinde fonksiyonların alacağı parametreleri belirleyip fonksiyonların 
    içersinde o parametrelere self ile erişebiliriz.

"""
class Matematik :
    
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        
    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
        
    def carp(self):
        return  self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
    
    
    
matematik = Matematik(1,2)

print('Toplam :'+ str(matematik.topla()))

