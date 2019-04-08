# -*- coding: utf-8 -*-
from utility import DBConnectivity
#from exceptions import customExceptions
# =============================================================================
# import mysql.connector
# 
# connection = mysql.connector.connect(host='localhost',
#                              database='ses',
#                              user='root',
#                              password='root')
# 
# =============================================================================

# =============================================================================
# def slotDetails(ID):
#     
#     con = DBConnectivity2.create_connection()
#     cur = DBConnectivity2.create_cursor(con)
#     sql_statement = "select areaID,slot_num,reserve from parkingslottable where areaID=" + str(ID)
#     #user = {}
#     cur.execute(sql_statement)
#     result = cur.fetchall()
#     print(result)
# 
# =============================================================================
def slotDetails(ID):
    try:
      con = DBConnectivity.create_connection();
      cur = DBConnectivity.create_cursor(con);
      sql_statement = "select areaID,slot_num,status from parkingslottable where areaID= " + str(ID)
      cur.execute(sql_statement)
      result = cur.fetchall()
    #print(result)
      info = {}
      info_list = []
      for row in result:
          info = {
          'areaID':row[0],
          'slot_num':row[1],
          'status':row[2]
                }
      info_list.append(info)
      print(info)
      print(info_list)    
      return info_list
    except Exception as e:
        print(e);
    finally:
        cur.close();
        con.close();

def slotStatus(ID):
     try:
      con = DBConnectivity.create_connection();
      cur = DBConnectivity.create_cursor(con);
      sql_statement = "select status from parkingslottable where areaID='{}' ".format(ID)
      cur.execute(sql_statement)
      result = cur.fetchall()
      info_list = []
      for row in result:
          info_list.append(row[0])
          if(len(info_list)%5 ==0):
              info_list.append("\n")
      print(info_list)
      return "".join(info_list)
     except Exception as e:
        print(e);
     finally:
        cur.close();
        con.close();

def initSlots():
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        num_slots = [5,10,10,5,5,10]
        count = 0
        area = ['A','B','C','D','E','F']
        status = 'A'
        for i in range(len(area)):
            for j in range(num_slots[i]):
                sql_statement = "insert into parkingslottable values({},'{}',{},'{}')".format(count,area[i],j,status)
                count+=1
                print(count)
                cur.execute(sql_statement)
                con.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close();
        con.close();
  
def parkDetails(ID):
    try:
      con = DBConnectivity.create_connection();
      cur = DBConnectivity.create_cursor(con);
      sql_statement = "select areaID , capacity from parkingAreaTable where areaID="+ str(ID)
      cur.execute(sql_statement)
      result = cur.fetchall()
      info ={}
      for row in result:
        info = {
          'areaID':row[0],
          'capacity':row[1],
                }
      print(info)
      return info
    except Exception as e:
        print(e);
    finally:
        cur.close();
        con.close();
#parkDetails("'A'")   
#slotDetails("'A'")
        
