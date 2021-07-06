from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myreviews/myreviews.html')

def myreview(request):
    return render(request, 'myreviews/myreview.html')

def search(request):
    return render(request, 'myreviews/searchreview.html')
