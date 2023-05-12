from django.contrib import admin
from django.urls import path
from employee import views


urlpatterns = [
    path('add-employee', views.add_employee, name='adde'),
    path('company/all/employees/', views.all_employees, name='allem'),
    
]
