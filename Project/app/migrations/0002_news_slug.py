# Generated by Django 3.1.7 on 2021-07-10 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=11, max_length=127, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]