class EmployeeModel(models.Model):
    employee_id = models.CharField(max_length=10, unique=True, verbose_name='Employee ID')
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email', default='@gmail.com')
    phone_number = models.CharField(max_length=15, verbose_name='Phone Number')

    # department // dept
    # job_title // job
    # salary // job
    # contract_type // contract
    employment_status = models.BooleanField(verbose_name='Active?', default=True)
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
    picture = models.ImageField(verbose_name='Picture', default=None, blank=True, upload_to='employee/')
    
    # ? supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True) // tags
    
    def __str__(self):
        return self.first_name + " " + self.last_name


# ! ContractModel
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