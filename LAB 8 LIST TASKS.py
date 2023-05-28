#LIST

#%%

a=['ITCL',2.0,6,[5,7]]
print(a[0],a[-1])
i=0
while i<4:
    print(a[i])
    i +=1
    
#%%

a=[1,2,3]
b=[4,5,6]
print(a+b)
print([0]*4,a*3)
print(b[1:],b[:])

#%%

mylist=['a','b','c','d','e','f']
mylist[2]='x'
print(mylist)
mylist[1:3]=['c','g']
print(mylist)
del mylist[0]
print(mylist)

#%%

a=[1,2,3]
b=a[:]
print(b,id(a)==id(b))

#%%

def double (a):
    for i in range(len(a)):
        a[i]=2*a[i]
    return a
n=['a',2,'b',4,5]
a=double(n)
print(a)

#%%

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1])
print(matrix[2][1])
