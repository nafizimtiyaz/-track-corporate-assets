from django.contrib import admin
from django.urls import path,include
from companies import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.myhome,name="home"),
    path('ex',views.example,name="ex"),
    path('register',views.register,name="regi"),
    path('login',views.user_login,name="logs"),
    path('logout',views.logout1,name="out"),
    path('ok',views.comapany_name,name="name"),
    path('employee/',include("employee.urls")),
    path('assets/',include("assets.urls")),
]


