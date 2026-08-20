'''
class
Object
Encapsulation
Inharitance
Abstraction
polymorphisum
'''

'''
class is a bluprint of an object
object is an instance of class
'''

class Student:
    def __init__(self): ## name of a class
        self.name='sriya' ## variable
        self.age=17 ## properties/attributes of a class 

    def display(self): ## function ## methods
        print(f'my student name is {self.name} and she is {self.age} years old')    

a=Student()
a.name='raji'
print(a.name)

b=Student()
print(b.name)


'''
attributes
class attributes
instance attributes
methods
class methods,static methods
instance methods
'''