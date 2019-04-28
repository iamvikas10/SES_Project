# -*- coding: utf-8 -*-
from utility import DBConnectivity
from exceptions import customExceptions
from functionality.changeSlotStatus import changeSlotStatus
def currentbook_details(phoneNo):
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        sql = "select slotNo,ArrivalTime, preBookingStatus, completeStatus, areaId from Booking where phoneNo ='{}'".format(phoneNo)
        cur.execute(sql)
        results = cur.fetchall()
        details = {}
        for row in results:
            #print(row[0])
            if(row[2]==0 and row[3]==0):
                details = {
                    'slotNo':row[0],
                    'timeOfParking':row[1]
                }
                slotNo = row[0]
                areaId = row[4]
                slotStatus = "U"
                
                changeSlotStatus(areaId, slotNo,slotStatus)
                #if(changeSlotStatus):
                #    print("changing slot of "+ areaId + " " + slotNo+ "to "+ slotStatus)

        return details
    except customExceptions.DataNotUpdated as e:
        print(e);
    finally:
        cur.close();
        con.close();
