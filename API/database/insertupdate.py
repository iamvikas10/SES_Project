'''
Created Mar 18, 2019

@author: iamvikas10


from utility import DBConnectivity
from exceptions import customExceptions
from classes.user import User
from functionality.changeSlotStatus import changeSlotStatus'''

from utility import DBConnectivity
from classes.user import User
from exceptions import customExceptions
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
	except Exception as e:
		print(e);
	finally:
		cur.close();
		con.close();

'''this function is to fetch the details of the user from the sql table.
   returns a dictonary containing user details
'''
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
		sql_statement = "select arrivalTime,completeStatus from booking where phoneNo=" + str(phoneNo)
		#print(sql_insert_query)
		cur.execute(sql_statement);
		for row in cur:
			if(row[1] ==1):
				print(row[0])
				return row[0]
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
        
        
def update_tableBookingExit(exitTime, phoneNo,updateCompleteStatus,amount, completedStatus, preBookingStatus):
	try:
		con = DBConnectivity.create_connection();
		cur = DBConnectivity.create_cursor(con);

		sql_update_query = "update booking set exitTime='{}',completeStatus={},\
				amount={} where phoneNo='{}'and completeStatus='{}' and preBookingStatus={}\
					".format(exitTime,updateCompleteStatus,amount, phoneNo, completedStatus, preBookingStatus)
		#print(sql_insert_query)
		cur.execute(sql_update_query);
		con.commit();
		return True;
	except customExceptions.DataNotUpdated as e:
		print(e);
	finally:
		cur.close()
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

def update_parkingSlotByExitTime(exitTime, phoneNo):
	try:
		print(exitTime)
		con = DBConnectivity.create_connection()
		cur = DBConnectivity.create_cursor(con)
		sql_select_query = "Select slotNo, areaId from Booking where phoneNo='{}' and exitTime\
			='{}'".format(phoneNo, exitTime)
		cur.execute(sql_select_query)
		for row in cur:
			slotNo = row[0]
			areaId = row[1]
			slotStatus = "A"
			return changeSlotStatus(areaId, slotNo, slotStatus)

	except Exception as e:
		print(e)
	finally:
		cur.close()
		con.close()
def checkSlotAvailability(slotNo, areaID):
	try:
		con = DBConnectivity.create_connection()
		cur = DBConnectivity.create_cursor(con)
		sql_select_query = "Select status from parkingSlotTable where slot_num = {} and \
			areaID ='{}'".format(slotNo, areaID)
		cur.execute(sql_select_query)
		for row in cur:
			slotStatus = row[0]
			return slotStatus
	except Exception as e:
		print(e)
	finally:
		cur.close()
		con.close()
def getSlotAreaNumber(phoneNo):
	try:
		con = DBConnectivity.create_connection();
		cur = DBConnectivity.create_cursor(con);

		sql_statement = "select slotNo, areaId, preBookingStatus, completeStatus \
			from booking where phoneNo='{}'" + str(phoneNo)
		#print(sql_insert_query)
		cur.execute(sql_statement);
		dict_d = {
			"slotNo":1,
			"areaId":"",
			"isPreBooked":""
		}
		for row in cur:
			if(row[2] ==1 and row[3]==0):
				dict_d["slotNo"]=row[0]
				dict_d["areaId"]=row[1]
				dict_d["isPreBooked"] = "Y"
			elif(row[2]==0 and row[3]==1):
				dict_d["slotNo"]=row[0]
				dict_d["areaId"]=row[1]
				dict_d["isPreBooked"]="N"
		return dict_d
	except Exception as e:
		print(e);
	finally:
		cur.close();
		con.close();       
        