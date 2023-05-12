from django.shortcuts import render,redirect,get_object_or_404
from companies.models import Employee,CustomUser,comapany_name
from django.contrib.auth.decorators import login_required

@login_required
def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')

        company = request.user.company

        if company:
            employee = Employee.objects.create(company=company, name=name, email=email, department=department)
            employee.save()
            return redirect('/ex')
        else:
            error_message = "You are not associated with any company."
    else:
        error_message = None

    return render(request, 'create_employee.html', {'error_message': error_message})

def employee_list(request):
    if request.user.is_authenticated:
        company = request.user.company

        if company:
            employees = Employee.objects.filter(company=company)
        else:
            employees = []
    else:
        employees = []

    return render(request, 'employee_list.html', {'employees': employees})

@login_required
def all_employees(request):
    company = request.user.company
    em = Employee.objects.filter(company=company)

    return render(request,'employee_list.html',{'em':em})