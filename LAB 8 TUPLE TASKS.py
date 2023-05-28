tup=1,2,3,4,5
tup1=(1,2,3,4,5)
tup2=(2,)
print(tup,tup1,type(tup2))

#%%

tup=('a','b','c','d','e')
print (tup[0])
print( tup[1:3])
tup[0]='x'

#%%

thistuple=("apple","banana","cheery")
print(thistuple[-1])

#%%

thistuple=("apple","banana","cheery","orange","kiwi","melon","mango")
print(thistuple[2:5])

#%%

thistuple=("apple","banana","cheery","orange","kiwi","melon","mango")
print(thistuple[:4])

#%%

thistuple=("apple","banana","cheery","orange","kiwi","melon","mango")
print(thistuple[2:])

#%%

thistuple=("apple","banana","cheery","orange","kiwi","melon","mango")
print(thistuple[-4:-1])

#%%

thistuple=("apple","banana","cheery")
if "apple" in thistuple:
    print("Yes,'apple' is in the fruits tuple")
    
#%%

x=("apple","banana","cheery")
y=list(x)
y[1]="kiwi"
x=tuple(y)

print(x)

#%%

thistuple=("apple","banana","cherry")
y=list(thistuple)
y.append("orange")
thistuple=tuple(y)
print(thistuple)

#%%

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#%%

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#%%

thistuple = ("apple", "banana", "cherry")
del (thistuple)
print(thistuple) #this will raise an error because the tuple no longer exist

#%%

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#%%

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#%%

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#%%

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    
#%%

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
    
#%%

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
    
#%%

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#%%

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#%%

a=4
b=6
(a,b)=(b,a)
print (a,b)

#%%

def swap(a,b):
    return(b,a)
x,y=input("Enter values:")
(x,y)=swap(x,y)
print ( "value after swaping:",x,y)












