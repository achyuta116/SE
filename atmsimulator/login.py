import inquirer
import sys
from simple_chalk import chalk
from pysondb import PysonDB

# take acc-id and pin as input 
# search for user with given acc-id 
# check if pin matches

def login():
    id = inquirer.text(message="Enter your account id")
    pin = inquirer.text(message="Enter your PIN")

    db_obj = PysonDB("./backend/customers.json")

    user = db_obj.get_by_id(id)
    
    if(user["pin"]!=int(pin)):
        print(chalk.red.bold("Incorrect PIN entered"))
        sys.exit(1)
    else:
        print("Hello, ",chalk.green.bold(user["name"]))
        return id