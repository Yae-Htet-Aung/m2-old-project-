# Generated by Django 2.2 on 2023-09-11 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_department', '0002_auto_20230911_1540'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='DepartmentModel',
        ),
    ]
