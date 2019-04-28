from database import insertupdate

def changeSlotStatus(areaID, slotNumber, slotStatus):
    updateSlotStatus = insertupdate.update_parkingSlotTable(areaID, slotNumber, slotStatus)
    if(updateSlotStatus):
        print("changing slot of "+ str(areaID) + " " + str(slotNumber)+ "to "+ slotStatus)
        return True
    return False

