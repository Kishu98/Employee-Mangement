# Generated by Django 3.1.7 on 2021-05-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0002_employee_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
