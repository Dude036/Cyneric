# Generated by Django 3.2 on 2021-04-29 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_alter_town_leader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Critical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Magic', 'Magic'), ('Slashing', 'Slashing'), ('Piercing', 'Piercing'), ('Bludgeoning', 'Bludgeoning')], default='Magic', max_length=15)),
                ('severity', models.CharField(choices=[('Extreme', 'Extreme'), ('Moderate', 'Moderate'), ('Mild', 'Mild')], default='Mild', max_length=15)),
                ('success', models.BooleanField(default=True)),
                ('flavor_text', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
