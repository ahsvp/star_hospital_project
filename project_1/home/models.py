from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField()
    dept_image = models.ImageField(upload_to='departments/images/', blank=True, null=True)

    def __str__(self):
        return self.dept_name
class Doctor(models.Model):
    name = models.CharField(max_length=100)  # Doctor's full name
    specialty = models.CharField(max_length=100)  # Area of specialization
    experience_years = models.PositiveIntegerField()  # Years of experience
    contact_email = models.EmailField()  # Contact email
    bio = models.TextField()  # Brief biography
    image = models.ImageField(upload_to='doctors/images/', blank=True, null=True)  # Profile image

    def __str__(self):
        return self.name  # Returns the doctor's name when the object is represented
# models.py

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} - {self.subject}'

class Appoinment(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Full Name')
    email = models.EmailField(verbose_name='Email Address')
    mobile = models.CharField(max_length=10, verbose_name='Mobile Number')
    doctor = models.CharField(max_length=255, verbose_name='Doctor')
    preferred_date = models.DateField(verbose_name='Preferred Date')
    preferred_time = models.TimeField(verbose_name='Preferred Time')
    additional_note = models.TextField(verbose_name='Additional Note')
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name='Submitted At')

def __str__(self):
    return f'Full Name: {self.full_name}, Email: {self.email}, Mobile: {self.mobile}, Doctor: {self.doctor}, Preferred Date: {self.preferred_date}, Preferred Time: {self.preferred_time}, Additional Note: {self.additional_note}, Submitted At: {self.submitted_at}'


    