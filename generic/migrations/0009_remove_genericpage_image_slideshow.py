# Generated by Django 3.2.9 on 2021-11-12 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0008_genericpage_image_slideshow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genericpage',
            name='image_slideshow',
        ),
    ]
