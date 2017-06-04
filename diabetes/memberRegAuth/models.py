from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class regUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

