from django.shortcuts import get_object_or_404, render

from .models import Review


# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/reviews.html', context)

def review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {
        'review':review
    }

    return render(request, 'reviews/review.html', context)
