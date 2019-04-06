'''
Created on 4 April, 2019

@author: iamvikas10
'''
from classes.user import User
from utility import DBConnectivity

#function to check weather user have registered or not
def have_user_registered(phoneNo):
    con = DBConnectivity.create_connection();
    cur = DBConnectivity.create_cursor(con);
    bool_user_registered = True;
    sql_statement = "select count(*) from user where phoneNo =" + str(phoneNo);
    cur.execute(sql_statement)
    for count in cur:
        #print(count[0])
        if count[0] ==  0:
            #print("hiiiii")
            cur.close()
            bool_user_registered = False;
            break;
    cur.close()
    #print(boolEmail)
    return bool_user_registered;