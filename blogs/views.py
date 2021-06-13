from django.shortcuts import get_object_or_404, render

from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog':blog
    }

    return render(request, 'blogs/blog.html', context)
