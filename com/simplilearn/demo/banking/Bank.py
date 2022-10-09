'''
Created on Oct 8, 2022

@author: horuganti
'''

class Bank:

    def __init__(self, ifsc_code, bank_name, branch_name, loc):
        '''
        Constructor Initializes values
        '''
        self.ifsc_code = ifsc_code
        self.bank_name = bank_name
        self.branch_name = branch_name
        self.loc = loc
    
    #Prints Bank Details
    def printAccountInfo(self):
        print("ifsc code is " + self.ifsc_code)
        print("Bank Name is " + self.bank_name)
        print("Branch Name is " + self.branch_name)
        print("loc Name is " + self.loc)

            