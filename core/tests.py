from django.test import TestCase

from .models import User, XpAccount
from .utils import perform_transaction


class XpTracker(TestCase):

    def test_basics(self):
        user = User(username='john')
        user.save()

        groceries = XpAccount.objects.create(
            name="Groceries",
            amount=0.0,
            user=user
        )

        self.assertEqual(
            1,
            XpAccount.objects.count()
        )

        bank_account = XpAccount.objects.create(
            name="Bank Account",
            amount=1000.0,
            user=user
        )

        self.assertEqual(
            2,
            XpAccount.objects.count()
        )

        self.assertEqual(
            groceries.amount,
            0
        )

        self.assertEqual(
            bank_account.amount,
            1000.0
        )

        perform_transaction(
            src=bank_account,
            dst=groceries,
            amount=50,
            description="I did my groceries today at MegaDiscounter"
        )

        self.assertEqual(
            groceries.amount,
            50
        )

        self.assertEqual(
            bank_account.amount,
            950.00
        )
