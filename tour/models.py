from django.db import models

# Create your models here.


class Tour(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    details = models.TextField()
    img = models.ImageField()
    offer = models.BooleanField(default=False)