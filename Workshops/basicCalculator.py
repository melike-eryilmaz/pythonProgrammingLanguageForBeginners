""" 27/12/2020 Hesap makinesi
    Kullanıcıdan yapılacak olan işlemi ve iki adet sayıyyı alarak fonskiyonlar ile 
    sonucu hesaplama ve ekrana yazdırma örneğidir.

"""
def sumOp(number1,number2):
    return number1+number2

def difOp(number1,number2):
    return number1-number2

def impactOp(number1,number2):
    return number1*number2

def partitionOp(number1,number2):
     return number1/number2

print('Lütfen yapmak istediğiniz operasyonu seçiniz..')
print(' 1 : Topla')
print(' 2 : Çıkar')
print(' 3 : Çarp')
print(' 4 : Böl')

operations = int(input('Operasyon ? :'))
number1    = int(input('Birinci sayı :'))
number2    = int(input('Birinci sayı :'))

if operations == 1:
    sonuc = sumOp(number1,number2)
    
elif operations == 2:
    sonuc = difOp(number1,number2)
    
elif operations == 3:
    sonuc = impactOp(number1,number2)
    
elif operations == 4:
    sonuc = partititonOp(number1,number2)
else :
    print('Geçersiz seçim yaptınız..')
    
print('Sonuc:',sonuc)
