# Generated by Django 3.1.4 on 2020-12-10 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
        ('meals', '0005_auto_20201210_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantmeals',
            name='userprofile_ptr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurants'),
        ),
    ]
