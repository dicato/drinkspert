from django.contrib import admin

from apps.drinkspert.models import Person, Beer, Gin, Brewery, Bar

admin.site.register(Person)
admin.site.register(Beer)
admin.site.register(Gin)
admin.site.register(Brewery)
admin.site.register(Bar)