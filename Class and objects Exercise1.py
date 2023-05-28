class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

s1 = Students('Samreen', 19, '13th')
print(s1.name)
print(s1.age)
print(s1.grade)

#%%

class students:
    pass

s1=students()
print(s1)

#%%

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())

#%%
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
    def rectangle_perimeter(self):
        return (2*(self.length+self.width))
    
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
print(newRectangle.rectangle_perimeter())

#%%

class Rectangle():
    def __init__(self, l, w):
        self.l= l
        self.w= w

    def area(self):
        return self.l*self.w
    def perimeter(self):
        return (2*(self.l+self.w)) 
    def display(self):
        print(self.l)
        print(self.w)        
        print(obj.area())
        print(obj.perimeter())
x=int(input("Enter length: "))
y=int(input("Enter width: "))
obj=Rectangle(x,y)
print(obj.display())

