from atexit import register
from random import choices
import inquirer
from inquirer.themes import GreenPassion

from atmsimulator.welcome import welcome


def main():
    welcome()

    login_or_register = inquirer.list_input(
        "Login or Register?", choices=["Login", "Register"]
    )

    if login_or_register == "Login":
        pass
        # login()
    else:
        pass
        # register()


main()
