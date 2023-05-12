from django.db import models
from companies.models import Employee,CustomUser,comapany_name


class Device(models.Model):
    company=models.OneToOneField(comapany_name,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    model_name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DeviceAllocation(models.Model):
    Device=models.ForeignKey(Device,on_delete=models.CASCADE)
    Employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    company = models.ForeignKey(comapany_name, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    checkout_condition = models.CharField(max_length=100, null=True, blank=True)
    return_condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Device: {self.Device.name}, Employee: {self.Employee.name}, Company: {self.company.name}"