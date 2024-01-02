from django import forms
from hr_job import models
from django.forms import widgets

# EMPLOYMENT_CHOICES = (
#     ('draft', 'Draft'),
#     ('open', 'Open'),
#     ('confirm', 'Confirm')
# )


class JobForm(forms.ModelForm):
    class Meta:
        model = models.JobModel
        fields = "__all__"
        labels = {
            'title': 'Job Title',
            'description': 'Job Description',
            'responsibilities': 'Job Responsibilities',
            'requirements': 'Requirements',
            'employment_type': 'Employment Type',

            'location': 'Job Location',
            'salary': 'Salary',
            'published_date': 'Published Date',
            'application_deadline':'Application Deadline',
            'is_active':'Is Job Active?',

            'company_name': 'Company Name',
            'company_description': 'About Company',
            'company_website': 'Company Website',
            'contact_name': 'Contact Name',
            'contact_email': 'Contact Email',

            'contact_phone': 'Contact Phone',
            'benefits': 'Benefits',
            'additional_information': 'Additional Informations',
        }
        # title responsibilities requirements employment_type salary published_date benefits
        widgets = {
            'title': widgets.TextInput(attrs={'placeholder': 'Enter Job Title'}),
            'description': widgets.Textarea(attrs={'placeholder': 'Enter Job Description'}),
            'responsibilities': widgets.Textarea(attrs={'placeholder': 'Enter Job Responsibilities'}),
            'requirements': widgets.Textarea(attrs={'placeholder': 'Enter Job Requirements'}),
            'employment_type': widgets.Select(),

            'location': widgets.TextInput(attrs={'placeholder': 'Enter Location'}),
            'salary': widgets.NumberInput(attrs={'placeholder':'Enter Salary'}),
            'published_date': widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'application_deadline': widgets.DateInput(attrs={'type': 'date'}),
            'is_active': widgets.CheckboxInput(),

            'company_name': widgets.TextInput(attrs={'placeholder': 'Enter Company Name'}),
            'company_description': widgets.Textarea(attrs={'placeholder': 'Enter Company Description'}),
            'company_website': widgets.TextInput(attrs={'placeholder': 'Enter Company Website'}),
            'contact_name': widgets.TextInput(attrs={'placeholder': 'Enter Contact Name'}),
            'contact_email': widgets.TextInput(attrs={'placeholder': 'Enter Contact Email'}),

            'contact_phone': widgets.TimeInput(attrs={'placeholder': 'Enter Contact Number'}),
            'benefits': widgets.Textarea(attrs={'placeholder': 'Enter Benefits'}),
            'additional_information': widgets.Textarea(attrs={'placeholder': 'Enter Additional Information'}),
        }
