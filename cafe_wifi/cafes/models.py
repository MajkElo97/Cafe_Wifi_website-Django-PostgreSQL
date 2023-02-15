from django.db import models
from django.urls import reverse


# Create your models here.


class Cafe(models.Model):
    name = models.CharField(max_length=120)
    map_url = models.TextField()
    img_url = models.TextField()
    location = models.CharField(max_length=120)
    has_sockets = models.BooleanField(default=False)
    has_toilet = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    can_take_calls = models.BooleanField(default=False)
    seats = models.DecimalField(max_digits=10, decimal_places=2)
    coffee_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse("cafe-list")
