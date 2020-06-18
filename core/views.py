from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import XpAccount, common_accounts


@login_required
def index(request):

    if XpAccount.objects.count() == 0:
        return redirect('start')

    return render(request, 'core/index.html')


@login_required
def start(request):

    if request.method == 'POST':
        # for accounts that user selected
        # XpAccount.objects.create(...)
        return redirect('expenses')

    xpaccounts = [
        XpAccount(**acc) for acc in common_accounts
    ]
    return render(
        request,
        'core/start.html',
        {'xpaccounts': xpaccounts}
    )
