# Generated by Django 3.0.6 on 2020-06-16 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_device_temp_temp_dev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temp',
            old_name='Device_code',
            new_name='Device_id',
        ),
        migrations.RenameField(
            model_name='temp',
            old_name='Employee_name',
            new_name='Employee_id',
        ),
    ]
