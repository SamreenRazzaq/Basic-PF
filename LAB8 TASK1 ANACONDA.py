print ("lab 8 task 1")
def add_lists (a, b):
    print("Enter two lists of same size")
    L = eval(input("Enter first list(L): "))
    M = eval(input("Enter second list(M): "))
    N = []

    for i in range(len(L)):
        N.append(L[i] + M[i])

    print("List N:")
    return N
x=''
y=''
print(add_lists(x,y))

