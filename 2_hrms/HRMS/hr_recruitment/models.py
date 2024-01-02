from django.db import models
from django.utils import timezone
import os

class ResumeModel(models.Model):
    name = models.CharField(max_length=100)
    submission_date = models.DateTimeField(default=timezone.now)
    sequence = models.IntegerField(default='1')
    appointment_date = models.DateField(default=timezone.now)
    resume = models.FileField(upload_to='resume/')
    
    interview_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    interview_location = models.CharField(max_length=200, blank=True, null=True)
    interview_feedback = models.TextField(blank=True, null=True)
    assessment_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    assessment_feedback = models.TextField(blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=[('submitted', 'Submitted'), ('under_review', 'Under Review'), ('rejected', 'Rejected'), ('hired', 'Hired')], default='submitted')
    note = models.TextField(max_length=100, verbose_name='Note')  
    is_active = models.BooleanField(default=False)  
    created_date = models.DateTimeField(default=timezone.now)
    offer_extended = models.BooleanField(default=False)

    offer_accepted = models.BooleanField(default=False)
    offer_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    offer_benefits = models.TextField(blank=True, null=True)

    # def delete(self, *args, **kwargs):
    #     # Delete the associated file from the media folder
    #     if self.resume:
    #         if os.path.isfile(self.resume.path):
    #             os.remove(self.resume.path)
    #     super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
    

# from django.db import models

# class YourModel(models.Model):
#     file_field = models.FileField(upload_to='uploads/')

#     def delete(self, *args, **kwargs):
#         # Delete the associated file from the media folder
#         if self.file_field:
#             if os.path.isfile(self.file_field.path):
#                 os.remove(self.file_field.path)
#         super().delete(*args, **kwargs)
