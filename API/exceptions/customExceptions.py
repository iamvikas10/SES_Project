'''
Created on Mar 18, 2019

@author: iamvikas10
'''
      
        
class InvalidPasswordException(Exception):
    def __init__(self):
        super().__init__("The password is invalid")

class InvalidMobileNumberException(Exception):
    def __init__(self):
        super().__init__("Invalid Mobile Number")
        
class InvalidConfirmPasswordException(Exception):
    def __init__(self):
        super().__init__("Password and Confirm Password do not match")  

class DataNotUpdated(Exception):
	def __init__(self):
		super().__init__("Data not updated to database")        
        
