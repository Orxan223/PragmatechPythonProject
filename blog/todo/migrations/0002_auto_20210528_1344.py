# Generated by Django 3.1.7 on 2021-05-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='completed',
            field=models.BooleanField(blank=True, null=True, verbose_name='Tamamlandi'),
        ),
    ]
