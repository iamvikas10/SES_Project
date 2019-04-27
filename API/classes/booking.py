# -*- coding: utf-8 -*-
class booking:
    def __init__(self):
        self.__slotNo = None;
        self.__expectedArrival = None;
        self.__rcNo = None;
        self.__arrivalTime = None;
        self.__preBookingStatus = None;
        self.__phoneNo = None;
        self.__AreaId = None;
        self.__exitTime = None;
        self.__amount = None;
        self.__completedStatus = None;

    def get_slotNo(self):
        return self.__slotNo;
    def set_slotNo(self, value):
        self.__slotNo= value;
   
    def get_ExpectedArrival(self):
        return self.__ExpectedArrival
    def set_ExpectedArrival(self, value):
        self.__ExpectedArrival = value;
    
    def get_rcNo(self):
        return self.__rcNo;
    def set_rcNo(self, value):
        self.__rcNo = value;
    
    def get_phoneNo(self):
        return self.__phoneNo;
    def set_phoneNo(self, value):
        self.__phoneNo = value;
    
    def get_arrivalTime(self):
        return self.__arrivalTime;
    def set_arrivalTime(self, value):
        self.__arrivalTime = value;
    
    def get_preBookingStatus(self):
        return self.__preBookingStatus
    def set_preBookingStatus(self, value):
        self.__preBookingStatus = value;
    
    def get_AreaId(self):
        return self.__AreaId
    def set_AreaId(self, value):
        self.__AreaId = value;
    
    def get_exitTime(self):
        return self.__exitTime;
    def set_exitTime(self, value):
        self.__exitTime = value;
    
    def get_amount(self):
        return self.__amount;
    def set_amount(self, value):
        self.__amount = value;
    
    def get_completedStatus(self):
        return self.__completedStatus;
    def set_completedStatus(self, value):
        self.__completedStatus = value;
    
        
    

