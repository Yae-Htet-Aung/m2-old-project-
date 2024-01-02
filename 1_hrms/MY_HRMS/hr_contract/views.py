from django.shortcuts import render, redirect
from .models import ContractModel
from .forms import ContractForm

def list(request):
    if request.method == "GET":
        contracts = ContractModel.objects.all()
        context = {'contracts': contracts}
        return render(request,'contract_list.html', context)
    

def detail(request, contract_id):
    if request.method == 'GET':
        contracts = ContractModel.objects.get(id=contract_id)
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
            allowed_annual_leave = form.cleaned_data.get('allowed_annual_leave')

            value = form.cleaned_data.get('value')
            status = form.cleaned_data.get('status')
            terminated_date = form.cleaned_data.get('terminated_date')
            terminated_reason = form.cleaned_data.get('terminated_reason')
            note = form.cleaned_data.get('note')

            created_date = form.cleaned_data.get('created_date')
            updated_date = form.cleaned_data.get('updated_date')
            attachment = form.cleaned_data.get('attachment')
            # print('********************', attachment)
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
                created_date= created_date,
                updated_date=updated_date,

                note=note,
                status=status,
                attachment=attachment
            )
            contract.save()
            print('SAVE()*****')
            return redirect('/contract/list/')


