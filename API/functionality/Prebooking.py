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
def Prebooking_module(slotNo, phoneNo, rcNo, expectedArrivalTime,ArrivalTime,bookingStatus,AreaId):
    pre=Prebooking();
    body_message = {
        'isError':False,
        'msg':'Booked Successsfully'
    }
    pre.set_slotNo(slotNo);
    pre.set_phoneNo(phoneNo);
    pre.set_ExpectedArrival(expectedArrivalTime);
    pre.set_ExactArrival(ArrivalTime);
    pre.set_rcNo(rcNo);
    pre.set_bookingStatus(str(bookingStatus));
    pre.set_AreaId(AreaId);
    # validatePhone = regValidations.is_user_present(phoneNo);
    if(body_message['isError']==False):
        updateDB=Prebooking_insert.update_tablePrebook(pre)
    return body_message;


