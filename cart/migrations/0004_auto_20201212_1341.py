# Generated by Django 3.1.4 on 2020-12-12 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20201212_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total_amount',
            new_name='total',
        ),
    ]
