"""
    24/12/2020 İki matirisin toplamını hesaplayan uygulama
    Matris toplamları şu şekilde hesaplanmaktadır.
    x[0][0]+y[0][0] = z[o][0]
    Bunun için x i gezmek için bir döngü y yi gezmek için bir döngü tanımlayabiliriz.

"""

matris1 =[[1,2,3],
          [4,5,6],
          [4,5,6]]
          
          
matris2 =[[1,2,3],
          [4,5,6],
          [4,5,6]]

matris3 =[[0,0,0],
          [0,0,0],
          [0,0,0] ]         
# sabit uzunluk vererek
for x in range(0,3):
    for y in range(0,3):
        matris3[x][y] = matris1[x][y]+matris2[x][y]
    
    
print(matris3)

# Matrislerin uzunluğunu vererek
for x in range(len(matris1)):
    for y in range(len(matris2)):
        matris3[x][y] = matris1[x][y]+matris2[x][y]
        
        
print(matris3)





