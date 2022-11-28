import sys
from time import sleep

import inquirer
from simple_chalk import chalk

from . import globals
from .utils.util import clear


def operator_options_selection():
    # Implement functionality to display options provided to the operator
    clear()
    choice = [
        inquirer.List(
            "selection",
            message="Choose operator services",
            choices=["Shutdown", "Disable Service", "Enable Service"],
        )
    ]
    selection = inquirer.prompt(choice)["selection"]
    if selection == "Shutdown":
        operator_options_shutdown()
    elif selection == "Enable Service":
        operator_options_enable_service()
    else:
        operator_options_disable_service()


def operator_options_shutdown():
    # Implement functionality to shut down the ATM
    # here by quitting the CLI altogether
    clear()
    sys.exit("ATM SHUTDOWN")


def operator_options_disable_service():
    # Implement functionality to disable any service offered to the customer
    clear()
    choices = []
    if globals.config["loan"] == 1:
        choices.append("Loan")
    if globals.config["account"]["withdrawal"] == 1:
        choices.append("Withdrawal")
    if globals.config["account"]["mini"] == 1:
        choices.append("Mini Statement")

    if len(choices) == 0:
        print(chalk.red.bold("No services to disable"))
        sleep(3)
        return

    question = [
        inquirer.List(
            "selection", message="Disable which type of service", choices=choices
        )
    ]
    selection = inquirer.prompt(question)["selection"]

    if selection == "Loan":
        globals.config["loan"] = 0
        print("Loan option DISABLED")
    elif selection == "Withdrawal":
        globals.config["account"]["withdrawal"] = 0
        print("Withdrawal is DISABLED")
    elif selection == "Mini Statement":
        globals.config["account"]["mini"] = 0
        print("Mini Statement is DISABLED")
    print("Services updated")
    sleep(3)


def operator_options_enable_service():
    # Implement functionality to enable any service offered to the customer
    clear()
    choices = []
    if globals.config["loan"] == 0:
        choices.append("Loan")
    if globals.config["account"]["withdrawal"] == 0:
        choices.append("Withdrawal")
    if globals.config["account"]["mini"] == 0:
        choices.append("Mini Statement")

    if len(choices) == 0:
        print(chalk.red.bold("No services to enable"))
        sleep(3)
        return
    question = [
        inquirer.List(
            "selection", message="Enable which type of service", choices=choices
        )
    ]
    selection = inquirer.prompt(question)["selection"]

    if selection == "Loan":
        globals.config["loan"] = 1
        print("Loan option ENABLED")
    elif selection == "Withdrawal":
        globals.config["account"]["withdrawal"] = 1
        print("Withdrawal is ENABLED")
    elif selection == "Mini Statement":
        globals.config["account"]["mini"] = 1
        print("Mini Statement is ENABLED")
    print("Services updated")
    sleep(3)
