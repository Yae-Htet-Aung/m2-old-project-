from django.db import models
from datetime import datetime, timezone


def next2months():
    return datetime.now().replace(month=datetime.now().month + 2)
def today():
    return datetime.now()

class JobModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Job Title')
    description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()
    employment_type = models.CharField(default='Full-Time', max_length=20, choices=[
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
        ('Temporary', 'Temporary'),
        ('Internship', 'Internship'),
    ])

    location = models.CharField(max_length=200, default='Yangon')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateTimeField(default=today)
    # open_date = models.DateField(verbose_name='Open Date', default=timezone.now, auto_now_add=True)
    application_deadline = models.DateField(default=next2months)
    is_active = models.BooleanField(default=True)
    
    # Company Information
    company_name = models.CharField(max_length=100, default='yaehrms')
    company_description = models.TextField(blank=True, null=True)
    company_website = models.URLField(blank=True, null=True, default='yaehrms.com')
    
    # Contact Information
    contact_name = models.CharField(max_length=100, blank=True, null=True, default='HR Department')
    contact_email = models.EmailField(default='yaehrms@gmail.com')
    contact_phone = models.CharField(max_length=20, default='09111222333')
    
    # Additional Information
    benefits = models.TextField(blank=True, null=True, default='Meal allowance, Ferry, Bonus')
    additional_information = models.TextField(blank=True, null=True, default='Additional Information')

    # ! department = models.CharField(max_length=100)
    def __str__(self):
        return self.title
