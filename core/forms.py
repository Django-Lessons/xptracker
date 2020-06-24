from django import forms
from django.forms import ModelForm

from .models import ASSET, EXPENSE, INCOME, XpTransaction


class XpAccountForm(forms.Form):
    title = forms.CharField(
        label='Name',
        max_length=100
    )
    description = forms.CharField(
        label='Description',
        max_length=100
    )
    amount = forms.IntegerField(
        label="Amount",
    )
    acc_type = forms.ChoiceField(
        choices=[
            (EXPENSE, 'Expense'),
            (ASSET, 'Asset'),
            (INCOME, 'Income')
        ],
    )
    selected = forms.BooleanField(
        required=False
    )


class XpTransactionForm(ModelForm):

    class Meta:
        model = XpTransaction
        fields = [
            'src',
            'dst',
            'amount',
            'description'
        ]
