from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'services/services.html')

def computer_laptop_repair(request):
    return render(request,'services/computer_laptop_repair.html')

def computer_laptop_upgrade(request):
    return render(request,'services/computer_laptop_upgrade.html')

def iot(request):
    return render(request,'services/iot.html')

def networking(request):
    return render(request,'services/networking.html')

def webdevelopment(request):
    return render(request,'services/webdevelopment.html')
