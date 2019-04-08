'''
Created Mar 18, 2019

@author: iamvikas10

'''

import mysql.connector
from mysql.connector import Error

#function for creating connection to database.
def create_connection():
	try:
		connection = mysql.connector.connect(host='localhost',
                             database='ses',
                             user='root',
<<<<<<< HEAD
                             password='')
=======
                             password='root')
>>>>>>> 39fc74b772071d80bbca7b9acc47fa376ee9459a
		print(connection);
		return connection;
	except Error as e :
	    print ("Error while connecting to MySQL", e)

#function for creating cursor
def create_cursor(con):
	try:
		cursor = con.cursor();
		return cursor;
	except Error as e:
		print("Error While Connecting to MySQL", e)

