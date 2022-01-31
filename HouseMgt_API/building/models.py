from django.db import models
from django.conf import settings
from HouseMgt_API.house import House


class Building(models.Model):
    name = models.CharField(max_length=200, blank=False )
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    careTaker = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    houses = models.ForeignKey(House, on_delete=models.CASCADE)
    dateCommissioned = models.DateField()
    starsRating = models.IntegerField()
    account   = models.Int


    def __str_(self):
        return f"{self.Name}"

    def building_age():
        pass
