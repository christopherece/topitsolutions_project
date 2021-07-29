from django.shortcuts import get_object_or_404, render

from .models import Portfolio


# Create your views here.
def index(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios':portfolios
    }
    return render(request, 'portfolios/portfolios.html', context)

def portfolio(request, review_id):
    review = get_object_or_404(Portfolio, pk=review_id)
    context = {
        'portfolio':portfolio
    }
    return render(request, 'portfolios/portfolio.html', context)

def search(request):
    return render(request, 'portfolios/searchportfolio.html')
