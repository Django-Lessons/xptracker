from django.contrib.auth.models import AbstractUser
from django.db import models

EXPENSE = 'expense'
ASSET = 'asset'
INCOME = 'income'


class User(AbstractUser):
    pass


class XpAccount(models.Model):
    title = models.CharField(
        max_length=64
    )
    description = models.TextField()
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
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

    def __str__(self):
        return f"{self.title}/{self.acc_type}"


class XpTransaction(models.Model):

    created_at = models.DateTimeField()
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

