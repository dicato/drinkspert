# stardard library imports
import operator

# django imports
from django.http import Http404, HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

# local imports
from apps.drinkspert.models import Person, Beer, Gin

