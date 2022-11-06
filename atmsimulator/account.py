from texttable import Texttable
from simple_chalk import chalk

from globals import account

def customer_account_selection():
    # Implement select functionality for customer account screen
    pass


def customer_account_check_balance():
    # Implement functionality to retrieve and print balances
    # along with 5 recent transactions
    pass


def customer_account_cash_withdrawal():
    # Implement functionality to deduct money from respective account
    # and print withdrawal message to the customer
    pass


def customer_account_cheque_deposit():
    # Implement functionality to add cheque funds into respective
    # account and print confirmation message
    pass


def customer_account_mini_statement():
    """ display 5 most recent transactions of the user in table format """
    try:
        transactions: list = account.get("transactions") 

        if (transactions is not None and  len(transactions)>0):
            table = Texttable(max_width=0)
            table.add_row(
                [
                    "Sl No.",
                    "Time",
                    "Transaction ID",
                    "Type",
                    "Withdrawl",
                    "Deposit",
                    "Balance"
                ]
            )
            table.set_cols_align(["c", "c", "c", "c", "c", "c", "c"])
            table.add_rows(transactions[-5:])
            
            print(table.draw())
        else:
            print(chalk.red.bold("No Transactions to Display."))

    except Exception as e:
        print(e)
