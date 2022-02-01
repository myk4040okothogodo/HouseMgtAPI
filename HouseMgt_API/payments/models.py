from django.db import models
from django.conf import settings
#from ..house import House
import moneyed
from djmoney.models.fields import MoneyField
import datetime
from ..building import Building



# Create your models here.

class Payment(models.Model):
    """This class represents rent/utility payments made by the tenants. """

    building = models.OneToOneField(Building,blank=False, null=False, on_delete=models.CASCADE)
    room = models.OneToOneField(House,blank=False, null=False, on_delete=models.CASCADE)
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL,blank=False, null=False, on_delete=models.CASCADE)
    amount_paid = MoneyField(max_digits=10, decimal_places=2, default_currency='KES')
    receipt_no = models.IntergerField(blank=False,null=False)
    date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"{self.receipt_no}"

