from django.urls import path
from hr_contract import views

urlpatterns = [
    path('list/', views.list),
    path('add/', views.add),
    path('detail/<int:contract_id>/', views.detail),
    path('update/<int:contract_id>/',views.update),
    path('delete/<int:contract_id>/', views.delete)
]