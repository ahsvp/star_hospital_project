# Generated by Django 5.1.1 on 2024-10-15 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_departments_dept_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Departments',
            new_name='Department',
        ),
    ]
