from django import forms

from .models import ASSET, EXPENSE, INCOME, XpTransaction


class XpAccountForm(forms.Form):

    name = forms.CharField(
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


class XpTransactionForm(forms.ModelForm):

    class Meta:

        model = XpTransaction

        fields = [
            'src',
            'dst',
            'amount',
            'description'
        ]
