# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_person, name='add_person'),
    path('retrieve/', views.retrieve_persons, name='retrieve_persons'),
]
