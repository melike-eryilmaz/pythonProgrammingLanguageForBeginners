"""28/12/2020 Exception Handling"""
""" Herhangi bir hata olduğu zaman yakalamak için try except bloklarını kullanırız.
    try daki kod bloğu çalışmazsa alttaki except ,oda çalışmazsa alttaki except çalışır.
    ValueError-tip hatası ,ZeroDivisionError -sıfıra bölünememe hatası şeklinde pythonda hata türleri vardır.
"""

try :
    sayi = int(input('Lütfen bir sayı giriniz :'))
except ValueError:
    print('Tip uyuşmazlığı,lütfen sayı girin..')

except ZeroDivisionError:
    print('Sıfıra bölünme hatası ,Payda sıfır olamaz.')
    
except:
    print('Sebebi bilinemeyen bir hata oluştu.')
    
    
    
print('Bitti') 
