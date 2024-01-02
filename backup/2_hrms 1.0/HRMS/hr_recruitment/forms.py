# from .models import Applicant  # Import your Applicant model
from django import forms
from django.forms import widgets
from .models import ResumeModel

# STATUS_CHOICES =(
#     ('draft', 'draft'),
#     ('Confirm', 'confirm'),
#     ('Cancel', 'cancel')
# )

class ResumeForm(forms.ModelForm):
    
    class Meta:
        model = ResumeModel
        fields = "__all__"
        labels  = {
            'name':'Name', 
            'submission_date':'Submitted Date',
            'sequence':'Sequence',  
            'appointment_date':'Appointment Date',
            'resume': 'Upload Resume',
            'interview_date': 'Interview Date',
            'interview_location': 'Interview Location',
            'interview_feedback': 'Interview Feedback',
            'assessment_score': 'Assessment Score',
            'assessment_feedback': 'Assessment Feedback',
            'status': 'Status',
            'note':'Internal Note', 
            'is_active':'Is Active', 
            'created_date':'Created Date', 
            'offer_extended':'Offer Extended',
            'offer_accepted':'Offer Accepted',
            'offer_salary':'Offer Salary',
            'offer_benefits':'Offer Benefits',
        }
        widgets = {
            'name': widgets.TextInput(attrs={'placeholder':'Resume Name'}),
            'submission_date': widgets.DateTimeInput(attrs={'placeholder': 'Submitted Date', 'type': 'datetime-local'}),
            'sequence': widgets.NumberInput(),
            'appointment_date': widgets.DateInput(attrs={'placeholder':'Interview Appointment Date', 'type': 'date'}),
            'resume': widgets.FileInput(),

            'interview_date': widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'interview_location': widgets.TextInput(attrs={'placeholder': 'Location'}),
            'interview_feedback': widgets.TextInput(attrs={'placeholder': 'Feedback'}),
            'assessment_score': widgets.NumberInput(attrs={'placeholder': 'Score'}),
            'assessment_feedback': widgets.TextInput(attrs={'placeholder': 'Feedback'}),
            
            'status': widgets.Select(),
            'note': widgets.TextInput(attrs={'placeholder': 'Internal Note'}),
            'is_active': widgets.CheckboxInput(),
            'created_date': widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            
            'offer_extended': widgets.CheckboxInput(),
            'offer_accepted': widgets.CheckboxInput(),
            'offer_salary': widgets.NumberInput(),
            'offer_benefits': widgets.Textarea(),
            
            #'attachment': widgets.ClearableFileInput()
        }


    def get_initial(self, field, field_name):
        # Override the get_initial_for_field method to set the initial value for the file field
        if field_name == 'resume':
            # Return the current value of the file field
            return self.instance.resume

