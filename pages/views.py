from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'blogs':blogs
    }

    return render(request,'pages/index.html', context)

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')