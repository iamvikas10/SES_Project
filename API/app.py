from flask import Flask
from flask import request, jsonify,Response
from flask import render_template
from functionality.registration import user_registration
from functionality.login import login_module
from functionality import authentication
from database import viewUpdateDB
import jwt

def createApp():

	app = Flask(__name__)   #app initialization

	@app.route('/serverTest')
	def checkServer():
		return "Server Up and Running";
		
	#api for registration part
	@app.route('/registration', methods = ['POST'])
	def registration():
		name = request.json['name'];
		phoneNo = request.json['phoneNo'];
		email = request.json['email'];
		password = request.json['password'];
		respData = user_registration(name, phoneNo, email, password);
		return jsonify(respData), 200;
	''' 
		login api: Please refer to doc for endpoints
		jsonify : for making response object
		encode: mobileNo is the payload passed on which secret key works
	'''
	@app.route('/login', methods = ['POST'])
	def login():
		phoneNo = request.json['phoneNo'];
		password = request.json['password'];
		respData = login_module(phoneNo,password);
		print(respData)
		if(respData['isError']==False):
			user = viewUpdateDB.user_details(phoneNo)
			secret_key = 'SESProject';
			token = jwt.encode({'mobileNo':phoneNo},secret_key, algorithm = 'HS256');
			resp = jsonify(respData)
			resp.headers['Authorization']=token;
		return resp,200;

	#just for checking we dont need this in any of the screens
	@app.route('/userDetails',methods = ['POST']) 
	def user_details():
		phoneNo = request.json['phoneNo']
		respData = authentication.get_user_details(phoneNo);
		resp = jsonify(respData)
		return resp,200;

	#api for authorization
	@app.route('/authorization', methods =['POST'])
	def authorize_user():
		token = request.headers['Authorization'][7:]
		auth = authentication.authorization(token);
		return jsonify(auth);	
	return app;

