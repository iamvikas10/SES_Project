from validations.loginValidations import have_user_registered
from utility import DBConnectivity

#function for getting password of a particular user
def get_password(mobile_number):
    con = DBConnectivity.create_connection()
    db_cursor =  DBConnectivity.create_cursor(con)
    try:
        if have_user_registered(mobile_number):
            sql_statement = "select password from user where phoneNo=" + str(mobile_number)
            db_cursor.execute(sql_statement)
            for row in db_cursor:
                db_cursor.close()
                con.close()
                #print(row[0])
                return row[0]
    except Exception as e:
        print(e)
        db_cursor.close()
        con.close()
        return None