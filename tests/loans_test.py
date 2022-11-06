import unittest

import requests
from atmsimulator.loans import *
from unittest.mock import patch

class TestLoans(unittest.TestCase):
    def setUp(self) -> None:
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
        return super().setUp()

    @patch('requests.get', lambda _: requests.Response)
    def test_customer_loan_selection(self):
        with patch('requests.Response.json') as mock_json:
            mock_json.return_value = [globals.account]
            customer_loan_selection()

    @patch('requests.get', lambda _: requests.Response)
    def test_customer_loan_application(self):
        with patch('requests.Response.json') as mock_json:
            mock_json.return_value = [globals.account]
            customer_loan_application()
            self.assertEqual(len(globals.account['loans']), 3)

    @patch('requests.get', lambda _: requests.Response)
    def test_customer_loan_review(self):
        with patch('requests.Response.json') as mock_json:
            mock_json.return_value = [globals.account]
            customer_loan_review()



