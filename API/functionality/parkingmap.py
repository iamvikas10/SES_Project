# -*- coding: utf-8 -*-
from database.parkingDatabase import slotDetails , parkDetails , slotStatus

def getParkingSlotDetails(ID):
    details = slotDetails(ID)
    return details
def getParkingCapacityDetails(ID):
    details = parkDetails(ID)
    return details

def getSlotStatus(ID):
    details = slotStatus(ID)
    return details

def getAvailability(areaID,slot_num):
    parkAvail = {'Availability' : 'Available'}
    parking_area_detail = getParkingCapacityDetails(areaID)
    area_capacity = parking_area_detail['capacity']
    parking_slot_detail = getParkingSlotDetails(areaID)
    
    num_slots_reserved = 0
    for item in parking_slot_detail :
        num_slots_reserved += item['reserve']
    if len(parking_area_detail) == 1:
        if num_slots_reserved == area_capacity:
            parkAvail = {'Availability':'No Empty Slot'}
            return parkAvail
        elif num_slots_reserved <= area_capacity:
            for item in parking_slot_detail:
                if item['slot_num'] == slot_num and item['reserve'] == 0:
                    parkAvail ={'Availability':'Slot Available'}
                    return parkAvail
                elif item['slot_num'] == slot_num and item['reserve'] == 1:
                    parkAvail ={'Availability':'Slot Reserved'}
                    return parkAvail
    elif len(parking_area_detail) == 0:
        parkAvail = {'Availability':'Parking Area unavailable'}
        return parkAvail
def getAreaStatus(areaID):
    park_area_status = getSlotStatus(areaID)
    return park_area_status
        

