'''
Created on Mar 18, 2019

@author: iamvikas10
'''
from classes.user import User 
from exceptions import customExceptions
import re
from utility import DBConnectivity

#function to check weather user is present or not
def is_user_present(phoneNo):
    con = DBConnectivity.create_connection();
    cur = DBConnectivity.create_cursor(con);
    boolEmail = False;
    sql_statement = "select count(*) from user where phoneNo =" + str(phoneNo);
    cur.execute(sql_statement)
    for count in cur:
        #print(count[0])
        if count[0] ==  0:
            #print("hiiiii")
            cur.close()
            boolEmail = True;
            break;
    cur.close()
    #print(boolEmail)
    return boolEmail;

