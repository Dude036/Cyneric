# Generated by Django 3.2 on 2021-06-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_auto_20210510_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='img_source',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
