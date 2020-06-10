from django.contrib.auth.models import AbstractUser
from django.db import models

EXPENSE = 'expense'
ASSET = 'asset'
INCOME = 'income'


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
