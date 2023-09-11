# Generated by Django 4.1.5 on 2023-08-15 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_paymentmethod_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_methods', to='dashboard.hotel', verbose_name='الفندق'),
        ),
    ]
