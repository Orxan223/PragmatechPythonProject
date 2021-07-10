from django.db import models
from django.urls import reverse
# Create your models here.
# ---------------------------------------      News     ----------------------------------

    # News settles in this stock


class News(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    short_description =  models.CharField(blank=True, null=True, max_length=150)
    slug = models.SlugField('Slug',max_length=150)
    image = models.ImageField('Sekil', upload_to='Blog_image')
    pese = models.ForeignKey('Pese', on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('news_detail',args=[self.slug])


class Pese(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150)

    def __str__(self):
        return self.name
