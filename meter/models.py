from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Meter(models.Model):
    # Meter numbers have a length of 11
    meter_no = models.CharField("Meter Number", max_length=11, unique=True)
    manufacturer = models.CharField("Meter Manufacturer", max_length=255)
    # If a manager is deleted the meter will not be deleted, instead it will be retained
    manager = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.meter_no



class TokenHistory(models.Model):
    # From the decision reached, the name field is not necessary, and thus it is allowed to have NULL values
    name = models.CharField("Purchaser's Name", max_length=255, null=True)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.PROTECT)
    token_no = models.PositiveIntegerField(unique=True)
    # Automatically populate with the current date and time 
    purchased_at = models.DateTimeField(auto_now_add=True)
    # Meter for which token was generated
    meter = models.ForeignKey(Meter, on_delete=models.PROTECT)


    def __str__(self):
        return self.name
