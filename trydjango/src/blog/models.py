from django.db import models

# Create your models here.

class BlogPost(models.Model):
	# id = models.IntegerField() # pk
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	content = models.TextField(null=True, blank=True)

