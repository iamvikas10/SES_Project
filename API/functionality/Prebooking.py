'''
Created on Mar 18, 2019

@author: iamvikas10
'''
from validations import regValidations
from classes.prebooking import Prebooking;
from database import Prebooking_insert
from exceptions import customExceptions;
import base64;

#function for prebooking
def Prebooking_module(slotNo, phoneNo, rcNo, expectedArrivalTime,bookingStatus,AreaId):
    pre=Prebooking();
    body_message = {
        'isError':False,
        'msg':'Booked Successsfully'
    }
    
    # validatePhone = regValidations.is_user_present(phoneNo);
    if(body_message['isError']==False):
        updateDB=Prebooking_insert.update_tablePrebook(slotNo, phoneNo, rcNo, expectedArrivalTime,bookingStatus,AreaId)
    return body_message;


