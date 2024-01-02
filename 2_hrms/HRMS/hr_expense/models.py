# from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class ExpenseModel(models.Model):
    
    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=100)
    description = models.TextField()
    reason = models.TextField(max_length=500, blank=True)
    
    claimed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    approved_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null= True)
    currency = models.CharField(max_length=5, default='USD')
    payment_name = models.CharField(max_length=100)
    payment_description = models.TextField(max_length=200)
    payment_date = models.DateField(default=timezone.now)
    
    claimed_date = models.DateField(default=timezone.now)
    approval_date = models.DateField(default=timezone.now)
    receipt_image = models.ImageField(default=None, upload_to='receipt/')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('approved', 'Approved')], default='pending')
    comments = models.TextField()
    
    note = models.TextField(max_length=300, verbose_name='Note', blank=True)
    
    
    def __str__(self):
        return self.name

# foreign keys

# department = models.CharField(max_length=50)
# employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
# employee_id = models.CharField(max_length=10, unique=True)
# approver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='approved_expenses')