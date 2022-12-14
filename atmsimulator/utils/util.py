import os
import time
from datetime import date, datetime

from simple_chalk import chalk


def clear():
    """clear screen"""
    os.system("clear")


def timestamp():
    """Get Timestamp in  DD-MM-YYYY HH:MM:SS format"""

    curr_date = date.today()
    curr_date = datetime.strptime(str(curr_date), "%Y-%m-%d").strftime("%d-%m-%Y")

    curr_time = time.strftime("%H:%M:%S", time.localtime())

    timestamp = "%s %s" % (curr_date, curr_time)

    return timestamp


def disabled_service_message():
    print(
        chalk.red.bold(
            """Cannot avail this service as it has been disabled by you or the operator.
     Please visit our bank for more information or wait till services get enabled."""
        )
    )
    time.sleep(3)


def unsuccessful_transaction_message():
    print(
        chalk.red.bold(
            "Transaction Unsuccessful. Try again after some time. You may report your dissent on our feedback page."
        )
    )
    time.sleep(3)
