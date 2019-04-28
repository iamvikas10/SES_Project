# -*- coding: utf-8 -*-
from utility import DBConnectivity
from exceptions import customExceptions

def updateCarDetails(phoneNo,rcNo,carModel):
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        sql = "insert into car_details(phoneNo,rcNo,carModel) values('{}','{}','{}')".format(phoneNo,rcNo,carModel)
        cur.execute(sql)
        con.commit();
        return True;
    except customExceptions.DataNotUpdated as e:
        print(e);
    finally:
        cur.close();
        con.close();

def editUpdateCarDetails(phoneNo,rcNo,carModel):
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        sql = "update car_details set rcNo='{}', carModel = '{}' where phoneNo = '{}';".format(rcNo,carModel,phoneNo)
        cur.execute(sql)
        con.commit();
        return True;
    except customExceptions.DataNotUpdated as e:
        print(e);
    finally:
        cur.close();
        con.close();
def reg_car_details(phoneNo):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        sql = "select rcNo , carModel from car_details where phoneNo = '{}'".format(phoneNo)
        cur.execute(sql)
        result = cur.fetchall()
        details = {}
        for row in result:
            details = {
                  'rcNo':row[0],
                  'carModel':row[1]
                  }
        return details
    except customExceptions.DataNotUpdated as e:
        print(e);
    finally:
        cur.close();
        con.close();

def getPhoneNumberThroughCar(rcNo):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        sql = "select phoneNo from car_details where rcNo = '{}'".format(rcNo)
        cur.execute(sql)
        result = cur.fetchall()
        details = {}
        for row in result:
            details = {
                  'phoneNo':row[0],
                  }
        return details['phoneNo']
    except customExceptions.DataNotUpdated as e:
        print(e);
    finally:
        cur.close();
        con.close();