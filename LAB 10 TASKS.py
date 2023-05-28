# initialize the amount variable
amount = 10000
if(amount > 2999):
    print("You are eligible")
    
#%%

# initialize the amount variable
marks = 10000
# perform division with 0
a = marks / 0
print(a)

#%%

try:
 a = 10
 b = 0
 c = a/b
except:
     print("Can't divide with zero")
     
#%%

l1 = [1,2,5,8,9]
l2 = [1,5.6,"hello"] # mix of data types
l1[1] = 100 # muting the 1st position of l1 to 100
print(l1)
del l1[2] # delete from a position 2
print(l1)
#%%

l10 = [1,2,6,7,4,5,7,8,6,3]
l11 = [1,2,6,7,4,5,7,8,6,3,1000]
## numpy operations
np.mean(l11)
np.median(l11)
np.std(l11)

#%%

try:
 #block of code
except Exception1:
 #block of code
else:
 #this code executes if no except block is executed
 
#%%

 try:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     c = a/b
     print(a/b)
 
except Exception:
                 print("can't divide by zero")
                 print(Exception)
else:
     print("Hi I am else block")
 
#%%

try:
    a=10/1
    print(c)
except ArithmeticError:
                       print("Arithmetic Exception")
except NameError:
                 print("HH")
else:
     print("Successfully Done") 

#%%

def fun(a):
          if a < 4:

# throws ZeroDivisionError for a = 3
             b = a/(a-3)

# throws NameError if a >= 4
print("Value of b = ", b)

try:
    fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
                        print("ZeroDivisionError Occurred and Handled")
except NameError:
                print("NameError Occurred and Handled")
        
#%%

 try:
     fileptr = open("file2.txt","r")
     try:
         fileptr.write("Hi I am good")
     finally:
        fileptr.close()
        print("file closed")
 except:
       print("Error")
     
#%%

 try:
     age = int(input("Enter the age:"))
     if(age<18):
               raise ValueError
     else:
         print("the age is valid")
 except ValueError:
                   print("The age is not valid")
     
#%%

 try:
     a = int(input("Enter a:"))
     b = int(input("Enter b:"))
     if b is 0:
          raise ArithmeticError
     else:
         print("a/b = ",a/b)
except ArithmeticError:
                       print("The value of b can't be 0")
     
#%%

# define Python user-defined exceptions
class Error(Exception):
                       """Base class for other exceptions"""
pass

class ValueTooSmallError(Error):
                                """Raised when the input value is too small"""
pass

class ValueTooLargeError(Error):
                                """Raised when the input value is too large"""
pass

#%%

# you need to guess this number
number = 10
# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
                    raise ValueTooSmallError
        elif i_num > number:
                    raise ValueTooLargeError
                    break
    except ValueTooSmallError:
                        print("This value is too small, try again!")
                        print()
    except ValueTooLargeError:
                        print("This value is too large, try again!")
                        print()
                        print("Congratulations! You guessed it correctly.")
                        
#%%

x = 10
assert x > 0
print('x is a positive number.')

#%%

x = 0
assert (x > 0, 'Only positive numbers are allowed')
print('x is a positive number.')

#%%

def square(x):
            assert x>=0, 'Only positive numbers are allowed'
            return x*x
n = square(2) # returns 4
n = square(-2) # raise an AssertionError

#%%

def square(x):
            assert x>=0, 'Only positive numbers are allowed'
            return x*x
            try:
                square(-2)
            except AssertionError as msg:
                            print(msg)
    
#%%

def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)
mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))
mark1 = []
print("Average of mark1:",avg(mark1))



    
# This script calculates the factorial of a given
# integer, which is the product of the integer and
# all positive integers below it.

number = 5
multiplier = 1

while multiplier < number:
        number *= multiplier
    multiplier += 1

print (number)



























# This script calculates the factorial of a given
# integer, which is the product of the integer and
# all positive integers below it.

number = 5
multiplier = 1

while multiplier < number:
    number *= multiplier
    multiplier += 1

print (number)