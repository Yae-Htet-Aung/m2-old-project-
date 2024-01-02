from django.urls import path
from hr_expense import views

urlpatterns = [
    path('list/', views.expense_list.as_view(), name='expense_list'),
    path('add/', views.expense_add.as_view(), name='expense_add'),
    path('update/<int:pk>/', views.expense_update.as_view(), name='expense_update'),
    path('delete/<int:pk>/', views.expense_delete.as_view(), name='expense_delete'),
    path('detail/<int:pk>/', views.expense_detail.as_view(), name='expense_detail')
]