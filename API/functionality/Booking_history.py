from utility import DBConnectivity

def history_module(phoneNo):
    con = DBConnectivity.create_connection();
    cur = DBConnectivity.create_cursor(con);
    print(phoneNo)
    sql= "select areaId,slotNo,arrivalTime,exitTime,amount from booking where completeStatus=1 and phoneNo='{}'".format(phoneNo)
    cur.execute(sql)

    fetchall = [dict((cur.description[i][0], value) \
                     for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    return fetchall;