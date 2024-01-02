from django.db import models
from datetime import datetime
from django.utils import timezone

def next_year():
    return datetime.now().replace(year=datetime.now().year + 1)

class DepartmentModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    # manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, related_name='managed_department', blank=True, null=True)
    # parent_department = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    total_employees = models.CharField(max_length=20, verbose_name='Total Employees', default=None)
    
    created_date = models.DateField(default=timezone.now)
    updated_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, verbose_name='Status', default='Running Project')
    is_active = models.BooleanField(verbose_name='Is Active', default=False)
    project_name = models.CharField(max_length=300, verbose_name='Ongoing Project Name', blank=True, null=True)
    
    deadline = models.DateTimeField(default= next_year, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True, default='Yankin Township, Myanmanr Center')
    city = models.CharField(max_length=100, blank=True, null=True, default='Yangon')
    state = models.CharField(max_length=100, blank=True, null=True, default='Yangon Division')
    postal_code = models.CharField(max_length=20, blank=True, null=True, default='11081')
    
    country = models.CharField(max_length=100, blank=True, null=True, default='Myanmar')
    phone = models.CharField(max_length=20, blank=True, null=True, default='09111000111')
    email = models.EmailField(max_length=255, blank=True, null=True, default='dept@gmail.com')
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True, null=True)
    custom_field = models.TextField(blank=True, null=True)
    # employees = models.ManyToManyField('Employee', related_name='departments')

    def __str__(self):
        return self.name
    

