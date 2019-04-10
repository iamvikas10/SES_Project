# -*- coding: utf-8 -*-

from database.cardDetailsDB import updateCarDetails,reg_car_details, editUpdateCarDetails
def car_details_func(phoneNo,rcNo,carModel):
     body_message = {
        'isError':False,
        'msg':'Car Details updated Successfully'
      }
     if(body_message['isError']==False):
        updateDB= updateCarDetails(phoneNo,rcNo,carModel)
     return body_message

def edit_car_details(phoneNo, rcNo, carModel):
    body_message = {
        'isError':False,
        'msg':'Car Details updated Successfully'
    }
    if(body_message['isError']==False):
        updateDB= editUpdateCarDetails(phoneNo,rcNo,carModel)
        return body_message
def get_car_details(phoneNo):
    details = reg_car_details(phoneNo) 
    return details

