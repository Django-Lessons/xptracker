from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import redirect, render

from .utils import perform_transaction
from .forms import XpAccountForm, XpTransactionForm
from .models import (
    XpAccount,
    common_accounts,
    ASSET,
    XpTransaction
)


@login_required
def index(request):

    if XpAccount.objects.count() == 0:
        return redirect('start')

    expenses = XpTransaction.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'core/index.html',
        {'expenses': expenses}
    )


@login_required
def expense(request):

    if request.method == "POST":

        expense_form = XpTransactionForm(request.POST)

        if expense_form.is_valid():

            perform_transaction(
                src=expense_form.cleaned_data['src'],
                dst=expense_form.cleaned_data['dst'],
                amount=expense_form.cleaned_data['amount'],
                description=expense_form.cleaned_data['description']
            )

            return redirect('index')

    src = XpAccount.objects.get(
        acc_type=ASSET
    )

    initial = XpTransaction(
        src=src, amount=0
    )

    form = XpTransactionForm(
        instance=initial
    )

    return render(
        request,
        "core/expense.html", {
            'form': form
        }
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

    formset = XpAccountFormSet(initial=common_accounts)

    return render(
        request,
        'core/start.html',
        {'formset': formset}
    )
