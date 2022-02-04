from django.db import models
from django.conf import settings

from ..building.models import Building

class House(models.Model):
    """A single unit in a building that houses the tenant"""

    building = models.OneToOneField(Building,blank=False, null=False, on_delete=models.CASCADE)
    room_no = models.IntegerField(blank=False,null=False)
    floor_no = models.IntegerField(blank=False, null=False)
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="room_tenant" on_delete=models.CASCADE)
    occupied = models.BooleanField(default=False)



    def __str__(self):
        return self.building + self.room_no
