from django import forms
from hr_department import models
from django.forms import widgets

STATUS_CHOICES =(
	('running_project', 'Running Project'),
	('standby', 'Standby'),
	('busy', 'Busy')
)

class DepartmentForm(forms.ModelForm):
	class Meta:
		model = models.DepartmentModel
		fields = "__all__"
		labels = {
			'name':'Department Name',
			'description': 'Enter Note',
			'total_employees':'Total Employees',
			'created_date': 'Estiblished Date',
			'updated_date': 'Updated Date',
			'status':'Status',
			'is_active':'Is Active',
			'project_name':'Ongoing Project Name',
			'deadline':'Project Deadline',
			'address':'Address',
			'city':'City',
			'state':'State',
			'postal_code':'Postal Code',
			'phone':'Phone',
			'email':'Email',
			'budget':'Project Budget',
			'custom_field':'Custom Field',
		}
		widgets = {
			'name': widgets.TextInput(attrs={'placeholder': 'Name'}),
			'description': widgets.Textarea(attrs={'placeholder': 'Description'}),
			'total_employees': widgets.TextInput(attrs={'placeholder': 'Total Employees'}),
			'created_date': widgets.DateInput(attrs={'placeholder':'Established Date', 'type': 'date'}),
			'updated_date': widgets.DateInput(attrs={'placeholder': 'Updated Date', 'type': 'date'}),
			'status':  widgets.Select(choices=STATUS_CHOICES),
			'is_active': widgets.CheckboxInput(),
			'deadline': widgets.DateInput(attrs={'placeholder': 'Project Deadline', 'type': 'date'}),
			'address': widgets.TextInput(attrs={'placeholder': 'Address'}),
			'city': widgets.TextInput(attrs={'placeholder': 'City'}),
			'state': widgets.TextInput(attrs={'placeholder': 'State'}),
			'postal_code': widgets.TextInput(attrs={'placeholder': 'Postal Code'}),
			'phone': widgets.TextInput(attrs={'placeholder': 'Contact Number'}),
			'email': widgets.TextInput(attrs={'placeholder': 'Email'}),
			'budget': widgets.NumberInput(attrs={'palceholder': 'Project Budget'}),
			'custom_field': widgets.Textarea(attrs={'placeholder': 'Custom Field'}),
		}