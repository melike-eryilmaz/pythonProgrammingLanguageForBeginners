""" 25/12/2020 Object Orianted Programming - Classes"""
"""Ortak özellikleri ve fonksiyonları bir arada tutup erişmemizi sağlarlar."""

class Matematik :
    
    def _init_(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi1 = sayi2
        
    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cikar(self):
        return self.sayi1 - self.sayi2
        
    def carp(self):
        return  self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
    
    
    


