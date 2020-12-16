# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 17:06:41 2020

@author: Melike.Eryilmaz
"""

#Kullanıcıdan km cinsinden değerler alıp kaç mil olduğu bulup ekrana yazdıran programdır.
#1.Yöntem
km = input('Please enter the km : ')

mil = float(km)* float(0.621371192)

print(str(km)+' km = '+str(mil)+'mil')



# 2. Yöntem
donusumOrani = 0.621371192
km = float(input('Km? = '))
mil = donusumOrani*km

print(str(km)+' km = '+str(mil)+'mil')
