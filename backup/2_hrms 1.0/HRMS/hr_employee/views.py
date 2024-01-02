from django.shortcuts import render
# import os
from django.shortcuts import render, redirect
from hr_employee.models import EmployeeModel
# from datetime import datetime


def list(request):
    if request.method == "GET":
        employees = EmployeeModel.objects.all()
        context = {'employees': employees}
        return render(request, 'employee_list.html', context)


def detail(request, employee_id):
    if request.method == 'GET':
        employee = EmployeeModel.objects.get(id=employee_id)
        data = {'employee': employee}
        return render(request, 'employee_detail.html', data)


def add(request):
    if request.method == 'GET':
        employee = EmployeeModel()
        return render(request, 'employee_add.html', {'employee': employee})
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        # department = request.POST['department']
        # job_title = request.POST['job_title']
        # ! employment_status
        if request.POST.get('employment_status') == 'on':
            employment_status = True
        else:
            employment_status = False
        # salary = request.POST['salary']
        bank_account = request.POST['bank_account']
        bank_name = request.POST['bank_name']
        joining_date = request.POST['joining_date']
        # contract_type = request.POST['contract_type']
        identity_number = request.POST['identity_number']
        address = request.POST['address']
        marital_status = request.POST['marital_status']
        date_of_birth = request.POST['date_of_birth']
        age = request.POST['age']
        gender = request.POST['gender']
        citizen = request.POST['citizen']
        # picture = request.FILES['picture']
        picture = request.FILES.get('picture')
        
        # if picture == None:
        #         picture = "default"
        # else:
        #     picture = picture
        # picture = request.FILES.get('picture')

        data = EmployeeModel.objects.create(
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            # department=department,
            # job_title=job_title,
            employment_status=employment_status,
            # salary=salary,
            bank_account=bank_account,
            bank_name=bank_name,
            joining_date=joining_date,
            # contract_type=contract_type,
            identity_number=identity_number,
            address=address,
            marital_status=marital_status,
            date_of_birth=date_of_birth,
            age=age,
            gender=gender,
            citizen=citizen,
            picture=picture
        )
        data.save()
        return redirect('/employee/list/')


def update(request, employee_id):
    # print('update_employee CALL')
    employee = EmployeeModel.objects.get(id=employee_id)
    if request.method == 'GET':
        # print('update_employee GET CALL')
        employee.date_of_birth = str(employee.date_of_birth)
        employee.joining_date = str(employee.joining_date)
        data = {'employee': employee}
        return render(request, 'employee_update.html', data)

    if request.method == 'POST':
        employee.employee_id = request.POST.get('employee_id')
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.email = request.POST.get('email')
        employee.phone_number = request.POST.get('phone_number')
        # employee.department = request.POST.get('department')
        # employee.job_title = request.POST.get('job_title')
        if request.POST.get('employment_status') == 'on':
            employment_status = True
        else:
            employment_status = False
        # employee.salary = request.POST.get('salary')
        employee.bank_account = request.POST.get('bank_account')
        employee.bank_name = request.POST.get('bank_name')
        employee.joining_date = request.POST.get('joining_date')
        # employee.contract_type = request.POST.get('contract_type')
        employee.identity_number = request.POST.get('identity_number')
        employee.address = request.POST.get('address')
        employee.marital_status = request.POST.get('marital_status')
        employee.date_of_birth = request.POST.get('date_of_birth')
        employee.age = request.POST.get('age')
        employee.gender = request.POST.get('gender')
        employee.citizen = request.POST.get('citizen')
        # if request.FILES.get('picture'):
        #     employee.picture = request.FILES.get('picture')
        picture = request.FILES.get('picture')
        if picture:
            if employee.picture:
                employee.picture.delete()
            employee.picture = picture
        employee.save()
        return redirect('/employee/list/')


def delete(request, employee_id):
    if request.method == "GET":
        print('>>> delete_employee GET call')
        employee = EmployeeModel.objects.get(id=employee_id)
        
        picture = employee.picture
        if picture:
            picture.delete()
        print('>>> employee deleted')
        print('>>>', picture) 

        employee.delete()        
        return redirect('/employee/list/')
