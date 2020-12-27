""" 27/12/2020 File Operations """
#%%
# a mode :append mode dosyanın sonuna ekleme yapmamızı sağlar.
# Direkt sonuna boşluk vs koymadan ekleme yapar .
# \n ile bir satır in dedikten sonra yazabiliriz.
fileToAppend = open('students.txt','a')
fileToAppend.write('\n')
fileToAppend.write('Hellooo')
fileToAppend.close()

#%%


#%%
# append ile dosyanın sonuna yazarken write ile dosyanın üzerine yazarız.
fileToAppend = open('students.txt','w')
fileToAppend.write('\n')
fileToAppend.write('melike')

#%%

#%%
# Dosyaları silmek için os kütüphanesi kullanılır.
import os 

if os.path.exists('exampleFile.txt'):
    os.remove()
else:
    print('Dosya yok')

# Dizini silmek için rmdir() fonksiyonu kullanılır.
os.rmdir('empty')

#%%
