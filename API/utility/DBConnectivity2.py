# -*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import Error

#function for creating connection to database.
def create_connection():
	try:
		connection = mysql.connector.connect(host='localhost',
                             database='ses',
                             user='root',
                             password='root')
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


