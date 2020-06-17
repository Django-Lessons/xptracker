from django import forms

from .models import ASSET, EXPENSE, INCOME


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
