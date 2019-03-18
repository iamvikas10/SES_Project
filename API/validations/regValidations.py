'''
Created on Mar 18, 2019

@author: iamvikas10
'''
from classes.user import User 
from exceptions import customExceptions
import re
def validate_phoneNo(user):
    if(len(str(user.get_phoneNo()))!=10):
        raise customExceptions.InvalidMobileNumberException();
    elif(len(str(user.get_phoneNo()))==10):
        mob_no=str(user.get_phoneNo());
        if(not mob_no.isnumeric()):
            raise customExceptions.InvalidMobileNumberException();
    return True;
def validate_password(user):
    if(len(user.get_password())<6 or len(user.get_password())>10):
        raise customExceptions.InvalidPasswordException();
    elif(len(user.get_password())>=6 and len(user.get_password())<=10):
        flag=0;
        if((re.search(r'\@',user.get_password()) or re.search(r"\.",user.get_password()) or re.search(r"\#",user.get_password())) and (re.search(r"\d*",user.get_password()))):
            pwd=user.get_password();
            for i in pwd:
                if(str(i).islower()):
                    count=1;
            if(count==1):
                for j in pwd:
                    if(str(j).isupper()):
                        count=2;
            if(count==2):
                flag=0;
        else:
            flag=flag+1;
        if(flag!=0):
            raise customExceptions.InvalidPasswordException();
    return True;
        
def validate_confirmPassword(user):
    if(user.get_password() != user.get_confirmPassword()):
        raise customExceptions.InvalidConfirmPasswordException();
    return True;

def validate_userName(user):
    return True;

def validate_name(user):
    return True;

def validate_email(user):
    return True;
