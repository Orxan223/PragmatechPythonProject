# Generated by Django 3.1.7 on 2021-07-08 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210702_0338'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
    ]
