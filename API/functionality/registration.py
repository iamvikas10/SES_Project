'''
Created on Mar 18, 2019

@author: iamvikas10
'''
from validations import regValidations
from classes.user import User;
from database import viewUpdateDB
from exceptions import customExceptions;
import base64;

#function for user_registration
def user_registration(name, phoneNo, email, password):
    usr=User();
    body_message = {
        'isError':False,
        'msg':'User Successfully Registered'
    }
    usr.set_name(name);
    usr.set_phoneNo(int(phoneNo));
    validateEmail = regValidations.is_user_present(phoneNo);
   # print(validateEmail)
    if(validateEmail == True):
        usr.set_email(email);
    else:
        body_message['isError'] = True;
        body_message['msg'] = 'User Already Registered. Kindly login'
    pwd = str(user_encode_password(password));
    usr.set_password(str(pwd));
    print(type(usr.get_password()))
    if(body_message['isError']==False):
        updateDB=viewUpdateDB.update_tableUser(usr)
    return body_message;

#function for base64 encryption of password
def user_encode_password(password):
    password = password.encode()
    return base64.b64encode(password);

#function for base64 decryption of password
def user_decode_password(password):
    return base64.b64decode(password);
