# Generated by Django 3.2.9 on 2021-11-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_rename_instagrams_socialmediasettings_instagram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='instagram',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
