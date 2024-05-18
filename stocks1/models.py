from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
