from PIL import Image
import base64
import numpy as np
import pytesseract
import cv2
import os
import re
from database.Prebooking_insert import book_details
from database.viewUpdateDB import update_tableBooking
import time, datetime

def get_car_details(phoneNo):
    details = book_details(phoneNo) 
    return details

def number_plate_detection(image):
    #image = cv2.imread(filename)
   # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = image.convert('LA')
    
   
    #gray = cv2.medianBlur(gray, 3)
    
    #filename = "{}.png".format(os.getpid())
    #cv2.imwrite(filename, gray)
    img.save('test.png')
    text = pytesseract.image_to_string(Image.open('test.png'))
    #os.remove(filename)
    #print(text)
    #cv2.imshow("Image", image)
    #cv2.imshow("Output", gray)
    
    #cv2.waitKey(0)
    text = re.sub(pattern = r'[^A-Za-z0-9]',repl="",string=text)
    print(text)
    return text
def antimPlateDetection(value):
    nparr = np.fromstring(value, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(nparr.shape)
    img1 = Image.fromarray(img,'RGB')
                #do some fancy processing here....
    img1.save('test222.png')
    text = pytesseract.image_to_string(Image.open('test222.png'))
    text = re.sub(pattern = r'[^A-Za-z0-9]',repl="",string=text)
    return text
def getCurrentTime():
    ts = time.time();
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print(st)
    return st;
    
def confirm_booking(phoneNo,parkingArea,slotNumber,numberPlate):
    #numberPlate += "=" * ((4 - len(numberPlate) % 4) % 4)
    #imageString = base64.b64decode(numberPlate)
    #print(len(numberPlate))
    #imageString = base64.b64decode(bytes(numberPlate,'utf8'))
    
    #nparr = np.fromstring(imageString, np.uint8)
    #image = cv2.imdecode(nparr, cv2.IMREAD_COLOR);
    #print(imageString)
    #testImg = Image.fromarray(nparr,'RGB')
    #testImg.save('test.png')
    #print(testImg)
    #cv2.imwrite('imtest', image)
    #number_plate = number_plate_detection(image)
    
    user_car_details = get_car_details(phoneNo)
    user_number_plate = user_car_details['rcNo']
    print(user_number_plate)
    preBookingStatus = user_car_details['preBookingStatus']
    arrivalTime = getCurrentTime();
    if user_number_plate == numberPlate and preBookingStatus == 1:
        resp = {'isError':False}
        updateBookingTable = update_tableBooking(arrivalTime, phoneNo);
        return resp
    
    elif user_number_plate != numberPlate and preBookingStatus == 1:
        resp = {'isError':True}
        return resp
    
    elif preBookingStatus == 0:
        resp = {'isError':False}
        updateBookingTable = update_tableBooking(arrivalTime, phoneNo);
        return resp;
    

    