""" 25/12/2020 Object Orianted Programming Classes"""

class Person :
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age      = age
        
        
        
person1 = Person('Melike','Eryılmaz',23)

print(person1.firstName)

print(person1.lastName)
