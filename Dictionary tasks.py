thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict["brand"])

#%%

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"year": 2020
}
print(thisdict)

#%%

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964,
"year": 2020
}
print(thisdict)
print(len(thisdict))

#%%

thisdict= {
"brand": "Ford",
"electric": False,
"year": 1964,
"colors":["red", "white", "blue"]
}

thisdict= {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(type(thisdict))

#%%

thisdict= {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict["model"]
print(x)

#%%

car={
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.keys()
print(x) #beforethechange
car["color"]= "white"
print(x) #after the change

#%%

car={
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.values()
print(x) #before
car["year"] = 2020
print(x) #after the change

#%%

car={
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.values()
print(x) #beforethechange
car["color"] = "red"
print(x) #after the change

#%%

car={
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.values()
print(x) #beforethechange
car["color"] = "red"
print(x) #after the change
x = thisdict.items()

#%%

car={
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.items()
print(x) #beforethechange
car["year"] = 2020
print(x) #after the change

#%%

car={
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.items()
print(x) #beforethechange
car["color"] = "red"
print(x) #after the change

#%%

thisdict= {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
    
#%%

thisdict= {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict["year"] = 2018
print(thisdict)

#%%

thisdict= {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

#%%

thisdict= {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict["color"]= "red"
print(thisdict)

#%%

thisdict= {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)

#%%

thisdict= {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.pop("model")
print(thisdict)

#%%

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": "1964"
}
thisdict.popitem()
print(thisdict)

#%%

thisdict= {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
del thisdict["model"]
print(thisdict)

#%%

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
del thisdict
print(thisdict)

#%%

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.clear()
print(thisdict)

#%%

thisdict= {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict =thisdict.copy()
print(mydict)

#%%

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict = dict(thisdict)
print(mydict)

#%%

myfamily={
"child1" :{
"name" : "Emil",
"year" : 2004
},
"child2" :{
"name" : "Tobias",
"year" : 2007
},
"child3" :{
"name" : "Linus",
"year" : 2011
}
}
print(myfamily)

#%%

child1={
"name" : "Emil",
"year" : 2004
}
child2={
"name" : "Tobias",
"year" : 2007
}
child3={
"name" : "Linus",
"year" : 2011
}
myfamily={
"child1" :child1,
"child2" :child2,
"child3" :child3
}
print(myfamily)

#%%

eng2num={}
eng2num["one"]="1"
eng2num["two"]="2"
print(eng2num)

#%%

eng2num={'one':'1','two':'2','three':'3'}
print(eng2num)
print(eng2num['three'])

#%%

inventory={'apple':'430','banana':'312','orange':'525','pears':'217'}
print(inventory)
del inventory['pears']
print(inventory)
print(len(inventory))

#%%

eng2num={'one':'1','two':'2','three':'3'}
print (eng2num.keys())
print (eng2num.values())

#%%

eng2num={'one':'1','two':'2','three':'3'}
print(eng2num.items())
print('one' in eng2num)

#%%

opposites={'up':'down','right':'wrong','true':'false'}
alias=opposites
print(alias,id(alias)==id(opposites))
copy=opposites.copy()
print(copy,id(copy)==id(opposites))

#%%

string1="mississippi"
letter_counts={}
for letter in string1:
    if letter in letter_counts:
        letter_counts[letter]+=1
    else:
        letter_counts[letter]=1
print (letter_counts)
print('i',4)in letter_counts.items()

#%%

classes={'Math':['A','B','C'],
         'Physics':['D','E','F'],
         'Chemistry':['G','H','I'],
         'Computing':['J','K','L']}
print("students in Computing:",classes['Computing'])
classes['Math'].append('ABC')
print("students in Maths:",classes["Math"])

#%%

addressbook={"Arham":{'address':'karachi','email':'arham@arham.com'},
             "Anum":{'address':'lahore','email':'anum@arham.com'},
             "Irfan":{'address':'islamabad','email':'irfan@arham.com'},}
print("Arham's information:",addressbook["Arham"])
print("Irfan's email:",addressbook["Irfan"]['email'])


