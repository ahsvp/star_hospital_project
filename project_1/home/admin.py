from django.contrib import admin
from .models import Department,Doctor,ContactMessage,Appoinment
# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')  # Fields to display in the admin list view
    search_fields = ('name', 'email', 'subject')  # Enable search functionality on these fields
    list_filter = ('submitted_at',)  # Enable filtering by submission date

admin.site.register(ContactMessage, ContactMessageAdmin)

class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile', 'doctor', 'preferred_date','preferred_time','additional_note','submitted_at')
    search_fields =('full_name', 'email', 'mobile', 'doctor', 'preferred_date','preferred_time','additional_note','submitted_at')
    list_filter =('full_name', 'email', 'mobile', 'doctor', 'preferred_date','preferred_time','additional_note','submitted_at')
admin.site.register(Appoinment,AppoinmentAdmin)
