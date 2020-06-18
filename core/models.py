from django.contrib.auth.models import AbstractUser
from django.db import models

EXPENSE = 'expense'
ASSET = 'asset'
INCOME = 'income'

common_accounts = [
    {
        'title': "Bank Account",
        'description': "Your bank account",
        'acc_type': ASSET,
        'amount': 1000
    },
    {
        'title': "Income Account",
        'description': "Account for your income like salary, consulting.",
        'acc_type': INCOME,
        'amount': 0
    },
    {
        'title': "Groceries",
        'description': "All groceries expenses go here",
        'acc_type': EXPENSE,
        'amount': 0
    },
    {
        'title': "Rent",
        'description': "Monthly Rent",
        'acc_type': EXPENSE,
        'amount': 0
    },
    {
        'title': "Insurances",
        'description': "All kind of insurances",
        'acc_type': EXPENSE,
        'amount': 0
    },
    {
        'title': "Utility Bills",
        'description': "Like electricity bills, tv, internet",
        'acc_type': EXPENSE,
        'amount': 0
    }
]


class User(AbstractUser):
    pass


class XpAccount(models.Model):
    name = models.CharField(
        max_length=64
    )
    description = models.TextField()
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    acc_type = models.CharField(
        choices=[
            (EXPENSE, 'Expense'),
            (ASSET, 'Asset'),
            (INCOME, 'Income')
        ],
        default=EXPENSE,
        max_length=16
    )

class XpTransaction(models.Model):

    # transaction's date
    created_at = models.DateField()

    description = models.TextField()

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    src = models.ForeignKey(
        'XpAccount',
        on_delete=models.CASCADE,
        related_name='src'
    )

    dst = models.ForeignKey(
        'XpAccount',
        on_delete=models.CASCADE,
        related_name='dst'
    )

    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
    )
