""" 04/01/2021 Linspace :Başlangıç bitiş ve adet verilerek dizi üretmemizi sağlar."""
import numpy as np 

# 1 den 10 a kadar eşit aralıklarla 5 sayı üretmek 
a = np.linspace(1,10,5)
print(a)


# 
from  numpy import pi
x = np.linspace(0,2*pi,100)
print(x)
# Sinüs hesaplayabiliriz.
print(np.sin(x))
