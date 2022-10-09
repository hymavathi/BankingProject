'''
Created on Oct 8, 2022

@author: horugant
'''
from com.simplilearn.demo.banking.Bank import Bank

class Account(Bank):
    '''
    classdocs
    '''
    
    def __init__(self, accountID, custObj, balance):
        '''
        Constructor
        '''
        super().__init__('1234','icici','mmtc','vz')
        self.accountID = accountID
        self.custObj = custObj
        self.balance = balance

    def getAccountInfo(self):
        print("accountID is " + self.accountID)
        print("balance is " + str(self.balance))
        self.custObj.printCustomerInfo()
        super().printAccountInfo()
        
                
    # not sure what this third arg (true) supposed to do in the requirement description
    def deposit(self, amount, printRecpt):
        amount = float(amount)
        self.balance += amount
        if printRecpt == 'true':
            print('You have deposited ' + str(amount) + ' into your account. Your account balance is ' + str(self.balance))

    
    def withdraw(self, amount):
        if (float(amount) > float(self.balance)):
            print('Your available balance is less than the amount you want to withdraw.Kindy provide a valid amount to withdraw')
        else:
            self.balance -= amount           
            print('You have withdrawn ' + str(amount) + ' from your account. Your account balance is ' + str(self.balance))

            
    def getBalance(self):
        print( 'Your account balance is ' + str(self.balance))
        
        
# call the program with inputs
# customer = Customer('1', 'Hyma Oruganti', '191 Annabelle Branch', '9808334990' )
# account = Account('112233445566', customer, 100000)
#
# account.deposit(2000,'true')
# account.withdraw(500)
# account.getBalance()
# account.getAccountInfo()
        