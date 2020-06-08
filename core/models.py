from django.contrib.auth.models import AbstractUser
from django.db import models


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


class XpTransaction(models.Model):

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
