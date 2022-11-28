import unittest
import requests
from atmsimulator.account import customer_account_selection
from unittest.mock import patch


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        from atmsimulator import globals

        globals.account = {
            "id": 1,
            "username": "achyuta116",
            "password": "1234",
            "name": "Achyuta",
            "accounts": [
                {"type": "Savings", "balance": 300},
                {"type": "Current", "balance": 200},
            ],
            "transactions": [],
            "loans": [],
            "bills": [],
        }

        return super().setUp()

    @patch("requests.get", lambda _: requests.Response)
    def test_customer_account_selection(self):
        with patch("requests.Response.json") as _:
            # print(mock_json.return_value)
            customer_account_selection()
