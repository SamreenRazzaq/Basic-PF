#### QUESTION 1 #####
#%%
def farrange(word):
    finaloutput = ''
    j = 0
    for i in word:
        if j%2 == 0:
            finaloutput = finaloutput + i.upper()
        else:
            finaloutput = finaloutput + i.lower()
        j = j + 1
    return finaloutput
print(farrange("abcdef"))

#### QUESTION 2 ####
#%%
list = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(list, key=sum))