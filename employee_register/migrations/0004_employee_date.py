# Generated by Django 3.1.7 on 2021-05-02 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0003_employee_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
