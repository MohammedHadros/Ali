# Generated by Django 4.1.5 on 2023-08-10 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='package',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='dashboard.season', verbose_name='الباقة'),
            preserve_default=False,
        ),
    ]
