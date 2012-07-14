from django.contrib import admin

from apps.drinkspert.models import Person, Beer, Spirit, Brewery, Bar

admin.site.register(Person)
admin.site.register(Beer)
admin.site.register(Spirit)
admin.site.register(Brewery)
admin.site.register(Bar)