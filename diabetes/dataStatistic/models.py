from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class generalView(models.Model):
	counter = models.BigIntegerField(null=True)
	date = models.DateField(default=datetime.now())


class userFormPost(models.Model):
	member = models.ForeignKey(User)
	counter = models.BigIntegerField(null=True)
	date = models.DateField(default=datetime.now())


class userCreateReceipe(models.Model):
	member = models.ForeignKey(User)
	counter = models.BigIntegerField(null=True)
	date = models.DateField(default=datetime.now())
