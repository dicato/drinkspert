# stardard library imports
import operator

# django imports
from django.http import Http404, HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

# local imports
from apps.drinkspert.models import Person, Beer, Gin


def index(request):
    """
    The homepage.
    """
    return render_to_response('index.html')
    
def people(request):
    """
    Show all people.
    """
    all = Person.objects.all()
    return render_to_response('people.html', {'people': all})

def beers(request):
    """
    Show all beers.
    """
    all = Beer.objects.all()
    return render_to_response('beers.html', {'beers': all})
