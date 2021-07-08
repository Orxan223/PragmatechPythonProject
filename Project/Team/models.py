from django.db import models

# Create your models here.
# ---------------------------------------      Team     ----------------------------------
#


class Team(models.Model):
    image = models.ImageField('Sekil', upload_to='team_image')
    name = models.CharField(blank=True, null=True, max_length=150)
    profession = models.CharField(blank=True, null=True, max_length=150)
