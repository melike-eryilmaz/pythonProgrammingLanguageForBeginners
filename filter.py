""" 28/12/2020 Mapping 
    filter() fonksiyonu
    Elinizde birsürü veri var ve belli şartlara göre o veriyi filtrelemek istiyorsanız filter() fonksiyonu kullanabiliriz.


"""


numbers = [1,2,3,4,5]

numbersFilter = list(filter(lambda number : number >2,numbers))
print('Filtrelenmiş liste :',numbersFilter)
