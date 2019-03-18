from utility import DBConnectivity
from exceptions import customExceptions
from classes.user import User

def update_tableUser(user):
	try:
		con = DBConnectivity.createConnection();
		cur = DBConnectivity.createCursor(con);
		temp = "vikas"
		sql_insert_query = """Insert Into user(`username`,`name`,`phone_no`,`email`,
		`password`) values ('%s','%s','%s','%s','%s')""" % (user.get_userName(), 
			user.get_name(), user.get_phoneNo(), user.get_email(),user.get_password())
		cur.execute(sql_insert_query);
		con.commit();
		return True;
	except customExceptions.DataNotUpdated as e:
		print(e);
	finally:
		cur.close();
		con.close();