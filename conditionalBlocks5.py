sayi1=8
sayi2=9
sayi3=12
#Neden çalışmadı bir kontrol et
if sayi1>sayi2 & sayi1>sayi3 :
  print("En Büyük:",sayi1)
  if sayi2>sayi3:
    print("En Küçük",sayi3)
  else:
    print("En Küçük",sayi2)

elif sayi2>sayi1 & sayi2>sayi3:
  print("En Büyük:",sayi2)
  if sayi1>sayi3:
    print("En Küçük",sayi3)
  else:
    print("En Küçük",sayi1)
    
elif sayi3>sayi1 & sayi3>sayi2:
  print("En Büyük",sayi3)
  if sayi1>sayi2:
    print("En küçük",sayi2)
  else:
    print("En Küçük",sayi1)
else:
  print("yok")
