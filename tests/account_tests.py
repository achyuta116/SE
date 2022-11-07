import unittest
import requests
from atmsimulator.account import *
from unittest.mock import patch

class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        from atmsimulator import globals
        globals.account={
            "users": [
                {
                    "id": 1,
                    "username": "achyuta116",
                    "password": "1234",
                    "name": "Achyuta",
                    "accounts": [
                        {
                            "type": "Savings",
                            "balance": 300
                        },
                        {
                            "type": "Current",
                            "balance": 200
                        }
                    ],
                    "transactions": [],
                    "loans": [],
                    "bills": []
                }
            ]
        }
        return super().setUp()

    @patch('requests.get', lambda _: requests.Response)
    def test_customer_account_selection(self):
        with patch('requests.Response.json') as mock_json:
            print(mock_json.return_value)
            customer_account_selection()

    # @patch('requests.get', lambda _: requests.Response)
    # def test_customer_account_check_balance(self):
    #     with patch('requests.Response.json') as mock_json:
    #         mock_json.return_value = [globals.account]
    #         customer_account_check_balance()

    # @patch('requests.get', lambda _: requests.Response)
    # def test_customer_account_cash_withdrawal(self):
    #     with patch('requests.Response.json') as mock_json:
    #         mock_json.return_value = [globals.account]
    #         customer_account_cash_withdrawal()

    # @patch('requests.get', lambda _: requests.Response)
    # def test_customer_loan_review(self):
    #     with patch('requests.Response.json') as mock_json:
    #         mock_json.return_value = [globals.account]
    #         customer_account_cheque_deposit()
