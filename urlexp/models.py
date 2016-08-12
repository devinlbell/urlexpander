from django.db import models

# Create your models here.
class urlInfo(models.Model):
	short = models.URLField(max_length=500)
	expanded = models.URLField(max_length=500)
	status = models.CharField(max_length=20)
	title = models.CharField(max_length=200)
	waybackUrl = models.CharField(max_length=500)
	waybackTime = models.CharField(max_length=500)

