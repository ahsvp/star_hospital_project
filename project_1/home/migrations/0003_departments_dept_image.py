# Generated by Django 5.1.1 on 2024-10-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_department_departments'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='dept_image',
            field=models.ImageField(blank=True, null=True, upload_to='departments/images/'),
        ),
    ]
