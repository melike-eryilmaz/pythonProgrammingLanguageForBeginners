 # mathModule ü burada import edip içerisindek,i fonksiyon  ve özellikleri kullanabiliriz.
#%%
import mathModule 

mathModule.sum(1,2)
mathModule.diff(5,3)

#%%

#%%
# Moduleleri import ederken program içerisinde farklı bir isimle erişmek istersek as ile takma ad koyabiliriz.
import mathModule as mm

mm.sum(56,2)

#%%


#%%
# Module içerisinde sadece bir fonksiyona yada özelliğe erişmek istersek sadece o fonksiyonu import edebiliriz.
from mathModule import sum
mathModule.sum(1,2)
#%%

#%%
from mathModule import customer

print(customer['firstName'])
#%%
