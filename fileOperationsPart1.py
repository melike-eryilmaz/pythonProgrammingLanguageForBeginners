""" 27/12/2020 File Operations
    Programlama temeli aslında verilerle işlemlerdir.
    Verilere erişmek ,işlemek üzerine kurulu bir yapıdır.
    Burada da verilerin bulunduğu dosyaları okuma ,dosyalara yazma gibi işlemleri gerçekleştirebilmek
    için dosya işlemlerinden yararlanırız.

"""
#%%
# Aşağıdaki şekilde ismi verilen dosyayı aç demiş oluruz .
# Default olarak read modunda yani sadece var olan bir dosyayı açmamızı sağlar.
# Eğer ismini verdiğiniz dosya henüz yoksa hata verir.(no such file or directory)
f = open('customers.txt')
#%%

#%%
# Bir üstteki komutun aynısıdır.read mode
f = open('customers.txt','r')
#%%

#%%
# Eğer dosya yoksa oluşturmak istiyorsak w modu yani write modunu verebiliriz.
# write mode dosya yoksa o isimde bir dosya oluşturur.
 f = open('customers.txt','w')
#%%

#%% 
 # Dosyayı okumak ama aynı zamanda dosyaya ekleme de yapabilmek için a modunu kullanabiliriz.
 # append mode 
 f = open('customers.txt','a')
#%%

#%% 
 # Dosya yoksa oluşturmak için x modunu kullanabiliriz.
 # x :create mode
  f = open('customers.txt','x')
  
  #%%
  
  #%%
  f =open('customers.txt')
  # Yukarıda dosya yoksa oluşturup ,okuma komutlarını gördük.
  # customers.txt dosyasını oluşturduktan sonra içerisine txt metinler ekledim ve aşağıdaki gibi
  # f.read() komutuyla dosya içerisindeki txt metni okuyabiliriz.
  print(f.read())
  
  # Dosya içerinde sadece 2 karakteri okumak için 
  print(f.read(2))
  #%%
  
  
  #%%
  # read() dosya içerisindeki tüm herşeyi okurken readline() dosya içerisindeki satırları okur.
  # Her seferinde bir sonraki satırı okumaızı sağlar.
  # aynı anda hem read() hem readline() kullanmaya çalışırsanız zaten dosyayı baştan aşağı okuduğu
  # için tek bir sefer okuyup ikinci fonksiyonu çalıştırmayacaktır.
  # Bu yüzden okuma fonksiyonlarını aynı anda kullanmayız.
  f = open('customers.txt')
  print(f.readline())
  print(f.readline())
  print(f.readline())
  
  #%%
  
  #%%
  # Birsürü satırdan oluşan bir verimiz olduğunu ve satır satır okumamız gerekli olsaydı
  # Aşağıdaki gibi for ile kolayca veriyi okuyabilirdik .:)
  f =open('customers.txt')
  for l in f :
       print(l)
  
  #%%
