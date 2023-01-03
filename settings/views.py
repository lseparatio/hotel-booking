from django.shortcuts import render
from .models import SiteSettings


def all_reviews(request):
    review = SiteSettings.objects.all()
    
    context = {
        'SiteSettings': SiteSettings
    }

    return render (request, 'settings/index.html', context)