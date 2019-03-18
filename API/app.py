from flask import Flask
from flask import request, jsonify
from flask import render_template
from functionality.registration import userRegistration


def createApp():

	app = Flask(__name__)   #app initialization

	@app.route('/serverTest')
	def checkServer():
		return "Server Up and Running";

	@app.route('/registration', methods = ['POST'])
	def registration():
		userName = request.form['userName'];
		name = request.form['name'];
		phoneNo = request.form['phoneNo'];
		email = request.form['email'];
		password = request.form['password'];
		confirmPassword = request.form['confirmPassword'];
		respData = userRegistration(userName, name, phoneNo, email, password, confirmPassword);
		return jsonify(respData), 200;

	return app;

