# myapp_html/views.py

from django.shortcuts import render, redirect
from .models import Person


def add_person(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        Person.objects.create(name=name, image=image)
        return redirect('retrieve_persons')
    return render(request, 'add.html')

def retrieve_persons(request):
    persons = Person.objects.all()
    return render(request, 'retrieve_persons.html', {'persons': persons})
