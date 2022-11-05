import os
from ..login import login
from .. import globals


def clear():
    os.system("clear")

def reset():
    input('Press Enter to Exit')
    clear()
    login()
