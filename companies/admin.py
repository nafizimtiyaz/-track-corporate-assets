from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,comapany_name,Employee

class CustomUserAdmin(UserAdmin):
    list_display = ('company','email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('company','first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','Employee', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(comapany_name)
admin.site.register(Employee)