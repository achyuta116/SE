from atmsimulator.login import login
import requests
import sys
from requests.exceptions import ConnectionError
from simple_chalk import chalk

def main():
    try:
        _ = requests.get("http://localhost:3000/")
    except ConnectionError:
        print(chalk.red.bold("Bank server is down."))
        sys.exit(1)

    while True:
        login()


main()
