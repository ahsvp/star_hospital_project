from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Department,Doctor,ContactMessage,Appoinment

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        print("POST request received")  # Debugging line
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new contact message instance
        contact_message = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        try:
            contact_message.save()  # Save to the database
            print("Contact message saved:", contact_message)  # Debugging line
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            print("Contact message not saved. Error:", e)  # Debugging line

        return redirect('contact')
    else:
        # This block executes if the request method is not POST
        print("POST request not received (GET or other). Rendering the form.")  # Debugging line

    return render(request, 'contact.html')

def booking(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile = request.POST.get('phone')
        doctor = request.POST.get('doctor')
        preferred_date = request.POST.get('date')
        preferred_time = request.POST.get('time')
        additional_note = request.POST.get('message')

        # Create a new appointment instance
        try:
            appointment = Appoinment(
                full_name=full_name,
                email=email,
                mobile=mobile,
                doctor=doctor,
                preferred_date=preferred_date,
                preferred_time=preferred_time,
                additional_note=additional_note
            )
            appointment.save()  # Save to the database
            messages.success(request, 'Your appointment has been booked successfully!')
        except Exception as e:
            messages.error(request, f'Error booking appointment: {e}')

        return redirect('booking')  # Redirect after successful submission

    return render(request, 'booking.html')  # Render the form template

def doctor(request):
    doctors = Doctor.objects.all() 
    return render(request,'doctor.html', {'doctors': doctors})
def department(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})
def practice(request):
    return render(request,'practice.html')