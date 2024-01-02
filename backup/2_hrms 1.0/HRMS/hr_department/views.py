from django.shortcuts import render, redirect
from django.views import View
from .models import DepartmentModel
from .forms import DepartmentForm


class detail(View):
	def get(self, request, department_id):
		form = DepartmentModel.objects.get(id=department_id)
		return render(request, 'department_detail.html', {'form': form})


class list(View):
	def get(self, request):
		departments = DepartmentModel.objects.all()
		return render(request, 'department_list.html', {'departments': departments})


class add(View):
	def get(self, request):
		form = DepartmentForm()
		return render(request, 'department_create.html', {'form': form})

	def post(self, request):
		form = DepartmentForm(request.POST)
		if form.is_valid():
			print('*** form valid***')
			form.save()
			return redirect('/department/list/')


class update(View):
	def get(self, request, department_id):
		department = DepartmentModel.objects.get(id=department_id)
		form = DepartmentForm(instance=department)
		return render(request, 'department_update.html', {'form': form})

	def post(self, request, department_id):
		department = DepartmentModel.objects.get(id=department_id)
		form = DepartmentForm(request.POST, instance=department)
		if form.is_valid():
			print('*** update form valid ***')
			form.save()
			return redirect('/department/list/')


class delete(View):
	def get(self, request, department_id):
		department = DepartmentModel.objects.filter(id=department_id)
		department.delete()
		return redirect('/department/list/')
