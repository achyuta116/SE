import os
from ..__main__ import login
from .. import globals


def clear():
    os.system("clear")

def reset():
    input('Press Enter to Exit')
    clear()
    login()
