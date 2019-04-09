import jwt
from validations.loginValidations import have_user_registered
from functionality import registration
from database import loginDatabase


#function to check weather login password entered by the user is correct
def is_login_password_correct(mobile_number,password):
	pwd = str(registration.user_encode_password(password));
	#print(loginDatabase.get_password(mobile_number))
	if(loginDatabase.get_password(mobile_number) == pwd):
		print("i am here")
		return True
	else:
		return False

def login_module(mobileNo, password):
	body_response = {
		'isError':False,
		'msg':"User Login Successfully"
	}

	check_user_registered = have_user_registered(mobileNo);
	print(check_user_registered);
	if(check_user_registered):
		if(is_login_password_correct(mobileNo, password)):
			return body_response;
		else:
			body_response['isError']=True;
			body_response['msg']='Your password is incorrect. Please login Again'
			return body_response
	else:
		body_response['isError']=True;
		body_response['msg']='You have not registered'
		return body_response
