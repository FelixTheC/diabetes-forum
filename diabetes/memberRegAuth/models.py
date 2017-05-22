from django.db import models
from django.contrib.auth import user
from datetime import datetime


# Create your models here.
class ForumEintrag(models.Model):
	class Meta:
		verbose_name_plural = 'Forum contents'

	member = models.ForeignKey(user)
	text = models.TextField()
	datum = models.DateField(default=datetime.now())
