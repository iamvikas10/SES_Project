'''
Created on Mar 18, 2019

@author: iamvikas10
'''
from validations import regValidations
from classes.user import User;
from database import viewUpdateDB
from exceptions import customExceptions;


def userRegistration(userName, name, phoneNo, email, password, confirmPassword):
    usr=User();
    user = {'userName' : userName, 'name' : name, 'phoneNo' : phoneNo, 'email' : email}
    usr.set_userName(userName);
    usr.set_name(name);
    usr.set_phoneNo(phoneNo);
    usr.set_email(email);
    usr.set_password(password);
    usr.set_confirmPassword(confirmPassword);
    #is_data_valid=validate_methods.register_validations(a);
    try:
        if(regValidations.validate_userName(usr)):
            if(regValidations.validate_password(usr)):
                if(regValidations.validate_confirmPassword(usr)):
                    if(regValidations.validate_email(usr)):
                        if(regValidations.validate_phoneNo(usr)):
                            if(regValidations.validate_name(usr)):
                                updateDB=viewUpdateDB.update_tableUser(usr)
                                if(updateDB==True):
                                    return user;
                                else:
                                    return "Error in Validations"
                                        
    except customExceptions.InvalidConfirmPasswordException as e:
        print(e)
    except customExceptions.InvalidMobileNumberException as e:
        print(e)
    except customExceptions.InvalidPasswordException as e:
        print(e)
    