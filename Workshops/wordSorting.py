""" 25/12/2020 Kelime sıralama 
    Kullanıcıdan bir kelime dizisi isteyip girilen kelimeleri alfabetik sıraya sokan ve tek tek kelimeleri yazdıran program
"""

# Kullanıcıdan kelimeleri alıyoruz.
kelimeler = input('Kelime dizisi veya cümle giriniz : ')

# split() ile kelimeleri ayırıp dizye atıyoruz.
kelimedizisi = kelimeler.split()

print(kelimedizisi)

# Kelimeleri sıralıyoruz.
kelimedizisi.sort()

print(kelimedizisi)

# Kelimeleri tek tek yazdırıyoruz.
for x in kelimedizisi:
    print(x)
