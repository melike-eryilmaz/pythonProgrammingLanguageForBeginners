""" 04/01/2021 İndexing """

import numpy as np 

numbers = np.array([0,5,10,15,20,25,30])
# Dizinin elemanlarını tersten yazdırır.
print(numbers[::-1])

print(numbers[6])
# Dizinin elemanlarını 0. indisten 3 üncü indise kadar 3. indis dahil değil yazdırır.
print(numbers[0:3])


numbers2 = np.array([[0,5,10],[15,20,25]])
# Tüm satırlarda 2. indisi alır.
print(numbers2[:,2])

# Tüm satırlarda o. sütundan 2. sütuna kadar olan elemanları al.
print(numbers2[:,0:2])

# Tüm sütunlarda -1 .ci satıra kadar olan elemanları al.
print(numbers2[-1,:])

print(numbers2[:,-1])
