from django.test import TestCase

from .models import User, XpAccount
from .utils import perform_transaction


class XPTesting(TestCase):

    def setUp(self):
        self.user = User(username='john')
        self.user.save()

    def test_basics(self):
        """
        create two accounts and perform a transaction
        """
        groceries = XpAccount.objects.create(
            title="Groceries",
            amount=0.0,
            user=self.user
        )
        self.assertEqual(
            1,
            XpAccount.objects.count(),
        )
        bank_account = XpAccount.objects.create(
            title="BankAccount",
            amount=1000.0,
            user=self.user
        )
        self.assertEqual(
            2,
            XpAccount.objects.count(),
        )
        self.assertEqual(
            groceries.amount,
            0.0
        )
        self.assertEqual(
            bank_account.amount,
            1000.0
        )
        perform_transaction(
            src=bank_account,
            dst=groceries,
            amount=37.29,
            description="Groceries at MegaDiscounter"
        )
        self.assertEqual(
            groceries.amount,
            37.29
        )
        self.assertEqual(
            bank_account.amount,
            962.71
        )
