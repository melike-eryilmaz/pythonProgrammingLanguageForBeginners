#12/12/2020 
#Kullanıcıdan veri almak için input() kullanırız ve input olarak alınan değerler string olarak alınır.

name = input('Please enter your name : ')
surname = input('Please enter your surname : ')

firstNumber = input('Please enter  first number : ')
secondNumber = input('Please enter second number : ')

#inputlar string olarak alındığı için matematiksel işlemleri tip dönüşümü yaptıktan sonra yapmalıyız.
print('Sum:',firstNumber+secondNumber)

print('Real Sum : ',int(firstNumber)+int(secondNumber))
