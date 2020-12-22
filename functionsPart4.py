# 22/12/2020 lambda fonksiyonlar 
# lambda fonksiyonlar bir çok satırdan oluşan operasyonları tek satıra indirgememizi sağlar.


# '#%%' arasına kodlarımızı yazıp sadece bu aradaki kodların çalışabilmesi için sağ tık run cell yapabiliriz.(syper editöründe)
#%%
def dikucgenalanihesapla(a,b):
    return a*b/2;


alan=dikucgenalanihesapla(3,4)
print(alan)


#%%
#Üstteki fonksiyonu lambda kullanarak aşağıdaki şekilde yazabiliriz.

dikucgenalanihesapla2 =lambda a,b : a*b/2
print(dikucgenalanihesapla2(3, 6))
print(type(dikucgenalanihesapla2))

#Birçok dilde yapılamayan fonksiyonu aşağıdaki gibi bir değişkene atama işlemi pythonda yapılabilmektedir.
#Bir alt satırda x(4,5) şeklinde fonksiyon çağrılmıştır.
x= dikucgenalanihesapla2 
print(x(4,5))




