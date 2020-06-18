from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import redirect, render

from .forms import XpAccountForm
from .models import XpAccount, common_accounts


@login_required
def index(request):

    if XpAccount.objects.count() == 0:
        return redirect('start')

    return render(request, 'core/index.html')


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
