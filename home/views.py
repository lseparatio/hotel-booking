from django.shortcuts import render
from settings.models import IndexPage, TopNav

def index(request):
    """A view to return the index page"""
    
    if 'ro' in request.LANGUAGE_CODE:
        topnav = TopNav.objects.language('ro').all()
        index = IndexPage.objects.language('ro').all()
    else:
        topnav = TopNav.objects.language('en').all()
        index = IndexPage.objects.language('en').all()


    context = {
        'topnav' : topnav,
        'index' : index,
    }

    return render(request, 'home/index.html', context)
