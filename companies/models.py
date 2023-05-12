from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Create and save a new User with the given email and password
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Create and save a new superuser with the given email and password
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class comapany_name(models.Model):
    cid = models.BigAutoField(primary_key=True,null=False)
    name=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f'{self.name}'
class Employee(models.Model):
    company = models.ForeignKey(comapany_name, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.name}'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    company = models.OneToOneField(comapany_name, on_delete=models.CASCADE, null=True, blank=True)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        # Return the full name of the user
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        # Return the short name of the user
        return self.first_name




