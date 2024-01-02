from django.db import models
from django.utils import timezone
from datetime import datetime

def next_year():
    return datetime.now().replace(year=datetime.now().year + 1)

class ContractModel(models.Model):
    contract_name = models.CharField(max_length=50, verbose_name='Contract Name')
    contract_id = models.CharField(max_length=30, verbose_name='Contract ID', unique=True)
    start_date = models.DateField(verbose_name='Start Date', default=timezone.now)
    end_date = models.DateField(verbose_name='End Date', default=next_year)
    contract_type = models.CharField(max_length=30)
    
    # department
    # job_title
    rank = models.IntegerField(verbose_name='Rank', default=1)
    terminated_date = models.DateField(blank=True)
    terminated_reason = models.TextField(blank=True)

    status = models.CharField(max_length=20, verbose_name='Status', default='Draft')
    created_date = models.DateTimeField(verbose_name='Create Date', default=timezone.now)
    updated_date = models.DateTimeField( default=timezone.now)
    note = models.TextField(max_length=200, verbose_name='Note', blank=True)
    attachment = models.ImageField(verbose_name='Attachment', upload_to='contract/', blank=True, null=True)
    
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, default=2000, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=2000, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=3000, blank=True)
    allowed_annual_leave = models.IntegerField(blank=True,default=12)
    contractor_name = models.CharField(max_length=100, verbose_name='Contractor Name', blank=True)
    sub_contractor_name = models.CharField(max_length=100, verbose_name='Sub-Contractor Name', blank=True)

    # ! department
    # department = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True)
    # ! job
    # job_title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.contract_name

# ! foreign keys: department, job
# contract_type: Permanent, Intern, Contractor, Sub-contractor
# total_annual_leave: An integer field to store the total annual leave days. 