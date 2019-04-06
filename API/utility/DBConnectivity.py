'''
Created Mar 18, 2019

@author: iamvikas10

'''

import mysql.connector
from mysql.connector import Error
def create_connection():
	try:
		connection = mysql.connector.connect(host='localhost',
                             database='ses',
                             user='root',
                             password='0nline@1234')
		print(connection);
		return connection;
	except Error as e :
	    print ("Error while connecting to MySQL", e)

def create_cursor(con):
	try:
		cursor = con.cursor();
		return cursor;
	except Error as e:
		print("Error While Connecting to MySQL", e)

