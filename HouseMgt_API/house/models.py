from django.db import models
from HouseMgt_API.building import Building
from django.conf import settings
# Create your models here.


class House(models.Model):
    building = models.OneToOneField(Building, on_delete=models.CASCADE)
    room_no = models.IntegerField(null=False)
    floor_no = models.IntegerField(null=False)
    tenant = models.ForeignKey(setting.AUTH_USER_MODEL, on_delete=models.CASCADE)

