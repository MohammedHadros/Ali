# Generated by Django 4.1.5 on 2023-08-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='updated_at',
            new_name='updated',
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_number',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
