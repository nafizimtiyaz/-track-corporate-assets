from datetime import datetime
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages 
from assets.models import Device,DeviceAllocation
from companies.models import Employee,comapany_name


def create(request):
    if request.method=='POST':
        name=request.POST['name']
        model_name=request.POST['model_name']

        company = request.user.company
        if company:
            employee = Device.objects.create(company=company, name=name, model_name=model_name)
            employee.save()
            return redirect('/ex')
        else:
            error_message = "You are not associated with any company."
    return render(request,'cde.html')


def device_list(request):
    if request.user.is_authenticated:
        company = request.user.company

        if company:
            em = Device.objects.filter(company=company)
        else:
            em = []
    else:
        em = []

    return render(request, 'dlist.html', {'em': em})

def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    return render(request, 'device_detail.html', {'device': device})

def device_checkout(request, device_id):
    device = Device.objects.get(id=device_id)
    company = request.user.company
    employees = Employee.objects.filter(company=company)

    if request.method == 'POST':
        checkout_condition = request.POST.get('condition')
        selected_employee = request.POST.get('employee')

        if checkout_condition and selected_employee:
            employee = employees.get(name=selected_employee)
            allocation = DeviceAllocation.objects.create(
                Device=device,
                Employee=employee,
                company=company,
                checkout_date=datetime.now(),
                checkout_condition=checkout_condition
            )
            return redirect('device_detail', device_id=device_id)
        else:
            messages.error(request, 'Please provide the checkout condition and select an employee.')

    return render(request, 'device_checkout.html', {'device': device, 'employees': employees})

def device_return(request, device_id):
    device = Device.objects.get(id=device_id)
    if request.method == 'POST':
        allocation = DeviceAllocation.objects.get(Device=device, return_date=None)
        allocation.return_date = datetime.now()
        allocation.return_condition = request.POST['return_condition']
        allocation.save()
        return redirect('device_detail', device_id=device_id)
        
    else:
        return render(request, 'device_return.html', {'device': device})