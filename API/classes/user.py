'''
Created on Mar 18, 2019

@author : iamvikas10

'''

class User:
	def __init__(self):
		self.__userName = None;
		self.__name = None;
		self.__phoneNo = None;
		self.__email = None;
		self.__password = None;
		self.__confirmPassword = None;

	def get_userName(self):
		return self.__userName; 
	def set_userName(self, value):
		self.__userName = value;

	def get_name(self):
		return self.__name;
	def set_name(self, value):
		self.__name = value;

	def get_phoneNo(self):
		return self.__phoneNo;
	def set_phoneNo(self, value):
		self.__phoneNo = value;

	def get_email(self):
		return self.__email;
	def set_email(self, value):
		self.__email = value;

	def get_password(self):
		return self.__password;
	def set_password(self, value):
		self.__password= value;

	def get_confirmPassword(self):
		return self.__confirmPassword;
	def set_confirmPassword(self, value):
		self.__confirmPassword = value;