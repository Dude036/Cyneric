# Generated by Django 3.2 on 2021-04-20 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_town_generator_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='town',
            name='generator_settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='map.generatorshop'),
        ),
    ]
