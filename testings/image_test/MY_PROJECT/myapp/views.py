from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_people')
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

def show_people(request):
    people = Person.objects.all()
    return render(request, 'show_people.html', {'people': people})
