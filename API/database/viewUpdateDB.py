'''
Created Mar 18, 2019

@author: iamvikas10



from utility import DBConnectivity
from exceptions import customExceptions
from classes.user import User
from functionality.changeSlotStatus import changeSlotStatus


#This function is to insert the details of user into the SQL table.
def update_tableUser(user):
	try:
		con = DBConnectivity.create_connection();
		cur = DBConnectivity.create_cursor(con);
		sql_insert_query = """Insert Into user(`name`,`email`,`phoneNo`,
		`password`) values ('%s','%s','%s',"%s")""" % ( 
			user.get_name(), user.get_email(),user.get_phoneNo(), user.get_password())
		#print(sql_insert_query)
		cur.execute(sql_insert_query);
		con.commit();
		return True;
	except customExceptions.DataNotUpdated as e:
		print(e);
	finally:
		cur.close();
		con.close();

this function is to fetch the details of the user from the sql table.
   returns a dictonary containing user details

def user_details(phoneNo):
	try:
		con = DBConnectivity.create_connection();
		cur = DBConnectivity.create_cursor(con);
		sql_statement = "select * from user where phoneNo=" + str(phoneNo)
		#print(sql_insert_query)
		user = {}
		cur.execute(sql_statement);
		for row in cur:
			user = {
				'name':row[1],
				'email':row[2],
				'phoneNo':row[3]
			}
		return user;
	except Exception as e:
		print(e);
	finally:
		cur.close();
		con.close();
        
def arrivalTime(phoneNo):
	try:
		con = DBConnectivity.create_connection();
		cur = DBConnectivity.create_cursor(con);
		sql_statement = "select arrivalTime from booking where phoneNo=" + str(phoneNo)
		#print(sql_insert_query)
		arrivalTime = {}
		cur.execute(sql_statement);
		for row in cur:
			arrivalTime = {
				'arrivalTime':row[0],
			       }
		return arrivalTime;
	except Exception as e:
		print(e);
	finally:
		cur.close();
		con.close();       
        
        
        
def update_tableBooking(arrivalTime, phoneNo ):
	try:
		con = DBConnectivity.create_connection();
		cur = DBConnectivity.create_cursor(con);
		sql_update_query = "update booking set arrivalTime='{}' where phoneNo='{}'".format(arrivalTime, phoneNo)
		#print(sql_insert_query)
		cur.execute(sql_update_query);
		con.commit();
		return True;
	except customExceptions.DataNotUpdated as e:
		print(e);
	finally:
		cur.close();
		con.close();
        
        
def update_tableBookingExit(exitTime, phoneNo,completeStatus,amount):
	try:
		con = DBConnectivity.create_connection();
		cur = DBConnectivity.create_cursor(con);
		sql_select_query = "select areaId, slotNo from Booking where phoneNo='{}'".format(phoneNo)
		cur.execute(sql_select_query)
		for row in cur:
			areaId = row[0],
			slotNo = row[1]
			slotStatus = "A"
			isChange = changeSlotStatus(areaId, slotNo, slotStatus)
			if(isChange):
				print("Changing slot number of "+ areaId + " "+ slotNo+" to "+ slotStatus)
		sql_update_query = "update booking set exitTime='{}',completeStatus={},\
				amount={} where phoneNo='{}'".format(exitTime,completeStatus,amount, phoneNo)
		#print(sql_insert_query)
		cur.execute(sql_update_query);
		con.commit();
		return True;
	except customExceptions.DataNotUpdated as e:
		print(e);
	finally:
		cur.close();
		con.close();        
        
def update_parkingSlotTable(areaID, slotNumber, slotStatus):
	try:
		con = DBConnectivity.create_connection();
		cur = DBConnectivity.create_cursor(con);
		sql_update_query = "update parkingSlotTable set status = '{}' \
			where areaID = '{}' and slot_num = '{}'".format(slotStatus,areaID,slotNumber)
		cur.execute(sql_update_query)
		con.commit()
		return True
	except Exception as e:
		print(e)
	finally:
		cur.close()
		con.close()      
        '''