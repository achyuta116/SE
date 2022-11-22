import unittest
from atmsimulator.login import login


class TestLogin(unittest.TestCase):
    """Unittest to test the login functionality"""

    @classmethod
    def setUpClass(cls) -> None:

        print("Testing login")

    @classmethod
    def tearDownClass(cls) -> None:
        print("\nLogin test finished")

    def test_login(self):
        login()
