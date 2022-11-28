import re
import time

import inquirer
from simple_chalk import chalk
from texttable import Texttable

from . import globals
from .utils.util import (
    clear,
    disabled_service_message,
    unsuccessful_transaction_message,
)


def customer_account_selection():
    # Implement select functionality for customer account screen
    clear()
    question = [
        inquirer.List(
            "selection",
            message="Choose account service",
            choices=[
                "Check Balance",
                "Cash Withdrawal",
                "Cheque Deposit",
                "Mini Statement",
                "Cancel",
            ],
        )
    ]
    selection = inquirer.prompt(question)["selection"]
    if selection == "Check Balance":
        customer_account_check_balance()
    elif selection == "Cash Withdrawal":
        customer_account_cash_withdrawal()
    elif selection == "Cheque Deposit":
        customer_account_cheque_deposit()
    elif selection == "Mini Statement":
        customer_account_mini_statement()


def customer_account_check_balance():
    # Implement functionality to retrieve and print balance.
    # 5 recent transactions printed with mini-statement.
    clear()
    print(
        "Your current balance is: ", globals.account["accounts"][1]["balance"], " Rs."
    )
    print("Your savings are: ", globals.account["accounts"][0]["balance"], " Rs.")
    time.sleep(3)


def customer_account_cash_withdrawal():
    # Implement functionality to deduct money from respective account
    # and print withdrawal message to the customer
    clear()
    if globals.config["account"]["withdrawal"] != 1:
        disabled_service_message()
        return
    elif globals.config['cash']==0:
        return unsuccessful_transaction_message()

    else:
        question = [
            inquirer.List(
                "selection",
                message="Choose account to withdraw",
                choices=["Savings", "Current", "Cancel"],
            )
        ]
        selection = inquirer.prompt(question)["selection"]

        clear()

        request_questions = [
            inquirer.Text(
                name="w",
                message="Enter amount in Rs. to be withdrawn: ",
                validate=lambda _, x: re.match("^[0-9]+$", x),
            ),
        ]

        if selection == "Savings":
            withdraw = inquirer.prompt(request_questions)
            withdraw = int(withdraw["w"])
            if (
                globals.account["accounts"][0]["balance"] < withdraw
                or withdraw > 250000
                or withdraw < 50
                or withdraw > globals.config['cash']
            ):
                print(
                    "Your account has insufficient balance or maximum withdrawal limit exceeded or less than minimum withdraw requested."
                )
                unsuccessful_transaction_message()
                return
            else:
                globals.account["accounts"][0]["balance"] -= withdraw
                globals.config['cash']-= withdraw
                # print(globals.config['cash'])
                print(
                    "Withdraw successful. Your savings balance is: ",
                    globals.account["accounts"][0]["balance"],
                )

        elif selection == "Current":
            withdraw = inquirer.prompt(request_questions)
            withdraw = int(withdraw["w"])

            if (
                globals.account["accounts"][1]["balance"] < withdraw
                or withdraw > 250000
                or withdraw < 50
                or withdraw > globals.config['cash']
            ):
                print(
                    "Your account has insufficient balance or maximum withdrawal limit exceeded or less than minimum withdraw requested."
                )
                unsuccessful_transaction_message()
                return
            else:
                globals.account["accounts"][1]["balance"] -= withdraw
                globals.config['cash']-= withdraw
                print(
                    "Withdraw successful. Your savings balance is: ",
                    globals.account["accounts"][1]["balance"],
                )

        else:
            unsuccessful_transaction_message()
            return
        time.sleep(3)


def customer_account_cheque_deposit():
    # Implement functionality to add cheque funds into respective
    # account and print confirmation message
    clear()
    question = [
        inquirer.List(
            "selection",
            message="Choose account to deposit cheque",
            choices=["Savings", "Current", "Cancel"],
        )
    ]
    selection = inquirer.prompt(question)["selection"]

    clear()

    request_questions = [
        inquirer.Text(
            name="d",
            message="Enter amount in Rs. to be deposited: ",
            validate=lambda _, x: re.match("^[0-9]+$", x),
        ),
    ]

    if selection == "Savings":
        deposit = inquirer.prompt(request_questions)
        deposit = int(deposit["d"])
        if deposit > 50:
            globals.account["accounts"][0]["balance"] += deposit
            globals.config['cash']+= deposit
            # print(globals.config['cash'])
            print(
                "Deposit successful. Your savings balance is: ",
                globals.account["accounts"][0]["balance"],
            )
        else:
            # print('Invalid input. Please enter a numeral amount greater than 50 rs')
            unsuccessful_transaction_message()
            return

    elif selection == "Current":
        deposit = inquirer.prompt(request_questions)
        deposit = int(deposit["d"])

        if deposit < 50:
            # print('Invalid input. Please enter a numeral amount greater than 50 rs')
            unsuccessful_transaction_message()
            return
        else:
            globals.account["accounts"][1]["balance"] += deposit
            globals.config['cash']+= deposit
            print(
                "Deposit successful. Your current balance is: ",
                globals.account["accounts"][1]["balance"],
            )
    else:
        unsuccessful_transaction_message()
        return
    time.sleep(3)


def customer_account_mini_statement():
    """display 5 most recent transactions of the user in table format"""
    clear()
    if globals.config["account"]["mini"] != 1:
        disabled_service_message()
        return
    else:
        try:
            transactions: list = globals.account["transactions"]

            if transactions is not None and len(transactions) > 0:
                table = Texttable(max_width=0)
                table.add_row(
                    [
                        "Sl No.",
                        "Time",
                        "Transaction ID",
                        "Type",
                        "Withdrawl",
                        "Deposit",
                        "Balance",
                    ]
                )
                table.set_cols_align(["c", "c", "c", "c", "c", "c", "c"])
                table.add_rows(transactions[-5:])

                print(table.draw())
                time.sleep(3)
            else:
                print(chalk.red.bold("No Transactions to Display."))
                time.sleep(3)
                return

        except Exception as e:
            print(e)
