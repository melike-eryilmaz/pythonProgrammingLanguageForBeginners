""" 27/12/2020 File Operations
    Liste içerisindeki verileri sırasıyla dosyaya yazma uygulaması

"""
Persons = ['Zafer','Duygu','Esra']
fileToAppend = open('Persons.txt','a')

for person in Persons:
    fileToAppend.write(person)
    fileToAppend.write('\n')

fileToAppend.close()
