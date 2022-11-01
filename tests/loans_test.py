import unittest
from atmsimulator.loans import *

class TestLoans(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        from atmsimulator import globals
        globals.account = {
            "id": 1,
            "username": "Achyuta",
            "password": "123456",
            "accounts": [],
            "loans": [
                {
                    "type": "Personal",
                    "principal": 4000,
                    "tenure": 3,
                    "date": "01/11/2022",
                    "status": "Notified Bank"
                },
                {
                    "type": "Personal",
                    "principal": 5000,
                    "tenure": 4,
                    "status": "Approved",
                    "interest": 400,
                    "date": "31/10/2022"
                }

            ],
            "bills": []
        }
        return super().setUpClass()

    def test_customer_loan_selection(self):
        customer_loan_selection()

    def test_customer_loan_application(self):
        customer_loan_application()
        self.assertEqual(len(globals.account['loans']), 3)

    def test_customer_loan_review(self):
        customer_loan_review()



