from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import CustomUser,comapany_name,Employee



def myhome(request):
    return render(request,'home.html')


@login_required
def example(request):
    a=Employee.objects.all()
    return render(request,'ex.html',{'a':a})


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        companyName = request.POST['company']

        if email and password1 and password1 == password2 and first_name and last_name:
            # Create the CustomUser instance
            user = CustomUser(email=email, first_name=first_name, last_name=last_name)
            user.set_password(password1)
            user.save()

            # Create the company instance
            company = comapany_name.objects.create(name=companyName)

            # Assign the company to the user
            user.company = company
            user.save()

            return redirect('/login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/ex') 
        else:
            error_message = 'Invalid email or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

@login_required()
def logout1(request):
    auth.logout(request)
    return redirect('/login')


def company_name(request):
    if request.method =='POST':
        name=request.POST['cname']

        name1=comapany_name(name=name)
        name1.save()
        return redirect('/login')
    else:
        return render(request,register.html)