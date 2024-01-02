from django.urls import path
from hr_job import views

urlpatterns = [
    path('list/', views.list),
    path('add/', views.add),
    path('detail/<int:job_id>/', views.detail),
    path('update/<int:job_id>/', views.update),
    path('delete/<int:job_id>/', views.delete)
]
