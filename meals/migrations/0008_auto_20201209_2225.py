# Generated by Django 3.1.4 on 2020-12-09 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201209_2150'),
        ('meals', '0007_auto_20201209_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantmeals',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
    ]
