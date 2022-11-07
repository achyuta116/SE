import os
import time 
from datetime import date,datetime
from ..login import login
from .. import globals


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
    
def reset():
    input('Press Enter to Exit')
    clear()
    login()

def disabled_service_message():
    print('Cannot avail this service as it has been disabled by you or the operator. Please visit our bank for more information or wait till services get enabled.')

def unsuccessful_transaction_message():    
    print('Transaction Unsuccessful. Try again after some time. You may report your dissent on our feedback page.')
