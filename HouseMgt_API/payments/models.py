from django.db import models
from django.conf import settings
from HouseMgt_API.building import Building
from HouseMgt_API.house import House
import moneyed
from djmoney.models.fields import MoneyField
import datetime



# Create your models here.

class Payment(models.Model):
    building = models.OneToOneField(Building, on_delete=models.CASCADE)
    room = models.OneToOneField(House, on_delete=models.CASCADE)
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Amount_paid = MoneyField(max_digits=10, decimal_places=2, default_currency='KES')
    receipt_no = models.IntergerField(null=False)


    def __str__(self):
        return f"{self.receipt_no}"

