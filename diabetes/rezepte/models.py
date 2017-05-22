from django.db import models

# Create your models here.
class Receipe(models.Model):
    headline = models.CharField(max_length=254, null=True)
    discription = models.TextField(null=True)
    bePerPortion = models.IntegerField(null=True)
