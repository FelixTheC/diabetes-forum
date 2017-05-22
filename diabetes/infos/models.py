from django.db import models
from datetime import datetime

# Create your models here.
class Info(models.Model):
	headline = models.CharField(max_length=254, null=True)
	content = models.TextField(null=True)
	datum = models.DateField(default=datetime.now())