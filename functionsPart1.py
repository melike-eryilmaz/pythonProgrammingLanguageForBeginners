# 22/12/2020 Functions
"""Bir kodu birden fazla yerde kullanmamız gerekiyorsa her yerde teker teker yazmamızı engeller."""
"""Örneğin uygulmanızda kdv tanımları bir çok yerde lazım ve bunları tek tek yapmamız gerekiyorsa kdv miktarını geriye
dönen bir fonksiyon yaptığımız zaman istediğimiz yerlerde bu fonksiyonu çağırabiliriz.
Her alanda farklı kdv tanımlanıyor diye düşünürsek fonksiyona parametre olarak hangi kdv tanımı istendiği gönderip
gönderilen değere göre kdv değerini bulup döndürebiliriz."""

# The function greets to person passed is a parameter.
def greet(name):
    
    print('Helloo '+name+'.Good Morning !')


greet('Melike')
