# Generated by Django 3.0.2 on 2020-03-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0010_auto_20200314_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigntech',
            name='employee',
            field=models.ManyToManyField(to='employee_register.Employee'),
        ),
    ]
