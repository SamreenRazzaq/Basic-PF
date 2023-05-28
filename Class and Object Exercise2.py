class BankAccount: 
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def Deposit(self , d ):
        self.balance = self.balance + d
    def Withdrawal(self , w):
        if(self.balance < w):
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w
    def bankFees(self):
        self.balance = (95/100)*self.balance
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance )        
newAccount = BankAccount(123456789, "abc" , 100000 )
newAccount.Withdrawal(300)
newAccount.Deposit(200)
newAccount.display()

#%%

class Computation:
    def _init_ (self):
        pass
    def factorial(self, n):
        j = 1
        for i in range (1, n + 1):
            j = j * i
        return j
    def sum (self, n):
        j = 1
        for i in range (1, n + 1):
            j = j + i
        return j
    def testPrim (self, n):
        j = 0
        for i in range (1, n + 1):
            if (n% i == 0):
                j = j + 1
        if (j == 2):
            return True
        else:
            return False
    def testprims (self, n, m):
        commonDiv = 0
        for i in range (1, n + 1):
            if (n% i == 0 and m% i == 0):
                commonDiv = commonDiv + 1
        if commonDiv == 1:
            print ("The numbers", n, "and", m, "are co-primes")
        else:
            print ("The numbers", n, "and", m, "are not co-primes")
    def tableMult (self, k):
        for i in range (1,10):
            print (i, "x", k, "=", i * k)
    def allTables (self):
        for k in range (1,10):
            print ("\nthe multiplication table of:", k, "is:")
            for i in range (1,10):
                print (i, "x", k, "=", i * k)
    def listDiv (self, n):
        lDiv = []
        for i in range (1, n + 1):
            if (n% i == 0):
                lDiv.append (i)
        return lDiv
    def listDivPrim (self, n):
        lDiv = []
        for i in range (1, n + 1):
            if (n% i == 0 and self.testPrim (i)):
                lDiv.append (i)
        return lDiv
Comput= Computation ()
Comput.testprims (13, 7)
print ("List of divisors of 18:", Comput.listDiv (18))
print ("List of prime divisors of 18:", Comput.listDivPrim (18))
Comput.allTables ()