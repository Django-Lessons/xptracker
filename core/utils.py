from datetime import datetime

from .models import XpTransaction


def perform_transaction(src, dst, amount, description):
    """
    Move given amount of money from source to destination
    account
    """
    XpTransaction.objects.create(
        src=src,
        dst=dst,
        amount=amount,
        description=description,
        user=src.user,
        created_at=datetime.now()
    )
    src.amount -= amount
    src.save()
    dst.amount += amount
    dst.save()
