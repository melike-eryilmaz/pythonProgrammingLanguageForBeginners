""" 25/12/2020 Object Orianted Programming Classes

    İnheritance : Ortak operasyonların bir yerde yazılıp her yerde kullanılabilmesi için kullanılır.
    Miras alma anlamına gelir.
    Örneğin Customer ve Worker sınıflarıda Person sınıfındandır.Person sınıfının özelliklerini alabilir.
    Ama Customer'ın kredikartınumarası varken Worker sınıfının maaş özelliği olabilir.
    Böyle durumlarda Customer ve Worker için iki ayrı sınıf -class oluşturup ortak olan özelliklerini ise 
    Person sınıfından miras alabiliriz.
"""

class Person :
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age      = age
        
# Worker Person dan miras olarak firstName,lastName,age özelliklerini alır.
class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
# Customer Person dan miras olarak firstName,lastName,age özelliklerini alır.
class Customer(Person):
    def __init__(self,creditcardNumber):
        self.creditcardNumber = creditcardNumber
   
        
ahmet = Worker()
# ahmet Person sınıfı özelliği olan fisrtName miras olarak almıştır.
print(ahmet.firstName)
print(ahmet.salary)


mehmet = Worker()
# mehmet Person sınıfı özelliği olan fisrtName miras olarak almıştır.
print(mehmet.firstName)
print(mehmet.creditcardNumber)
