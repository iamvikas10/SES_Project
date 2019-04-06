from database.viewUpdateDB import user_details
import jwt

#return the details of user in the form of dictionary
def get_user_details(phoneNo):
	user = user_details(phoneNo);
	return user;

#function for authorization
def authorization(token):
	resp_body = {
		'isAuthenticated':True,
		'msg':'User is Authenticated'	
	}
	try:
		decoded_token = decode_token(token)
		user_details = get_user_details(decoded_token['mobileNo'])
		return resp_body

	except Exception as e:
		resp_body['isAuthenticated'] = False;
		resp_body['msg']='User is not Authenticated'
		return resp_body

#function for decoding token
def decode_token(token):
	secret_key = 'SESProject';
	decoded_token = jwt.decode(token,secret_key, algorithms = 'HS256')
	return decoded_token
