class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("John", 36)
print(p1.name)
print(p1.age)

#%%

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def myfunc(self):
        print("Hello" + self.name)
              
p1=Person("John", 36)
p1.myfunc()

#%%

class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age
    def myfunc(abc):
        print("Hello" +abc.name)
p1=Person("John", 36)
p1.myfunc()

#%%

class Dog:

    attr1 = "mammal"
    attr2 = "dog"
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

Rodger = Dog()

print(Rodger.attr1)
Rodger.fun()

#%%

class Dog:
    animal = 'dog'
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
print("\nAccessing class variable using class name")
print(Dog.animal)

#%%

class Employee:
 'Common base class for all employees'
 empCount = 0
 def __init__(self, name, salary):
         self.name = name
         self.salary = salary
         Employee.empCount += 1
 
 def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
 def displayEmployee(self):
     print ("Name : ", self.name, " Salary: ", self.salary)
     
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

#%%

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
x=Person("John", "Doe")
x.printname()

#%%

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear =year
        
x = Student("Mike", "Olsen", 2019)

#%%

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear =year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", 
self.graduationyear
