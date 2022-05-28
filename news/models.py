from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Month(models.TextChoices):
	# Spring
	Birth = 'Genysi'
	Melting = 'Tixyl'
	Roots = 'Rysumas'
	# Summer
	Bloom = 'Anthys'
	Apex = 'Perigree'
	Fruiting = 'Ekarpo'
	# Fall
	Play = 'Ludere'
	Reap = 'Therismo'
	Death = 'Chima'
	# Winter
	Darkness = 'Skotad'
	Bottom = 'Apogee'
	Ice = 'Pagos'


class Era(models.TextChoices):
	# Era's last 100 years, with a rotating leadership
	First_Age = 'Uniting'			# Starts with Elves
	Second_Age = 'Trade'			# Then Dwarves
	Third_Age = 'Expansion'			# Then Humans
	Fourth_Age = 'Magic'
	Fifth_Age = 'Wealth'
	Sixth_Age = 'War' 				# Cithrel and Ciphers
	Seventh_Age = 'Golden'			# High Fantasy Steampunk
	Eight_Age = 'Calamity'			# Next Campaign!
	Ninth_Age = 'Restoration'
	Tenth_Age = 'Industry'
	Eleventh_Age = 'Modern'
	Twelfth_Age = 'Technology'


class Article(models.Model):
	title = models.CharField(max_length=50, default='')
	article = models.TextField(default='')

	day = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(28)])
	month = models.CharField(max_length=20, choices=Month.choices, default=Month.Birth)
	year = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
	era = models.CharField(max_length=20, choices=Era.choices, default=Era.Sixth_Age)

	def __repr__(self):
		return self.title + ": " + str(self.day) + '/' + str(list(Month).index(self.month)) + '/' + str(self.year) + 'E' + str(list(Era).index(self.era))

	def __str__(self):
		return self.title + ": " + str(self.day) + '/' + str(list(Month).index(self.month)) + '/' + str(self.year) + 'E' + str(list(Era).index(self.era))
