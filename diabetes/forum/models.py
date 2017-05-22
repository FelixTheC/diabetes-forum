from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class ForumEintrag(models.Model):
	class Meta:
		verbose_name_plural = 'Forum contents'

	member = models.ForeignKey(User)
	text = models.TextField(null=True)
	datum = models.DateField(default=datetime.now())

