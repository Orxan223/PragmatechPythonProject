from django.db import models
# Create your models here.


class About(models.Model):
    title = models.CharField(blank=True,null=True,max_length=150)
    text =models.TextField(blank=True,null=True)
    image = models.ImageField('Image',upload_to = 'about_image')



    def __str__(self):
        return self.title