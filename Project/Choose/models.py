from django.db import models

# Create your models here.


class Choose (models.Model):
    description = models.CharField(blank=True,null=True,max_length=127)