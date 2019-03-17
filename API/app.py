from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/serverTest')
def checkServer():
	return "Server Up and Running";

if __name__ == "__main__":
	app.run(port = "6001", debug = True)