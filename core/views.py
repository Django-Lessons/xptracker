from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import XpAccount


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
    return render(request, 'core/start.html')
