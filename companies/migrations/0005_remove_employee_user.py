# Generated by Django 3.1 on 2023-05-12 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
    ]