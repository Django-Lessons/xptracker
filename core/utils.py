from datetime import date

from .models import XpTransaction


def perform_transaction(
    src,
    dst,
    amount,
    description
):
    """
    Move given amount of money from source account to destination
    account.
    """
    XpTransaction.objects.create(
        src=src,
        dst=dst,
        amount=amount,
        description=description,
        user=src.user,
        created_at=date.today()
    )

    src.amount -= amount
    src.save()
    dst.amount += amount
    dst.save()
