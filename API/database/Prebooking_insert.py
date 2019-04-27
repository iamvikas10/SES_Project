from utility import DBConnectivity
from exceptions import customExceptions
from classes.prebooking import Prebooking


#This function is to insert the details of prebooking into the SQL table.
def update_tablePrebook(Prebooking):

	try:
		con = DBConnectivity.create_connection();
		cur = DBConnectivity.create_cursor(con);
		print(Prebooking.get_ExpectedArrival())
		sql_insert_query = """Insert Into Prebooking_Table(`slotNo`,`phoneNO`,`expectedArrivalTime`,`rcNo`,`ArrivalTime`,`bookingStatus`,`AreaId`
		) values ('%s','%s',"%s",'%s',"%s",'%s','%s')""" % (
			Prebooking.get_slotNo(), Prebooking.get_phoneNo(),Prebooking.get_ExpectedArrival(),Prebooking.get_rcNo(), Prebooking.get_ExactArrival(),Prebooking.get_bookingStatus(),Prebooking.get_AreaId())
		#print(sql_insert_query)
		sql_insert_query_currentBooking = """Insert Into Current_booking(`slotNo`,`phoneNO`,`rcNo`,`ArrivalTime`,`BookingStatus`,`AreaId`
				) values ('%s','%s',"%s",'%s',"%s",'%s')""" % (Prebooking.get_slotNo(), Prebooking.get_phoneNo(), Prebooking.get_rcNo(),
			Prebooking.get_ExactArrival(), Prebooking.get_bookingStatus(), Prebooking.get_AreaId())
		# print(sql_insert_query)
		cur.execute(sql_insert_query);
		cur.execute(sql_insert_query_currentBooking);
		con.commit();
		return True;
	except customExceptions.DataNotUpdated as e:
		print(e);
	finally:
		cur.close();
		con.close();

'''this function is to fetch the details of the user from the sql table.
   returns a dictonary containing user details
'''
def book_details(phoneNo):
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        sql = "select rcNo , preBookingStatus from booking where phoneNo ='{}'".format(phoneNo)
        cur.execute(sql)
        results = cur.fetchall()
        details = {}
        for row in results:
            details = {
                  'rcNo':row[0],
                  'preBookingStatus':row[1]
                  }
        return details
    except customExceptions.DataNotUpdated as e:
        print(e);
    finally:
        cur.close();
        con.close();





# =============================================================================
# def currentbook_details(phoneNo):
#     try:
#         con = DBConnectivity.create_connection();
#         cur = DBConnectivity.create_cursor(con);
#         sql = "select slotNo,ArrivalTime from prebooking_table where phoneNo ='{}'".format(phoneNo)
#         cur.execute(sql)
#         results = cur.fetchall()
#         details = {}
#         for row in results:
#             details = {
#                   'slotNo':row[0],
#                   'timeOfParking':row[1]
#                   }
#         return details
#     except customExceptions.DataNotUpdated as e:
#         print(e);
#     finally:
#         cur.close();
#         con.close();
# =============================================================================

# def prebook_Details(phoneNo):
#     try:
#         con = DBConnectivity.create_connection();
#         cur = DBConnectivity.create_cursor(con);
#         sql_statement = "select * from Prebooking_Table where phoneNo=" + str(phoneNo)
#         #print(sql_insert_query)
#         Prebook_User = {}
#         cur.execute(sql_statement);
#         for row in cur:
#             Prebook_User  = {
#                 'slotNo':row[1],
#                 'phoneNo':row[2],
#                 'expectedArrivalTime':row[3],
#                 'ArrivalTime':row[4],
#                 'bookingStatus':[5]
#             }
#         return Prebook_User
#
#
#     except Exception as e:
#         print(e)
#     finally:
#         cur.close();
#         con.close();