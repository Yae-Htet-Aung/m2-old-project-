from django import forms
from django.forms import widgets
from .models import ExpenseModel


class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model = ExpenseModel
        fields = "__all__"
        labels  = {
            'name': 'Expense Name',
            'date': 'Expense Date',
            'category': 'Expense Category',
            'description': 'Expense Description',
            'reason': 'Reason',

            'claimed_amount': 'Claimed Amount',
            'approved_amount': 'Approved Amount',
            'currency': 'Currency',
            'payment_name': 'Payment Name',
            'payment_description': 'Payment Description',
            
            'payment_date': 'Payment Date',
            'claimed_date': 'Claimed Date',
            'approval_date': 'Approval Date',
            'receipt_image': 'Receipt Image',
            'status': 'Status',
            
            'comments': 'Comments',
            'note': 'Note',
            
        }
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder': 'Expense Name'}),
            'date': widgets.DateInput(attrs={'type': 'date'}),
            'category': widgets.TextInput(),
            'description': widgets.TextInput(),
            'reason': widgets.TextInput(),

            'claimed_amount': widgets.NumberInput(),
            'approved_amount': widgets.NumberInput(),
            'currency': widgets.TextInput(),
            'payment_name': widgets.TextInput(),
            'payment_description': widgets.TextInput(),
            
            'payment_date': widgets.DateInput(attrs={'type': 'date'}),
            'claimed_date': widgets.DateInput(attrs={'type': 'date'}),
            'approval_date': widgets.DateInput(attrs={'type': 'date'}),
            'receipt_image': widgets.FileInput(),
            'status': widgets.Select(),

            'comments': widgets.TextInput(),
            'note': widgets.Textarea(),
            }


    def get_initial(self, field, field_name):
        # Override the get_initial_for_field method to set the initial value for the file field
        if field_name == 'receipt_image':
            # Return the current value of the file field
            return self.instance.receipt_image