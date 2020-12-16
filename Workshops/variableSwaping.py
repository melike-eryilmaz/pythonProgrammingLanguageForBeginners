#12/12/2020


x = 10 
y = 20 

#Yöntem 1 : x değerini temp bir değişkene atarak x içerisine y yi koyup daha sonra y içerisine temp değişkende tutulan değeri
# atabiliriz.
# temp = x
# x = y
# y = temp  

# Sadece python diline özel aşağıdaki şekilde variable swaping yapılabilir.
x,y = y,x



print("x = " + str(x))
print("y = " + str(y))
