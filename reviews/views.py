from django.shortcuts import render
from .models import Review, User


def all_reviews(request):
    review = Review.objects.all()
    
    context = {
        'review': review
    }

    return render (request, 'reviews/index.html', context)
