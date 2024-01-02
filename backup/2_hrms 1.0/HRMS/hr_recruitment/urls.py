from django.urls import path
from hr_recruitment import views

urlpatterns = [
    path('list/', views.list.as_view(), name='list'),
    path('add/', views.add.as_view(), name='add'),
    path('update/<int:pk>/', views.update.as_view(), name='update'),
    path('delete/<int:pk>/', views.delete.as_view(), name='delete'),
    path('details/<int:pk>/', views.detail.as_view(), name='detail')
    # path('domain_name/', file_name.class_name.as_view(), name='url_name')
    # name='nickname'
]
# pk = primary key, fk = foreign key
# see resume list .html for pk
# domain_name = header's href,
# name = success_url 
# {% url 'detail' pk=resume.id %} from list // detail = url_name
