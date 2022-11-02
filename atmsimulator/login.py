import inquirer
import requests
import sys
from simple_chalk import chalk
from pyfiglet import figlet_format

from .globals import account

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
        global account
        account = data[0]
        print("Hello,", chalk.green.bold(user_name))

if __name__ == "__main__":
    login()
    