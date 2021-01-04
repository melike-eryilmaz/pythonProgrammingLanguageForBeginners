
"""
04/01/2021
Veri analizi ---Python
Pythonda veri analizinde kullanılan iki temel kütüphane numpy ve pandasdır. 

numpy --> num-py -sayısal python kütüphanesidir.
Diziler üzerinden işlemler gerçekleştirilir.
  
"""
import numpy as np

# havaDurumu = [[12,23,34],[24,27,22],[12,26,16]]
# print(havaDurumu)

# numpy arange() ile 0 dan verilen sayıya kadar bir array oluşturur.
nparray = np.arange(15)
print(nparray)

# Numpy ile oluşturduğumuz diziyi yeniden boyutlandırmak-yapılandırmak için reshape(satir,sütun) kullanırız.
nparray_reshape = np.arange(15).reshape(3,5)
print(nparray_reshape)
print(type(nparray_reshape))
# Dizinin boyutunu bulmak için ndim kullanılır.
print("Dimension Count = "+str(nparray_reshape.ndim))


# Kaç elemanlı ,boyutlu bir dizi olduğunu bulmak için shape kullanırız..
nparray1 = np.arange(10)#10 elemanlı 1 boyutlu..
print(nparray1.shape)
print(nparray1.ndim)
