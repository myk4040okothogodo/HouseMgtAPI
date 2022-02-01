from django.db import models
from django.conf import settings
#from ..house.models import House


class Building(models.Model):
    """A building or apartment of mutliple rooms housing tenants."""

    name = models.CharField(max_length=200, blank=False, default='' )
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    careTaker = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #houses = models.ForeignKey(House, on_delete=models.CASCADE)
    dateCommissioned = models.DateField()
    starsRating = models.IntegerField()
    account   = models.IntegerField(blank=False, null=False)


    def __str_(self):
        return f"{self.Name}"

    def building_age():
        pass
