import inquirer
import sys
from inquirer.themes import GreenPassion
from simple_chalk import chalk
from pysondb import PysonDB

from .utils.utils import clear, sleep

# name, initial bank balance, type of account, address, DOB
# acc no will be randomly generated


def register():

    db_obj = PysonDB("./backend/customers.json")

    q = [
        inquirer.Text("name", message="Enter your name"),
        inquirer.List(
            "type",
            message="Select A/C type",
            choices=["savings", "current"],
            default="savings",
        ),
        inquirer.Text("address", message="Enter your address"),
        inquirer.Text("dob", message="Date of Birth(DD/MM/YYYY)"),
        inquirer.Text("balance", message="Initial Deposit", default=1000),
    ]
    responses = inquirer.prompt(q, theme=GreenPassion())
    pin = int(inquirer.password(message="Set your 4-digit PIN"))

    id = db_obj.add(
        {
            "name": responses["name"],
            "balance": responses["balance"],
            "type": responses["type"],
            "address": responses["address"],
            "dob": responses["dob"],
            "pin": pin,
            "transactions": [],
        }
    )
    sleep()
    clear()
    print(
        f"Registration successfull! Your A/C number is {chalk.green.bold(id)}\nPlease visit nearest branch to avail other benefits."
    )
    sys.exit(0)
