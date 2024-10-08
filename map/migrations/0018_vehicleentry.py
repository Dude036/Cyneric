# Generated by Django 3.2 on 2023-09-21 22:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0017_choice_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('entity', models.CharField(choices=[['Train', 'Murder Train (Engine)'], ['Lab', 'Murder Train (Lab)'], ['Sleeper', 'Murder Train (Passenger Car)'], ['Planar_Skiff', 'Icarus'], ['Mobile_Inn', 'Murder Bus'], ['Speedster_1', 'Magicycle 1'], ['Speedster_2', 'Magicycle 2'], ['Inventory', 'Inventory']], default=None, max_length=20, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, default='', max_length=1000)),
                ('content', models.TextField(blank=True, default='')),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
