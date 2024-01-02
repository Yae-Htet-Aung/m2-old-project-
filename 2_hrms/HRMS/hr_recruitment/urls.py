from django.urls import path
from hr_recruitment import views

urlpatterns = [
    path('list/', views.resume_list.as_view(), name='resume_list'),
    path('add/', views.resume_add.as_view(), name='resume_add'),
    path('update/<int:pk>/', views.resume_update.as_view(), name='resume_update'),
    path('delete/<int:pk>/', views.resume_delete.as_view(), name='resume_delete'),
    path('detail/<int:pk>/', views.resume_detail.as_view(), name='resume_detail')
    # path('domain_name/<primary_key>/', file_name.class_name.as_view(), name='nickname')
]

# pk = primary key, fk = foreign key

# ? name == url_name == success_url (from views)

# ? pk resume_list >> 
# <a href=" {% url 'resume_detail' pk=resume.id %}"> 
#           {% url 'nickname' pk=resume.id %} 
# OR action="/resume_detail/{{ form.instance.id }}"

# ? domain_name >> header's href
# <a href="/recruitment/list">