'''
Created on Oct 8, 2022

@author: horugant
'''
from com.simplilearn.demo.banking.Customer import Customer
from com.simplilearn.demo.banking.SavigsAccount import SavigsAccount

class BankingOps():
    '''
    classdocs
    '''
    def __init__(self):
        self.customer = Customer('1', 'Hyma Oruganti', '191 Annabelle Branch', '9808334990' )
        self.sAccount = SavigsAccount('11223334444455', self.customer, 10000, 100 )
        
    def doOperation(self, opId):
        match opId:
            case 1: 
                self.sAccount.getAccountInfo()
            case 2:
                self.sAccount.getBalance()
            case 3:
                self.sAccount.deposit()
            case 4: 
                self.sAccount.withdraw()
            case -1:
                print('exiting. Rerun the program for doing transactions')
                exit()

    
opId = 0
print('Wleocme to ICICI Bank. What do you want to Perform from the following Operations?')
print('1.Get Account Info 2.Get Balance 3.Deposit 4.Withdraw -1:Exit')
ops = BankingOps()

while opId >= 0 : 
    opId = int(input("Enter the number of operationId you want to perform: "))
    ops.doOperation(opId)
           

