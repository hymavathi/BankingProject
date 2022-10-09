'''
Created on Oct 8, 2022

@author: horugant
'''

class Customer:
    '''
    classdocs
    '''

    def __init__(self, customer_id, custname, address, contact_details):
        '''
        initializes values
        '''
        self.customer_id = customer_id
        self.custname = custname
        self.address = address
        self.contact_details = contact_details
        
    #Prints Customer info 
    def printCustomerInfo(self):
        print("CustomerName is " + self.custname)
        print("address is " + self.address)
        print("contact details are" + self.contact_details)
        
        
        