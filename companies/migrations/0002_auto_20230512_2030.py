# Generated by Django 3.1 on 2023-05-12 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='companies.comapany_name'),
        ),
    ]
