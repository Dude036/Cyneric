from django.db import models


# Create your models here.
class Town(models.Model):
    name = models.CharField(default='', max_length=50)
    description = models.TextField(default='')
    government = models.TextField(default='')
    governing_body = models.CharField(default='', max_length=200)
    economy = models.TextField(default='')
    population = models.BigIntegerField(default=0)
    x_coord_max = models.IntegerField(default=0)
    y_coord_max = models.IntegerField(default=0)
    x_coord_min = models.IntegerField(default=0)
    y_coord_min = models.IntegerField(default=0)


class Person(models.Model):
    name = models.CharField(default='', max_length=50)
    title = models.CharField(default='', max_length=50)
    description = models.TextField(default='')
    leader = models.ForeignKey(Town, on_delete=models.CASCADE)
