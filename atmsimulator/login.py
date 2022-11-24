import inquirer
import requests
import sys
from simple_chalk import chalk
from pyfiglet import figlet_format
from .account import customer_account_selection
from .loans import customer_loan_selection
from .atm_operator import operator_options_selection

from .globals import get_account, set_account 

def customer_category_selection():
    question = [inquirer.List('selection',
                              message="Choose transaction type",
                              choices=['Accounts', 'Loans'])]
    selection = inquirer.prompt(question)['selection']
    if selection == 'Accounts':
        customer_account_selection()
    elif selection == 'Loans':
        customer_loan_selection()

def login():
    """ Display welcome message followed by a login prompt. """

    print(chalk.green.bold(figlet_format("Hindustan Bank", font="slant"))) # welcome msg

    user_name = inquirer.text(message="Enter your username")
    pin = inquirer.password(message="Enter your PIN")

    res = requests.get(f"http://localhost:3000/users/?username={user_name}&password={pin}")
    data = res.json()

    if (len(data)==0):
        print(chalk.red.bold("Incorrect credentials provided"))
        sys.exit(1)
    else:
        set_account(data[0])
        print("Hello,", chalk.green.bold(user_name))
        if get_account()['isOperator']:
            operator_options_selection()
        else: 
            customer_category_selection()

            res = requests.put(f"http://localhost:3000/users/{user_name}", 
                         json=get_account())
            if (res.status_code == 200):
                print(chalk.green.bold('Transaction successful'))
            else:
                print(chalk.red.bold('Something went wrong with your transaction'))
                sys.exit(1)





if __name__ == "__main__":
    login()
    
