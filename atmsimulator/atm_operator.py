import sys
import inquirer
from . import globals
from .utils.util import *

def operator_options_selection():
    # Implement functionality to display options provided to the operator
    choice = [
        inquirer.List('selection',
                      message='Choose operator services',
                      choices=['Shutdown', 'Disable Service', 'Enable Service']
                      )]
    selection = inquirer.prompt(choice)['selection']
    if(selection=="Shutdown"):
        operator_options_shutdown()
    elif(selection=="Enable Service"):
        operator_options_enable_service()
    else:
        operator_options_disable_service()


def operator_options_shutdown():
    # Implement functionality to shut down the ATM
    # here by quitting the CLI altogether
    sys.exit("ATM SHUTDOWN")


def operator_options_disable_service():
    # Implement functionality to disable any service offered to the customer
    choices = []
    if (globals.config['loan'] == 1):
        choices.append('Loan')
    if (globals.config["account"]["withdrawal"] == 1):
        choices.append('Withdrawal')
    if (globals.config["account"]["mini"] == 1):
        choices.append('Mini Statement')

    if len(choices) == 0:
        print('No services to disable')
        return

    question = [
        inquirer.Checkbox('selection',
                      message='Disable which type of service',
                      choices=choices
                      )]
    selection = inquirer.prompt(question)['selection']
    for element in selection:
        if(element=="Loan"):
            globals.config["loan"] = 0
            print("Loan option DISABLED")
        elif(element=="Withdrawal"):
            globals.config["account"]["withdrawal"] = 0
            print("Withdrawal is DISABLED")
        elif(element=="Mini Statement"):
            globals.config["account"]["mini"] = 0
            print("Mini Statement is DISABLED")
    print("Services updated")

def operator_options_enable_service():
    # Implement functionality to enable any service offered to the customer
    choices = []
    if (globals.config['loan'] == 0):
        choices.append('Loan')
    if (globals.config["account"]["withdrawal"] == 0):
        choices.append('Withdrawal')
    if (globals.config["account"]["mini"] == 0):
        choices.append('Mini Statement')

    if len(choices) == 0:
        print('No services to enable')
        return
    question = [
        inquirer.Checkbox('selection',
                      message='Enable which type of service',
                      choices=choices)]
    selection = inquirer.prompt(question)['selection']
    for element in selection:
        if(element=="Loan"):
            globals.config["loan"] = 1
            print("Loan option ENABLED")
        elif(element=="Withdrawal"):
            globals.config["account"]["withdrawal"] = 1
            print("Withdrawal is ENABLED")
        elif(element=="Mini Statement"):
            globals.config["account"]["mini"] = 1
            print("Mini Statement is ENABLED")
    print("Services updated")
