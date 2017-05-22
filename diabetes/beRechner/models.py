from django.db import models


# Create your models here.
class be(models.Model):
	what = models.CharField(max_length=254)
	bePerHundretGr = models.DecimalField(max_digits=3, decimal_places=2)
