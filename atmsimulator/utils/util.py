import os
import time 
from datetime import date,datetime

def clear():
    """ clear screen """
    os.system("clear")

def timestamp():   
    """ Get Timestamp in  DD-MM-YYYY HH:MM:SS format"""

    curr_date = date.today()
    curr_date = datetime.strptime(str(curr_date), "%Y-%m-%d").strftime("%d-%m-%Y")

    curr_time = time.strftime("%H:%M:%S", time.localtime())

    timestamp = "%s %s" %(curr_date,curr_time)

    return timestamp
