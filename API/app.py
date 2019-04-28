from flask import Flask
import requests
from database.insertupdate import arrivalTime
from database.cardDetailsDB import reg_car_details
from flask import request, jsonify,Response,json
from flask import render_template
from functionality import slotBooking
import datetime,time
from functionality.registration import user_registration
from functionality.login import login_module
from functionality import parkingmap
from functionality import currentbooking
from functionality import authentication
from database import insertupdate,cardDetailsDB
from database import Prebooking_insert
from functionality import cars_details
from functionality import exitParking
from database import insertupdate, parkingDatabase,Prebooking_insert
import urllib
import jwt
from functionality.home import home_module
from functionality.Prebooking import Prebooking_module
from functionality.Booking_history import history_module
from functionality.slotBooking import getCurrentTime
from functionality.changeSlotStatus import changeSlotStatus
from database.insertupdate import checkSlotAvailability


def createApp():

    app = Flask(__name__)   #app initialization    

    @app.route('/serverTest')
    def checkServer():
        return "Server Up and Running";
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
    @app.route('/preBooking', methods=['POST'])
    def prebooking():
        resp= {
            "isError": True,
            "msg": "You are not authorized to view"
        }
        AreaId = request.json['areaID'];
        slotNo = request.json['slotNo'];

        #det = request.json['rcNo']
        ExpectedArrivalTime = request.json['expectedArrival'];
        #ArrivalTime = request.json['ArrivalTime'];
        bookingStatus = ""
        #print(ExpectedArrivalTime)
        expectedTime = datetime.datetime.strptime(ExpectedArrivalTime, '%Y-%m-%d %H:%M')
        #Time_Arrived = datetime.datetime.strptime(ArrivalTime, '%Y-%m-%d %H:%M:%S')
        slotStatus = "R"
        changeSlotStatus(AreaId, slotNo, slotStatus)
        time2 = time.time()
        print(time2)
        #time2 = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
        st = datetime.datetime.fromtimestamp(time2).strftime('%Y-%m-%d %H:%M')
        print(st)
        #d = expectedTime - time2
        #seconds = d.seconds
# =============================================================================
#         if d.seconds >= 600:
#             bookingStatus = "NO"
#         else:
#             bookingStatus = "YES"
# =============================================================================
        token = request.headers['Authorization'][7:]
        var = authentication.authorization(token);
        if (var['isAuthenticated'] == True):
            user_details=authentication.get_user_details_through_token(token)
            phoneNo = user_details['phoneNo'];
            details = reg_car_details(phoneNo)
            rcNo = details["rcNo"]
            bookingStatus = 1
            respData = Prebooking_module(slotNo, phoneNo, rcNo, ExpectedArrivalTime,bookingStatus,AreaId);
            return jsonify(respData),200

    def sleepingFunction():
        pass            
    '''time.sleep(180+seconds)
            arrivTime=arrivalTime(phoneNo)
            ArrivalTime = arrivTime["arrivalTime"]
            if ArrivalTime is None:
                Prebooking_insert.updateBookingStatus(phoneNo)
                slotStatus = "A"
                changeSlotStatus(AreaId, slotNo, slotStatus)
                return jsonify(respData), 200;

        else:
            return jsonify(resp), 200'''
   
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
            secret_key = 'SESProject';
            token = jwt.encode({'mobileNo':phoneNo},secret_key, algorithm = 'HS256');
            resp = jsonify(respData)
            resp.headers['Authorization']=token;
            return resp,200;
        return jsonify(respData),200;

    #just for checking we dont need this in any of the screens
    @app.route('/userDetails',methods = ['POST']) 
    def user_details():
        phoneNo = request.json['phoneNo']
        respData = authentication.get_user_details(phoneNo);
        resp = jsonify(respData)
        return resp,200;

    @app.route('/currentBooking',methods=['GET'])
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
   
    
    @app.route('/carDetails',methods=['POST','GET'])
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
             carRespDetails ={
                     "rcNo":None,
                     "carModel": None
             }
             token = request.headers['Authorization'][7:]
             var = authentication.authorization(token);
             if (var['isAuthenticated'] == True):
                 user_details=authentication.get_user_details_through_token(token)
                 phoneNo = user_details['phoneNo'];
                 respData = cars_details.get_car_details(phoneNo)
                 if(len(respData.keys())==0):
                     return jsonify(carRespDetails), 200
                 else:
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

    @app.route('/bookingHistory', methods=['GET'])
    def Booking_History():
        resp = {
            "isError": True,
            "msg": "You are not authorized to view"
        }
        token = request.headers['Authorization'][7:]
        var = authentication.authorization(token);
        if (var['isAuthenticated'] == True):
            user_details=authentication.get_user_details_through_token(token)
            phoneNo = user_details['phoneNo'];
            respData = history_module(phoneNo);
            return json.dumps(respData), 200
        else:
            return jsonify(resp), 200

    
    @app.route('/bookSlot',methods=['POST'])
    def book_slot():
        resp = {
            "isError": True,
            "msg": "You are not authorized to view"
                }
        parkingArea = request.json['parkingArea']
        slotNumber = request.json['slotNumber']
        #numberPlate = request.json['numberPlate']
        url = 'http://192.168.137.121:5004/numberPlate';
        response = requests.get(url)
        jsonLoads= json.loads(response.content)
        val=''
        for key in jsonLoads:
            val = jsonLoads[key]
        numberPlate = val
        print(val)
        #numberPlate = 'abc'
        token = request.headers['Authorization'][7:]
        var = authentication.authorization(token);
        if (var['isAuthenticated'] == True):
            user_details=authentication.get_user_details_through_token(token)
            phoneNo = user_details['phoneNo'];
            respData = slotBooking.confirm_booking(phoneNo,parkingArea,slotNumber,numberPlate)
            return jsonify(respData),200
        else:
            return jsonify(resp), 200
    @app.route('/antimPlateDetection',methods=['GET'])
    def generatedText():
        url = 'http://192.168.137.121:5004/sendImageVal';
        response = requests.get(url)
        jsonLoads= json.loads(response.content)
        val=''
        for key in jsonLoads:
            val = jsonLoads[key]
        base64.b64decode(val)
        return response, 200
    @app.route('/exitParking',methods = ['GET'])
    def exit_parking():
        resp = {
            "isError": True,
            "msg": "You are not authorized to view"
                }
        #print("i am here")
        exitTime = getCurrentTime();
        
        token = request.headers['Authorization'][7:]
        var = authentication.authorization(token);
        if (var['isAuthenticated'] == True):
            user_details=authentication.get_user_details_through_token(token)
            phoneNo = user_details['phoneNo'];
            exitParking.updateExitTime(exitTime,phoneNo);
            msg = {
                "Time":"Car got exit"}
            return jsonify(msg);
        else:
            return jsonify(resp), 200


    @app.route('/parkingMap/<areaID>',methods = ['GET'])
    def parking_map(areaID):
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
    @app.route('/authorizePrebooked', methods = ['POST'])
    def authorize_preBooked():
        url = 'http://192.168.137.121:5004/numberPlate'
        response = requests.get(url)
        jsonLoads= json.loads(response.content)
        val=''
        for key in jsonLoads:
            val = jsonLoads[key]
        numberPlate = val
        print(numberPlate)
        phoneNumber = cardDetailsDB.getPhoneNumberThroughCar(numberPlate)
        slotAreaNumber = insertupdate.getSlotAreaNumber(phoneNumber)

        getSlotStatus = insertupdate.checkSlotAvailability(slotAreaNumber["slotNo"], slotAreaNumber["areaId"])
        print(getSlotStatus)
        if(getSlotStatus == "R" and slotAreaNumber["isPreBooked"]=="N"):
            url='http://192.168.137.121:5002/buzzer'
            response = request.get(url)
        
    return app


