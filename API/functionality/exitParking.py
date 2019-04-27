# -*- coding: utf-8 -*-
import datetime
from database.viewUpdateDB import update_tableBookingExit,arrivalTime
def upadateExitTime(exitTime,phoneNo):
    completeStatus = 1
    ArrivalTime = arrivalTime(phoneNo)
    print(ArrivalTime)
    ExitTime = datetime.datetime.strptime(exitTime, '%Y-%m-%d %H:%M:%S')
    ArrivalTime = datetime.datetime.strptime(ArrivalTime, '%Y-%m-%d %H:%M:%S')
    d = ExitTime-ArrivalTime
    minutes = d.seconds/60.0
    amount = minutes * 2.0
    update_tableBookingExit(exitTime,phoneNo,completeStatus,amount)
