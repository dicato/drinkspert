from django.db import models

# TODO
# Make a model called a 'Purchase' or something.
# This would tie the person to the drink to the location.

class Person(models.Model):
    """
    A drinker.
    """
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    beers = models.ManyToManyField("Beer")

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Drink(models.Model):
    """
    Common base class for all drink types.

    Subclass for Beer, Gin, Vodka, etc.
    
    """
    name = models.CharField(max_length=512)
    
    class Meta:
        # This makes 'Drink' an abstract base class
        abstract = True
    
class Beer(Drink):
    """
    A beer.
    """
    brewery = models.ForeignKey("Brewery")
    style = models.CharField(max_length=256)

    # TODO:
    # Image Field for beer bottle / logo

    def __unicode__(self):
        return self.name


class Gin(Drink):
    """
    Hmm, juniper.
    """
    distiller = models.CharField(max_length=512)

    def __unicode__(self):
        return self.name


class Brewery(models.Model):
    """
    Creator of beers.
    """
    # TODO:
    # Maybe this should be a generic 'owner'
    # so we can reuse it for spirits
    name = models.CharField(max_length=512)

    # TODO:
    # Determine best way to model an address
    address = models.CharField(max_length=512)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Bar(models.Model):
    """
    Where you had a drink. 
    """
    name = models.CharField(max_length=512)

    # TODO:
    # Determine best way to model an address
    address = models.CharField(max_length=512)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.name
