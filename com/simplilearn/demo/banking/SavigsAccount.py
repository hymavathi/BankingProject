'''
Created on Oct 8, 2022

@author: horugant
'''

from com.simplilearn.demo.banking.Account import Account



class SavigsAccount(Account):
    '''
    classdocs
    '''

    def __init__(self, accountID, custObj, balance, minBalance):
        '''
        Constructor
        '''
        super().__init__(accountID, custObj, balance)
        self.minBalance = float(minBalance)
        
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))

        if float(self.balance-amount) < self.minBalance:
            print('Your balance after the withdraw will be less than the set min balance required on this account. Please enter valid amount to withdraw')
            self.withdraw()
        else:
            super().withdraw(amount)
            
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        super().deposit(amount, 'true')
        
    def getSavingAccountInfo(self):
        super().getAccountInfo()
        print('min balance set on this account is' + str(self.minBalance))
            
        