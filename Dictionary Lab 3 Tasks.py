#%%LAB TASK 1
dict_integers={1:'apple',2:'mango',3:'orange',4:'pears',5:'banana'}
num=int(input("Enter a number:"))
if num in dict_integers:
    print("True")
else:
    print('False')

#%%LAB TASK 2
dict1={1:2,4:3,7:4}
copy=dict1.copy()
for(x,y) in copy.items():
        a=y**2
        dict1.update({x:a})
        
print(dict1)

#%%LAB TASK 3
string=input("Enter a string:")
list1=list(string)
sorted_list=sorted(list1)

count={}
for letter in sorted_list:
    if letter in count:
        count[letter]+=1
    else:
        count[letter]=1
print (count)
    