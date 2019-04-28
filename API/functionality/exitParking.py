# -*- coding: utf-8 -*-
import datetime
from database.insertupdate import update_tableBookingExit,arrivalTime, update_parkingSlotByExitTime
def updateExitTime(exitTime,phoneNo):
    completeStatus = 0
    updateCompletedStatus = 1
    preBookingStatus = 0
    ArrivalTime = arrivalTime(phoneNo)
    print(ArrivalTime)
    ExitTime = datetime.datetime.strptime(exitTime, '%Y-%m-%d %H:%M:%S')
    ArrivalTime = datetime.datetime.strptime(str(ArrivalTime), '%Y-%m-%d %H:%M:%S')
    d = ExitTime-ArrivalTime
    minutes = d.seconds/60.0
    amount = minutes * 2.0
    update_tableBookingExit(ExitTime,phoneNo,updateCompletedStatus,amount, completeStatus,preBookingStatus)
    changeSlotStatus(ExitTime, phoneNo)

def changeSlotStatus(ExitTime, phoneNo):
    isUpdated = update_parkingSlotByExitTime(ExitTime,phoneNo)
    
    if(isUpdated):
        print("kya mai chal raha hu")
        return True