# Generated by Django 3.2 on 2023-04-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0015_initentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='initentry',
            name='conditions',
            field=models.TextField(blank=True, default=''),
        ),
    ]