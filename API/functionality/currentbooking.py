# -*- coding: utf-8 -*-
from database.current_detailsDB import currentbook_details

def currentbookingdetails(phoneNo):
    details = currentbook_details(phoneNo)  
    return details


