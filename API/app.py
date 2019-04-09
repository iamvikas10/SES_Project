from flask import Flask
from flask import request, jsonify,Response,json
from flask import render_template
import datetime
from functionality.registration import user_registration
from functionality.login import login_module
from functionality import parkingmap
from functionality import currentbooking
from functionality import authentication
from functionality import cars_details
from database import Prebooking_insert

from database import viewUpdateDB, parkingDatabase

import jwt
from functionality.home import home_module
from functionality.Prebooking import Prebooking_module
from functionality.Booking_history import history_module


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
        resp = jsonify(respData)
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
    #for parking area screens
    @app.route('/home', methods=['GET'])
    def home():
        resp = {
            "isError":True,
            "msg":"You are not authorized to view"
        }
        token = request.headers['Authorization'][7:]
        var = authentication.authorization(token);
        if(var['isAuthenticated']==True):
            respData = home_module();
            return json.dumps(respData), 200
        else:
            return jsonify(resp), 200

    # for prebooking
    @app.route('/prebooking', methods=['POST'])
    def prebooking():
        resp= {
            "isError": True,
            "msg": "You are not authorized to view"
        }
        slotNo = request.json['slotNo'];

        rcNo = request.json['rcNo']
        ExpectedArrivalTime = request.json['ExpectedArrivalTime'];
        ArrivalTime = request.json['ArrivalTime'];
        bookingStatus = ""
        AreaId = request.json['AreaId']
        expectedTime = datetime.datetime.strptime(ExpectedArrivalTime, '%Y-%m-%d %H:%M:%S')
        Time_Arrived = datetime.datetime.strptime(ArrivalTime, '%Y-%m-%d %H:%M:%S')
        print(Time_Arrived)
        d = Time_Arrived - expectedTime
        if d.seconds >= 600:
            bookingStatus = "NO"
        else:
            bookingStatus = "YES"
        token = request.headers['Authorization'][7:]
        var = authentication.authorization(token);
        if (var['isAuthenticated'] == True):
            user_details=authentication.get_user_details_through_token(token)
            phoneNo = user_details['phoneNo'];
            respData = Prebooking_module(slotNo, phoneNo, rcNo, ExpectedArrivalTime, ArrivalTime, bookingStatus,AreaId);
            return jsonify(respData), 200;

        else:
            return jsonify(resp), 200

    @app.route('/currentbooking',methods=['GET'])
    def current_booking():
        resp= {
            "isError": True,
            "msg": "You are not authorized to view"
        }
        token = request.headers['Authorization'][7:]
        var = authentication.authorization(token);
        if (var['isAuthenticated'] == True):
            user_details=authentication.get_user_details_through_token(token)
            phoneNo = user_details['phoneNo'];
            respData = currentbooking.currentbookingdetails(phoneNo)
            return jsonify(respData) , 200
        else:
          return jsonify(resp), 200
   
    
    @app.route('/cardetails',methods=['POST','GET'])
    def car_details():
        if request.method == 'POST':
             resp= {
            "isError": True,
            "msg": "You are not authorized to view"
             }
             rcNo = request.json['rcNo']
             carModel = request.json['carModel']
             token = request.headers['Authorization'][7:]
             var = authentication.authorization(token);
             if (var['isAuthenticated'] == True):
                 user_details=authentication.get_user_details_through_token(token)
                 phoneNo = user_details['phoneNo'];
                 checkCarExists = cars_details.get_car_details(phoneNo)
                 #print(checkCarExists)
                 if(len(checkCarExists.keys())==0):
                     print("Debugging addinng first car")
                     respData = cars_details.car_details_func(phoneNo,rcNo,carModel)
                     return jsonify(respData) , 200
                 else:
                     print("Debugging updating car")
                     respData = cars_details.edit_car_details(phoneNo,rcNo,carModel)
                     return jsonify(respData) , 200
             else:
                 return jsonify(resp), 200
        elif request.method == 'GET':
             resp= {
            "isError": True,
            "msg": "You are not authorized to view"
             }
             token = request.headers['Authorization'][7:]
             var = authentication.authorization(token);
             if (var['isAuthenticated'] == True):
                 user_details=authentication.get_user_details_through_token(token)
                 phoneNo = user_details['phoneNo'];
                 respData = cars_details.get_car_details(phoneNo)
                 print(len(respData.keys()))
                 return jsonify(respData) , 200
             else:
                 return jsonify(resp) , 200
        
    
    #just for initializing 
    @app.route('/initialize',methods=['POST'])
    def init_parkingSlots():
        parkingDatabase.initSlots();
        return "Success Init", 200

    #api for authorization
    @app.route('/authorization', methods =['POST'])
    def authorize_user():
        token = request.headers['Authorization'][7:]
        auth = authentication.authorization(token);
        return jsonify(auth);    
    
    
    @app.route('/parkingMap',methods = ['GET']) 
    def parking_map():
      areaID  = request.json['areaID']
      #slot_num = request.json['slot_num']
      resp1 = {
            "isError": True,
            "msg": "You are not authorized to view"
        }
      token = request.headers['Authorization'][7:]
      var = authentication.authorization(token);
      if (var['isAuthenticated'] == True):
          area_slot_status = parkingmap.getAreaStatus(areaID)
          resp = jsonify(area_slot_status)
          return resp ,200
      else:
          return jsonify(resp1), 200
    return app;   


    @app.route('/Booking_history', methods=['GET'])
    def Booking_History():
        resp = {
            "isError": True,
            "msg": "You are not authorized to view"
        }
        token = request.headers['Authorization'][7:]
        var = authentication.authorization(token);
        if (var['isAuthenticated'] == True):
            respData = history_module();
            return json.dumps(respData), 200
        else:
            return jsonify(resp), 200



    #





