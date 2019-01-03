from django.db import models

# Create your models here.

class GitUser(models.Model):
	search_query = models.CharField(max_length=120)