from pyfiglet import figlet_format
from simple_chalk import chalk

from .utils.utils import clear

def welcome():
    clear()
    print(chalk.green.bold(figlet_format("Hindustan Bank")))