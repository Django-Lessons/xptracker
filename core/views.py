from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import ASSET, EXPENSE, INCOME, XpAccount

account_templates = [
    {
        'title': "Bank Account",
        'description': "You bank account",
        'acc_type': ASSET,
    },
    {
        'title': "Income Account",
        'description': "Account for your income like salary, consulting.",
        'acc_type': INCOME,
    },
    {
        'title': "Groceries",
        'description': "All groceries expenses go here",
        'acc_type': EXPENSE
    },
    {
        'title': "Rent",
        'description': "Monthly Rent",
        'acc_type': EXPENSE
    },
    {
        'title': "Insurances",
        'description': "All kind of insurances",
        'acc_type': EXPENSE
    },
    {
        'title': "Insurances",
        'description': "All kind of insurances",
        'acc_type': EXPENSE
    },
    {
        'title': "Utility Bills",
        'description': "Like electricity bills, tv, internet",
        'acc_type': EXPENSE
    }
]


@login_required
def index(request):

    if XpAccount.objects.count() == 0:
        return redirect('start')

    return render(request, 'core/index.html')


@login_required
def start(request):
    """
    User will be redirected here if he/she does not have
    XpAccounts associated.
    Help user to create first couple of accounts.
    Let him/her selects from suggested accounts
    """
    xpaccounts = [
        XpAccount(**acc) for acc in account_templates
    ]
    return render(
        request,
        'core/start.html',
        {'xpaccounts': xpaccounts}
    )
