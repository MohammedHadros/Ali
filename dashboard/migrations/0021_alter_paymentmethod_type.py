# Generated by Django 4.1.5 on 2023-08-19 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_remove_paymentmethod_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='type',
            field=models.IntegerField(choices=[(100, 'تحويل بنكي'), (200, 'دفع عند الوصول')], verbose_name='نوع وسيلة الدفع'),
        ),
    ]