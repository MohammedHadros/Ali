# Generated by Django 4.1.5 on 2023-09-03 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_alter_hotel_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='location',
        ),
    ]
