from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import redirect, render

from .forms import XpAccountForm, XpTransactionForm
from .models import ASSET, EXPENSE, INCOME, XpAccount

account_templates = [
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


@login_required
def index(request):

    if XpAccount.objects.count() == 0:
        return redirect('start')

    return render(request, 'core/index.html')


@login_required
def expense(request):

    form = XpTransactionForm()

    return render(
        request,
        'core/expense.html',
        {'form': form}
    )


@login_required
def accounts(request):

    accounts = XpAccount.objects.filter(user=request.user)

    return render(
        request,
        'core/accounts.html',
        {'accounts': accounts}
    )


@login_required
def start(request):
    """
    User will be redirected here if he/she does not have
    XpAccounts associated.
    Help user to create first couple of accounts.
    Let him/her selects from suggested accounts
    """
    if XpAccount.objects.count() != 0:
        return redirect('accounts')

    XpAccountFormSet = formset_factory(XpAccountForm, extra=0)

    if request.method == 'POST':
        xpaccounts_formset = XpAccountFormSet(request.POST)
        if xpaccounts_formset.is_valid():
            for form in xpaccounts_formset:
                attrs = form.cleaned_data
                if attrs['selected']:
                    attrs.pop('selected', False)
                    attrs['user_id'] = request.user.id
                    XpAccount.objects.create(**attrs)

            return redirect('index')

    formset = XpAccountFormSet(
        initial=account_templates,
    )

    return render(
        request,
        'core/start.html',
        {'formset': formset}
    )
