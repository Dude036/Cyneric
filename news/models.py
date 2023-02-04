from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from enum import Enum


# Create your models here.
class Month(Enum):
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

	def __str__(self):
		return self.value

	def __int__(self):
		return [x.value for x in Month].index(self.value) + 1

	@classmethod
	def from_str(self, label):
		if label in ('Birth', 'Genysi', 'Birth'.lower(), 'Genysi'.lower()):
			return self.Birth
		if label in ('Melting', 'Tixyl', 'Melting'.lower(), 'Tixyl'.lower()):
			return self.Melting
		if label in ('Roots', 'Rysumas', 'Roots'.lower(), 'Rysumas'.lower()):
			return self.Roots
		if label in ('Bloom', 'Anthys', 'Bloom'.lower(), 'Anthys'.lower()):
			return self.Bloom
		if label in ('Apex', 'Perigree', 'Apex'.lower(), 'Perigree'.lower()):
			return self.Apex
		if label in ('Fruiting', 'Ekarpo', 'Fruiting'.lower(), 'Ekarpo'.lower()):
			return self.Fruiting
		if label in ('Play', 'Ludere', 'Play'.lower(), 'Ludere'.lower()):
			return self.Play
		if label in ('Reap', 'Therismo', 'Reap'.lower(), 'Therismo'.lower()):
			return self.Reap
		if label in ('Death', 'Chima', 'Death'.lower(), 'Chima'.lower()):
			return self.Death
		if label in ('Darkness', 'Skotad', 'Darkness'.lower(), 'Skotad'.lower()):
			return self.Darkness
		if label in ('Bottom', 'Apogee', 'Bottom'.lower(), 'Apogee'.lower()):
			return self.Bottom
		if label in ('Ice', 'Pagos', 'Ice'.lower(), 'Pagos'.lower()):
			return self.Ice
		else:
			raise NotImplementedError

	@classmethod
	def choices(self):
		return [(x.value, x.name) for x in self]


class Era(Enum):
	# Era's last 100 years, with a rotating leadership
	First_Age = 'Uniting'			# Starts with Elves
	Second_Age = 'Trade'			# Then Dwarves
	Third_Age = 'Expansion'			# Then Humans
	Fourth_Age = 'Magic'			# Magic begins to become used as items
	Fifth_Age = 'Wealth'			# Rich Exploit Magic Items
	Sixth_Age = 'War' 				# Cithrel and Ciphers
	Seventh_Age = 'Golden'			# Modern Fantasy Steampunk
	Eight_Age = 'Calamity'			# Next Campaign! Magic stops working
	Ninth_Age = 'Restoration'		# Rebuilding the continents into seperate countries
	Tenth_Age = 'Industry'			# Rediscovery of modern life through different means
	Eleventh_Age = 'Modern'			# Defining the modern era as one would 1970's 
	Twelfth_Age = 'Technology'		# Computers exists... Leading towards cyberpunk

	def __str__(self):
		return self.value

	def __int__(self):
		return [x.value for x in Era].index(self.value)

	@classmethod
	def choices(self):
		return [(x.value, x.name) for x in self]


class Article(models.Model):
	title = models.CharField(max_length=50, default='')
	article = models.TextField(default='')

	day = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(28)])
	month = models.CharField(max_length=20, choices=Month.choices(), default=Month.Birth, help_text="""<p>Birth = Genysi</p><p>Melting = Tixyl</p><p>Roots = Rysumas</p><p>Bloom = Anthys</p><p>Apex = Perigree</p><p>Fruiting = Ekarpo</p><p>Play = Ludere</p><p>Reap = Therismo</p><p>Death = Chima</p><p>Darkness = Skotad</p><p>Bottom = Apogee</p><p>Ice = Pagos</p>""")
	year = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
	era = models.CharField(max_length=20, choices=Era.choices(), default=Era.Sixth_Age, help_text="""<p>First_Age = Uniting</p><p>Second_Age = Trade</p><p>Third_Age = Expansion</p><p>Fourth_Age = Magic</p><p>Fifth_Age = Wealth</p><p>Sixth_Age = War</p><p>Seventh_Age = Golden</p><p>Eight_Age = Calamity</p><p>Ninth_Age = Restoration</p><p>Tenth_Age = Industry</p><p>Eleventh_Age = Modern</p><p>Twelfth_Age = Technology</p>""")

	def __str__(self):
		return str(self.day) + '/' + str(self.month) + '/' + str(self.year) + ' Era of ' + str(self.era)

	def __repr__(self):
		return str(self.month) + ' ' + str(self.day) + ', Year ' + str(self.year) + ' in the Era of ' + str(self.era)


class Date:
	Day: int = 1
	Month: Month = Month.Birth
	Year: int = 98
	Era: Era = Era.Sixth_Age

	def __init__(self, day, month, year, era):
		if day >= 1 and day <= 28:
			self.Day = day
		if isinstance(month, Month):
			self.Month = month
		elif isinstance(month, int) and month >= 1 and month <= 12:
			self.Month = list(Month)[month]
		if year >= 1 and year <= 100:
			self.Year = year
		if isinstance(era, Era):
			self.Era = era
		elif isinstance(era, int) and month >= 1 and month <= 12:
			self.Era = list(Era)[era]

	def __str__(self):
		return str(self.Day) + '/' + str(int(self.Month)) + '/' + str(self.Year) + ' Era of ' + str(self.Era)

	def __repr__(self):
		return str(self.Month) + ' ' + str(self.Day) + ', Year ' + str(self.Year) + ' in the Era of ' + str(self.Era)

	def to_dict(self):
		return {
			"Era": self.Era,
			"Year": self.Year,
			"Day": self.Day,
			"Month": self.Month
		}

	# Comparison operators
	def __eq__(self, other):
		return self.Day == other.Day and self.Month == other.Month and self.Year == other.Year and self.Era == other.Era

	def __ne__(self, other):
		return not self.__eq__(other)

	def __lt__(self, other):
		if int(self.Era) < int(other.Era):
			return True
		if self.Year < other.Year:
			return True
		if int(self.Month) < int(other.Month):
			return True
		if self.Day < other.Day:
			return True
		return False

	def __le__(self, other):
		return self.__lt__(other) or self.__eq__(other)

	def __gt__(self, other):
		return not self.__lt__(other)

	def __ge__(self, other):
		return self.__gt__(other) or self.__eq__(other)


class Holiday:
	Name: str = ""
	Description: str = ""
	Date: Date = Date(1, Month.Birth, 1, Era.First_Age)

	def __init__(self, date, name, desc):
		self.Date = date
		self.Name = name
		self.Description = desc

	def __str__(self):
		return self.Name + ": " + str(self.Date)
