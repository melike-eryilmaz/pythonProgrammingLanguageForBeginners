# 21/12/2020 forIteration 

sehirler = ['İstanbul','Ankara','İzmir']
print(sehirler[0])
print(sehirler[1])
print(sehirler[2])

for sehir in sehirler :
    if sehir != 'İstanbul':
        print(sehir+' için sehir kodu:'+sehir[0:3])
        print('***************************')
