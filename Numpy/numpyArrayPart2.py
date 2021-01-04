""" 04/01/2020 Numpy Array"""
import numpy as np

a = np.array([1,3,5,7,9,11])
a = a.reshape(2,3)

print(a)
print(a.dtype) # dtype dizinin elemanlarının tiplerini verir.
print(a.ndim)  # ndim dizinin boyutunu verir.

b = np.array([[1,3],[5,7],[9,11]])
print(b)
print(b.ndim)
