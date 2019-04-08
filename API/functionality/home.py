from utility import DBConnectivity

def home_module():
    con = DBConnectivity.create_connection();
    cur = DBConnectivity.create_cursor(con);
    fetch = cur.execute("select * from ParkingArea_Table")

    fetchall = [dict((cur.description[i][0], value) \
                     for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    return fetchall;