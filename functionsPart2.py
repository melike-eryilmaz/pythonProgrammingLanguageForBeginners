# 22/12/2020 Functions

# Fonksiyonlar tekrar tekrar kullanılabilir.
# Fonksiyonlara parametre olarak verilen değerlere default value atanabilir.
# Fakat birden fazla parametre içerisinde bazıları default değer alırken bazıları almıyorsa default değer alan parametreler en sağda-en sonda tanımlanmalıdır.

def selamVer(isim):
    print('Merhaba '+isim)

selamVer('Melike')
selamVer('Selin')
selamVer('Selena')


def selamVer2(isim,soyisim = 'Arkadaş'):
    print('Merhaba '+isim+' '+soyisim)
    

selamVer2('Derin')

selamVer2('Derin','Otto')

def selamVer3(isim='ziyaretçi',soyisim = 'Arkadaş'):
    print('Merhaba '+isim+' '+soyisim)
