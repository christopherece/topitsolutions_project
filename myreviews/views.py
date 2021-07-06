from django.shortcuts import get_object_or_404, render

from .models import Myreview


# Create your views here.
def index(request):
    reviews = Myreview.objects.all()
    context = {
        'reviews':reviews
    }
    return render(request, 'myreviews/myreviews.html', context)

def myreview(request, review_id):
    review = get_object_or_404(Myreview, pk=review_id)
    context = {
        'review':review
    }
    return render(request, 'myreviews/myreview.html', context)

def search(request):
    return render(request, 'myreviews/searchreview.html')
