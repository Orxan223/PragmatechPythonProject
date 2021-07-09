from django.db import models

# Create your models here.
class Work(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150)
    description =  models.CharField(blank=True, null=True, max_length=150)
