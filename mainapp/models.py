from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class Tour(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    tour_days = models.PositiveIntegerField()
    picture = models.ImageField(upload_to='tours/')

    def __str__(self):
        return self.city + ", " + self.country
