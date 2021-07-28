from django.db import models

# Create your models here.


class Register(models.Model):
    full_name = models.CharField(blank=True, null=True, max_length=150)
    last_name = models.CharField(blank=True, null=True, max_length=150)
    username = models.CharField(blank=True, null=True, max_length=150)
    email = models.EmailField(blank=True, null=True, max_length=150)
    password1 = models.IntegerField(blank=True, null=True)
    password2 = models.IntegerField(blank=True, null=True)