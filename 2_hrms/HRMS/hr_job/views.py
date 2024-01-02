from django.shortcuts import render, redirect
from .models import JobModel
from .forms import JobForm


def detail(request, job_id):
    if request.method == "GET":
        job = JobModel.objects.get(id=job_id)
        return render(request, 'job_detail.html', {'job': job})


def list(request):
    if request.method == "GET":
        jobs = JobModel.objects.all()
        return render(request, 'job_list.html', {'jobs': jobs})


def add(request):
    if request.method == "GET":
        form = JobForm()
        # print('jonform >>> \n', form, '\n')
        return render(request, 'job_add.html', {'form': form})
    if request.method == "POST":
        print('POST CALLED <<<')
        form = JobForm(request.POST)
    if form.is_valid():
        print('>>> form valid <<<')
        form.save()
        return redirect('/job/list/')


def update(request, job_id):
    job = JobModel.objects.get(id=job_id)
    if request.method == "GET":
        form = JobForm(instance=job)
        return render(request, 'job_update.html', {'form': form})
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            # print('** form valid ***')
            form.save()
            return redirect('/job/list/')


def delete(request, job_id):
    if request.method == "GET":
        job = JobModel.objects.filter(id=job_id)
        job.delete()
        # print('** job deleted ***')
        return redirect('/job/list/')
