# Generated by Django 3.1.4 on 2020-12-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20201212_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
