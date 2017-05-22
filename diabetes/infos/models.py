from django.db import models
from datetime import datetime

# Create your models here.
class Info(models.Model):
	headline = models.CharField(max_length=254)
	content = models.TextField()
	datum = model.DateField(default=datetime.now())