# Generated by Django 3.1.7 on 2021-06-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20210625_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='about_image', verbose_name='Sekil'),
        ),
    ]
