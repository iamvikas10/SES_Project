from utility import DBConnectivity

def history_module():
    con = DBConnectivity.create_connection();
    cur = DBConnectivity.create_cursor(con);
    fetch = cur.execute("select * from Booking_History")

    fetchall = [dict((cur.description[i][0], value) \
                     for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    return fetchall;