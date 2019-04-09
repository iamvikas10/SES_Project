# -*- coding: utf-8 -*-
from utility import DBConnectivity
from exceptions import customExceptions
def currentbook_details(phoneNo):
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        sql = "select slotNo,ArrivalTime from prebooking_table where phoneNo ='{}'".format(phoneNo)
        cur.execute(sql)
        results = cur.fetchall()
        details = {}
        for row in results:
            details = {
                  'slotNo':row[0],
                  'timeOfParking':row[1]
                  }
        return details
    except customExceptions.DataNotUpdated as e:
        print(e);
    finally:
        cur.close();
        con.close();
