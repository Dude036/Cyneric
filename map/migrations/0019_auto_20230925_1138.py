# Generated by Django 3.2 on 2023-09-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0018_vehicleentry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Critical',
        ),
        migrations.AddField(
            model_name='schedule',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]