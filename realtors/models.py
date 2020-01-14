from django.db import models
from datetime import datetime

class Realtor(models.Model):
	name = models.CharField(max_length=50)
	photo = models.ImageField(upload_to='reators/%Y/%m/%d')
	description = models.TextField(blank=True)
	phone = models.CharField(max_length=15)
	email = models.EmailField(max_length=254)
	hire_date = models.DateTimeField(default=datetime.now)
	is_mvp = models.BooleanField(default=False)
	def __str__(self):
		return self.name
