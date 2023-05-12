from django.contrib import admin
from django.urls import path
from assets import views


urlpatterns = [
    path('creat',views.create,name="cr"),
    path('devices/', views.device_list, name='device_list'),
    path('device/<int:device_id>/', views.device_detail, name='device_detail'),
    path('device/<int:device_id>/checkout/', views.device_checkout, name='device_checkout'),
    path('device/<int:device_id>/return/', views.device_return, name='device_return'),
]
