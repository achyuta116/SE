from time import sleep

import inquirer
import requests
from pyfiglet import figlet_format
from simple_chalk import chalk

from atmsimulator.utils.util import clear

from .account import customer_account_selection
from .atm_operator import operator_options_selection
from .globals import get_account, set_account
from .loans import customer_loan_selection


def customer_category_selection():
    clear()
    question = [
        inquirer.List(
            "selection",
            message="Choose transaction type",
            choices=["Accounts", "Loans"],
        )
    ]
    selection = inquirer.prompt(question)["selection"]
    if selection == "Accounts":
        customer_account_selection()
    elif selection == "Loans":
        customer_loan_selection()


def login():
    """Display welcome message followed by a login prompt."""
    clear()
    print(
        chalk.green.bold(figlet_format("Hindustan Bank", font="slant"))
    )  # welcome msg

    user_name = inquirer.text(message="Enter your username")
    pin = inquirer.password(message="Enter your PIN")

    res = requests.get(
        f"http://localhost:3000/users/?username={user_name}&password={pin}"
    )
    data = res.json()

    if len(data) == 0:
        print(chalk.red.bold("Incorrect credentials provided"))
        sleep(3)
        return
    else:
        set_account(data[0])
        print("Hello,", chalk.green.bold(user_name))
        if get_account()["isOperator"]:
            operator_options_selection()
        else:
            customer_category_selection()
            clear()
            res = requests.put(
                f"http://localhost:3000/users/{user_name}", json=get_account()
            )
            if res.status_code != 200:
                print(chalk.red.bold("Something went wrong with your transaction"))
                sleep(3)


if __name__ == "__main__":
    login()
