""" 28/12/2020  Exception Handling - Hata Yakalama
    Bize gelen bir dizi içerisinde gelmesi gereke değerlerden farklı değerler de yanlışlıkla geldiğini düşünelim.
    Örneğin sayılardan oluşan bir dizi gelmesi gerekirken string ifadeler de karışmış olsun.
    Dolayısıyla dizi hatasız sayılardan gelecek diye düşünüp try except olmadan program kodu yazarsak hataları yakalayamayız.
    try except kullanarak hataları yakalayalım.

"""
# sistem üzerinden verilen hataları okumak için sys kütüphanesini import ediyoruz.
import sys

data = [1,2,'abc',"6",0]

for x in data:

    try:
        print('Sayı : '+str(x))
        result = 1/int(x)
        print('Sonuc :',result)
    except ValueError:
        print(str(x)+' bir sayı değil!')
        
    except ZeroDivisionError:
        print('Sıfıra Bölme hatası')
    except :
        print(str(x)+' hesaplanamadı.')
        print('Sistem tarafından :',sys.exc_info([0]))
