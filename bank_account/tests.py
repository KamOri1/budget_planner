from django.contrib.auth.models import User
from django.test import TestCase

from bank_account.models import BankAccount


class TestModels(TestCase):
    def test_model_BankAccount(self):
        user = User.objects.create_user(
            username="Test", password="password", email="test@gmail.com"
        )

        bank_account = BankAccount.objects.create(
            user_id=user,
            account_name="Shopping",
            account_number=102030,
            sum_of_funds=144,
        )

        self.assertEqual(str(bank_account.user_id), user.username)
        self.assertEqual(str(bank_account), "Shopping")
        self.assertEqual(int(bank_account.account_number), 102030)
        self.assertEqual(int(bank_account.sum_of_funds), 144)
        self.assertTrue(isinstance(bank_account, BankAccount))
