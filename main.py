import inquirer
from atmsimulator.welcome import welcome
from atmsimulator.login import login
from atmsimulator.register import register


def main():
    welcome()

    login_or_register = inquirer.list_input(
        "Login or Register?", choices=["Login", "Register"]
    )

    if login_or_register == "Register":
        register()  # no further execution

    login()


main()
