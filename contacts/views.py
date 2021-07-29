from contacts.models import Contact
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'contacts/index.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']

    #check for redundant

    admin_info = User.objects.get(is_superuser=True)
    admin_email = admin_info.email

    send_mail(
        'Inquiry',
        'You have a new inquiry. Please login to your admin panel to read the message',
        'christopheranchetaece@gmail.com',
        [admin_email],
        fail_silently=False,
    )

    contactus = Contact(name=name, phone=phone, 
                email=email, message=message, 
                )

    contactus.save()

    messages.success(request, 'Your inquiry has been submitted, we will get back to you soon')
    return redirect('/contacts')