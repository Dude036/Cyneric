# Generated by Django 3.2.6 on 2022-10-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0014_town_img_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('ac', models.IntegerField(default=0)),
                ('hp', models.IntegerField(default=0)),
                ('initiative', models.IntegerField(default=0)),
            ],
        ),
    ]