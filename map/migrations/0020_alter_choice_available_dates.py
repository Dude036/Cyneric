# Generated by Django 3.2 on 2023-09-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0019_auto_20230925_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='available_dates',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
