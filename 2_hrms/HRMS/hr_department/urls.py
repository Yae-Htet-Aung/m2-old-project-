from django.urls import path
from hr_department import views

urlpatterns = [
	path('list/', views.list.as_view()),
	path('add/', views.add.as_view()),
	path('update/<int:department_id>/', views.update.as_view()),
	path('detail/<int:department_id>/', views.detail.as_view()),
	path('delete/<int:department_id>/', views.delete.as_view())
]