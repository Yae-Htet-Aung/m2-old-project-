from django.shortcuts import render, redirect
from .models import ContractModel
from .forms import ContractForm


def list(request):
    if request.method == "GET":
        contracts = ContractModel.objects.all()
        context = {'contracts': contracts}
        return render(request, 'contract_list.html', context)


def detail(request, contract_id):
    if request.method == 'GET':
        contracts = ContractModel.objects.get(id=contract_id)
        if contracts.attachment == 'default':
            contracts.attachment = 'contract/_default.jpg'
        data = {'contract': contracts}
        return render(request, 'contract_detail.html', data)


def add(request):
    if request.method == "GET":
        print("GET CALLED ***** ")
        form = ContractForm()
        return render(request, 'contract_add.html', {'form': form})

    if request.method == 'POST':
        print('data => ', request.POST)
        form = ContractForm(request.POST, request.FILES)
        print('POST CALLED *****')
        if form.is_valid():
            print('form valid******')
            contract_id = form.cleaned_data.get('contract_id')
            contract_name = form.cleaned_data.get('contract_name')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            contract_type = form.cleaned_data.get('contract_type')

            # department = request.POST['department']
            # job_title = request.POST['job_title']
            contractor_name = form.cleaned_data.get('contractor_name')
            sub_contractor_name = form.cleaned_data.get('sub_contractor_name')
            basic_salary = form.cleaned_data.get('basic_salary')
            salary = form.cleaned_data.get('salary')
            allowed_annual_leave = form.cleaned_data.get(
                'allowed_annual_leave')

            value = form.cleaned_data.get('value')
            status = form.cleaned_data.get('status')
            terminated_date = form.cleaned_data.get('terminated_date')
            terminated_reason = form.cleaned_data.get('terminated_reason')
            note = form.cleaned_data.get('note')

            created_date = form.cleaned_data.get('created_date')
            updated_date = form.cleaned_data.get('updated_date')

            attachment = form.cleaned_data.get('attachment')
            if attachment == None:
                attachment = "default"
            else:
                attachment = attachment

            contract = ContractModel.objects.create(
                contract_id=contract_id,
                contract_name=contract_name,
                start_date=start_date,
                end_date=end_date,
                contract_type=contract_type,

                contractor_name=contractor_name,
                sub_contractor_name=sub_contractor_name,
                basic_salary=basic_salary,
                salary=salary,
                allowed_annual_leave=allowed_annual_leave,

                value=value,
                terminated_date=terminated_date,
                terminated_reason=terminated_reason,
                created_date=created_date,
                updated_date=updated_date,

                note=note,
                status=status,
                attachment=attachment
            )
            contract.save()
            print('SAVE()*****')
            return redirect('/contract/list/')


def update(request, contract_id):
    print('>>> contract update call')
    print('>>> contract_id ', contract_id)
    contract = ContractModel.objects.get(id=contract_id)
    if request.method == "GET":
        print(">>> GET CALL")
        values = {
            'contract_id': contract.contract_id, 
            'contract_name': contract.contract_name,
            'start_date' :contract.start_date,
            'end_date' : contract.end_date,
            'contract_type' : contract.contract_type,

            'contractor_name' : contract.contractor_name,
            'sub_contractor_name' : contract.sub_contractor_name,
            'basic_salary' : contract.basic_salary,
            'salary' : contract.salary,
            'allowed_annual_leave' : contract.allowed_annual_leave,

            'value' : contract.value,
            'terminated_date': contract.terminated_date,
            'terminated_reason': contract.terminated_reason,
            'created_date': contract.created_date,
            'updated_date': contract.updated_date,

            'note' : contract.note,
            'status' : contract.status,
            'attachment' : contract.attachment
        }
        print(">>> values >>> ", values)
        form = ContractForm(initial=values)
        context = {'form': form, 'uploaded_image': contract.attachment, 'contract': contract}
        return render(request, 'contract_update.html', context)
    
    elif request.method == "POST":
        print('>>> update POST CALL')
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            contract.contract_id = form.cleaned_data.get('contract_id')
            contract.contract_name = form.cleaned_data.get('contract_name')
            contract.start_date = form.cleaned_data.get('start_date')
            contract.end_date = form.cleaned_data.get('end_date')
            contract.contract_type = form.cleaned_data.get('contract_type')

            # department = request.POST['department']
            # job_title = request.POST['job_title']
            contract.contractor_name = form.cleaned_data.get('contractor_name')
            contract.sub_contractor_name = form.cleaned_data.get('sub_contractor_name')
            contract.basic_salary = form.cleaned_data.get('basic_salary')
            contract.salary = form.cleaned_data.get('salary')
            contract.allowed_annual_leave = form.cleaned_data.get( 'allowed_annual_leave')

            contract.value = form.cleaned_data.get('value')
            contract.status = form.cleaned_data.get('status')
            contract.terminated_date = form.cleaned_data.get('terminated_date')
            contract.terminated_reason = form.cleaned_data.get('terminated_reason')
            contract.note = form.cleaned_data.get('note')

            contract.created_date = form.cleaned_data.get('created_date')
            contract.updated_date = form.cleaned_data.get('updated_date')

            attachment = form.cleaned_data.get('attachment')

            if attachment:
                if contract.attachment:
                    contract.attachment.delete()
                contract.attachment = attachment

            # if form.cleaned_data.get('attachment'):
            #     contract.attachment = form.cleaned_data.get('attachment')
            # else: 
            #     contract.attachment = "default"
            
            print('FORM UPDATE CALL')
                       
            contract.save()
            return redirect('/contract/detail/' + str(contract_id) + '/')


def delete(request, contract_id):
    print('>>> delete_contract call')
    print('>>> contract_id ', contract_id)
    if request.method == "GET":
        print('>>> delete_contract GET call')
        contract = ContractModel.objects.get(id=contract_id)
        attachment = contract.attachment
        print('>>> ', attachment)
        if attachment != 'default':
            attachment.delete()
            print(">>> attachment deleted! ")
        contract.delete()
        return redirect('/contract/list/')

# def delete(request, employee_id):
#     if request.method == "GET":
#         print('>>> delete_employee GET call')
#         employee = EmployeeModel.objects.get(id=employee_id)

#         picture = employee.picture
#         if picture:
#             picture.delete()
#         print('>>> employee deleted')
#         print('>>>', picture)

#         employee.delete()
#         return redirect('/employee/list/')
