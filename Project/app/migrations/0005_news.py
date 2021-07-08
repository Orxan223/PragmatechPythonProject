# Generated by Django 3.1.7 on 2021-07-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210708_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(upload_to='News_image', verbose_name='Sekil')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
                'ordering': ('-created_at',),
            },
        ),
    ]
