from django.db import models
from django.utils import timezone


class EmployeeModel(models.Model):
    employee_id = models.CharField(max_length=10, unique=True, verbose_name='Employee ID')
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email', default='@gmail.com')
    phone_number = models.CharField(max_length=15, verbose_name='Phone Number')

    # department
    # job_title
    employment_status = models.BooleanField(verbose_name='Active?', default=True)
    #? supervisor
    bank_account = models.CharField(max_length=20, verbose_name='Bank Account')
    bank_name = models.CharField(max_length=50, verbose_name='Bank Name')

    joining_date = models.DateField(verbose_name='Joining Date', default=timezone.now)
    #contract_type
    identity_number = models.CharField(max_length=30, verbose_name='Identity Number')
    address = models.CharField(max_length=200, verbose_name='Address')
    marital_status = models.CharField(max_length=10, verbose_name='Marital Status', default='Single')
    
    date_of_birth = models.DateField(verbose_name='Date of Birth', default=timezone.now)
    age = models.IntegerField(verbose_name='Age')
    gender = models.CharField(max_length=10, verbose_name='Gender', default='Other')
    citizen = models.CharField(max_length=50, verbose_name='Citizen', default='Myanmar')
    picture = models.ImageField(verbose_name='Picture', default=None, upload_to='employee/')
    
    # ? supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    # ! department
    # department = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    # ! contract
    # salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salary')
    # contract_type = models.CharField(max_length=20, default='Permanent')
    # ! job
    # job_title = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

# ! foreign keys: department, contract