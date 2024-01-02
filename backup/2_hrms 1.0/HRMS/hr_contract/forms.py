from django import forms
from django.forms import widgets
from .models import ContractModel
from datetime import datetime, timedelta

STATUS_CHOICES = (
    ('Draft', 'Draft'),
    ('Pending', 'Pending'),
    ('Confirm', 'Confirm'),
    ('Terminated', 'Terminated')
)

TYPE_CHOICES = (
    ('Employee', 'Employee'),
    ('Freelance', 'Freelance'),
    ('Contractor', 'Contractor'),
    ('Sub-contractor', 'Sub-contractor')
)


class ContractForm(forms.Form):

    contract_name = forms.CharField(label='Contract Name', widget=widgets.TextInput(
        attrs={'placeholder': 'Enter Contract Name'}))

    contract_id = forms.CharField(
        label='Contract ID', widget=widgets.TextInput())

    contractor_name = forms.CharField(label='Contractor Name', widget=widgets.TextInput(
        attrs={'placeholder': 'Enter Contractor Name'}), required=False)

    sub_contractor_name = forms.CharField(label='Sub-contractor Name', widget=widgets.TextInput(
        attrs={'placeholder': 'Enter Sub-contractor Name'}), required=False, )

    start_date = forms.DateField(initial=datetime.now().date(
    ), label='Enter Start Date', widget=widgets.DateInput(attrs={'type': 'date'}))

    end_date = forms.DateField(initial=datetime.now().date(
    ) + timedelta(days=365), label='Enter End Date', widget=widgets.DateInput(attrs={'type': 'date'}))

    contract_type = forms.ChoiceField(
        label='Contract Type', choices=TYPE_CHOICES)

    rank = forms.IntegerField(label='Enter Rank', widget=widgets.NumberInput(
        attrs={'placeholder': 'Contract Rank'}), initial=0)

    terminated_date = forms.DateField(initial=datetime.now().date(
    ) + timedelta(days=365), label='Enter Terminated Date', widget=widgets.DateInput(attrs={'type': 'date'}), required=False)

    terminated_reason = forms.CharField(label='Terminated Reason', widget=widgets.TextInput(
        attrs={'placeholder': 'Enter Reason'}), required=False)

    status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES)

    created_date = forms.DateTimeField(initial=datetime.now(
    ), label='Enter Created Date', widget=widgets.DateTimeInput(attrs={'type': 'datetime-local'}))

    updated_date = forms.DateTimeField(initial=datetime.now(
    ), label='Enter Updated Date', widget=widgets.DateTimeInput(attrs={'type': 'datetime-local'}))

    note = forms.CharField(label='Enter Note', widget=widgets.TextInput(
        attrs={'placeholder': 'Add Note'}), required=False)

    attachment = forms.ImageField(label='Upload Attachment', required=False)

    basic_salary = forms.DecimalField(
        label='Basic Salary ($)', widget=widgets.TextInput(), required=False, initial=0)

    salary = forms.DecimalField(
        label='Salary ($)', widget=widgets.TextInput(), required=False, initial=0)

    value = forms.DecimalField(
        label='Contract Value ($)', widget=widgets.TextInput(), required=False, initial=0)

    allowed_annual_leave = forms.IntegerField(
        label='Allowed Annual Leave', widget=widgets.NumberInput(), required=False, initial=0)

    class Meta:
        model = ContractModel
        fields = ('title', 'attachment')
# department
# job_title
