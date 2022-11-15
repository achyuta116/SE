import sys
import os
import inquirer
import json
from globals import *
from .utils.util import *
from login import *

def operator_options_selection():
    # Implement functionality to display options provided to the operator
    choice = [
        inquirer.List('selection',
                      message='Choose operator services',
                      choices=['Reboot', 'Shutdown', 'Disable Service']
                      )]
    selection = inquirer.prompt(choice)['selection']
    if(selection=="Reboot"):
        operator_options_reboot()
    elif(selection=="Shutdown"):
        operator_options_shutdown()
    else:
        operator_options_disable_service()


def operator_options_reboot():
    # Implement functionality to restart the ATM
    #os.execv(sys.argv[0],sys.argv)
    os.system("clear")           #trying different method for rebooting
    login()
    # os.startfile(sys.argv[0])
    # sys.exit()



def operator_options_shutdown():
    # Implement functionality to shut down the ATM
    # here by quitting the CLI altogether
    sys.exit("ATM SHUTDOWN")


def operator_options_disable_service():
    # Implement functionality to disable any service offered to the customer
    question = [
        inquirer.checkbox('selection',
                      message='Disable which type of service',
                      choices=['Loan', 'Withdrawal', 'Mini Statement','Bill']
                      )]
    selection = inquirer.prompt(question)['selection']
    for element in selection:
        if(element=="Loan"):
            globals.config["loan"] = 1
            print("Loan option DISABLED")
        elif(element=="Withdrawal"):
            globals.config["account"]["withdrawal"] = 1
            print("Withdrawal is DISABLED")
        elif(element=="Mini Statement"):
            globals.config["account"]["mini"] = 1
            print("Mini Statement is DISABLED")
        elif(element=="Bill"):
            globals.config["bill"] = 1
            print("Bill generation DISABLED")
            print()



