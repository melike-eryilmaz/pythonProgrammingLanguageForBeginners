# 12/12/2020 lower() upper() fonksiyonları
#Python da stringler ile işlemler yapmak için özel string fonksiyonları vardır.
#Bunlardan bazıları upper() (string ifadeyi büyük harfe çevirir) ve lower() (string ifadeyi küçük harfe çevirir.

firstString = 'Python is awesome!'
secondStrşng='PYTHON is Awesome!'

print(firstString.lower())
print(firstString.upper())

if(firstString.lower() == secondStrşng.lower()):
    print('Two string are same')
else:
    print('Two string are not same')
    
