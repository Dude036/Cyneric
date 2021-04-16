from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(default='', max_length=50)
    title = models.CharField(default='', max_length=50)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(default='', max_length=50)
    description = models.TextField(default='')
    government = models.TextField(default='')
    governing_body = models.CharField(default='', max_length=200)
    economy = models.TextField(default='')
    population = models.BigIntegerField(default=0)
    leader = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    x_coord_max = models.IntegerField(default=0)
    y_coord_max = models.IntegerField(default=0)
    x_coord_min = models.IntegerField(default=0)
    y_coord_min = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class GeneratorShop(models.Model):
    # Weapons
    weapon_shop_num = models.IntegerField(default=2)
    weapon_shop_rlo = models.IntegerField(default=0)
    weapon_shop_rhi = models.IntegerField(default=4)
    weapon_shop_qlo = models.IntegerField(default=15)
    weapon_shop_qhi = models.IntegerField(default=25)
    weapon_shop_add = models.IntegerField(default=3)
    weapon_shop_inf = models.FloatField(default=1.0)
    # Armors
    armor_shop_num = models.IntegerField(default=2)
    armor_shop_rlo = models.IntegerField(default=0)
    armor_shop_rhi = models.IntegerField(default=4)
    armor_shop_qlo = models.IntegerField(default=15)
    armor_shop_qhi = models.IntegerField(default=25)
    armor_shop_add = models.IntegerField(default=3)
    armor_shop_inf = models.FloatField(default=1.0)
    # Potions
    potion_shop_num = models.IntegerField(default=1)
    potion_shop_rlo = models.IntegerField(default=0)
    potion_shop_rhi = models.IntegerField(default=9)
    potion_shop_qlo = models.IntegerField(default=15)
    potion_shop_qhi = models.IntegerField(default=25)
    potion_shop_inf = models.FloatField(default=1.0)
    # Enchantments
    enchant_shop_num = models.IntegerField(default=1)
    enchant_shop_rlo = models.IntegerField(default=0)
    enchant_shop_rhi = models.IntegerField(default=9)
    enchant_shop_qlo = models.IntegerField(default=15)
    enchant_shop_qhi = models.IntegerField(default=25)
    enchant_shop_inf = models.FloatField(default=1.0)
    # Enchanter
    enchanter_shop_num = models.IntegerField(default=1)
    enchanter_shop_rlo = models.IntegerField(default=0)
    enchanter_shop_rhi = models.IntegerField(default=9)
    enchanter_shop_qlo = models.IntegerField(default=15)
    enchanter_shop_qhi = models.IntegerField(default=25)
    enchanter_shop_inf = models.FloatField(default=1.0)
    # Book
    book_shop_num = models.IntegerField(default=1)
    book_shop_qlo = models.IntegerField(default=15)
    book_shop_qhi = models.IntegerField(default=25)
    book_shop_inf = models.FloatField(default=1.0)
    # Inn
    inn_shop_num = models.IntegerField(default=1)
    inn_shop_rms = models.IntegerField(default=3)
    inn_shop_qlo = models.IntegerField(default=15)
    inn_shop_qhi = models.IntegerField(default=25)
    inn_shop_inf = models.FloatField(default=1.0)
    # Jeweller
    jewel_shop_num = models.IntegerField(default=1)
    jewel_shop_rlo = models.IntegerField(default=0)
    jewel_shop_rhi = models.IntegerField(default=4)
    jewel_shop_qlo = models.IntegerField(default=15)
    jewel_shop_qhi = models.IntegerField(default=25)
    jewel_shop_inf = models.FloatField(default=1.0)
    # Food
    food_shop_num = models.IntegerField(default=1)
    food_shop_qlo = models.IntegerField(default=15)
    food_shop_qhi = models.IntegerField(default=25)
    food_shop_inf = models.FloatField(default=1.0)
    # General
    general_shop_num = models.IntegerField(default=1)
    general_shop_rlo = models.IntegerField(default=0)
    general_shop_rhi = models.IntegerField(default=3)
    general_shop_qlo = models.IntegerField(default=15)
    general_shop_qhi = models.IntegerField(default=25)
    general_shop_trk = models.IntegerField(default=3)
    general_shop_inf = models.FloatField(default=1.0)
    # Brothel
    brothel_shop_num = models.IntegerField(default=1)
    brothel_shop_qlo = models.IntegerField(default=15)
    brothel_shop_qhi = models.IntegerField(default=25)
    brothel_shop_inf = models.FloatField(default=1.0)
    # Gunsmith
    gun_shop_num = models.IntegerField(default=2)
    gun_shop_rlo = models.IntegerField(default=0)
    gun_shop_rhi = models.IntegerField(default=4)
    gun_shop_qlo = models.IntegerField(default=15)
    gun_shop_qhi = models.IntegerField(default=25)
    gun_shop_add = models.IntegerField(default=3)
    gun_shop_inf = models.FloatField(default=1.0)
    # Variety
    variety_shop_num = models.IntegerField(default=1)
    variety_shop_qlo = models.IntegerField(default=15)
    variety_shop_qhi = models.IntegerField(default=25)
    variety_shop_inf = models.FloatField(default=1.0)
    # Quest
    quest_shop_num = models.IntegerField(default=1)
    quest_shop_llo = models.IntegerField(default=15)
    quest_shop_lhi = models.IntegerField(default=25)
    quest_shop_inf = models.FloatField(default=1.0)
    # Settings
    allow_pokemon = models.BooleanField(default=False)

    class Systems(models.TextChoices):
        DD_5 = 'D&D 5'
        PATHFINER_1 = 'Pathfinder 1'

    ttrpg_system = models.CharField(max_length=15, choices=Systems.choices)

    class Races(models.TextChoices):
        AASIMER = 'Aasimer'
        CATFOLK = 'Catfolk'
        CHANGELING = 'Changeling'
        DHAMPIR = 'Dhampir'
        DROW = 'Drow'
        DUERGAR = 'Duergar'
        DWARF = 'Dwarf'
        ELF = 'Elf'
        FETCHLING = 'Fetchling'
        GILLMAN = 'Gillman'
        GNOME = 'Gnome'
        GOBLIN = 'Goblin'
        GRIPPLI = 'Grippli'
        HALF_ELF = 'Half-Elf'
        HALF_ORC = 'Half-Orc'
        HALFLING = 'Halfling'
        HOBGOBLIN = 'Hobgoblin'
        HUMAN = 'Human'
        IFRIT = 'Ifrit'
        KITSUNE = 'Kitsune'
        KOBOLD = 'Kobold'
        LIZARDFOLK = 'Lizardfolk'
        MERFOLK = 'Merfolk'
        NAGAJI = 'Nagaji'
        ORC = 'Orc'
        OREAD = 'Oread'
        RARFOLK = 'Ratfolk'
        SAMSARANS = 'Samsarans'
        STRIX = 'Strix'
        SULI = 'Suli'
        SVIRFNEBLIN = 'Svirfneblin'
        SYPLH = 'Sylph'
        TENGU = 'Tengu'
        TIEFLING = 'Tiefling'
        UNDINE = 'Undine'
        VANARA = 'Vanara'
        VISHKANYA = 'Vishkanya'
        WAYANGs = 'Wayangs'
        AARAKOCRA = 'Aarakocra'
        AIR_GENASI = 'Air Genasi'
        BUGBEAR = 'Bugbear'
        CENTAUR = 'Centaur'
        DRAGONBORN = 'Dragonborn'
        EARTH_GENASI = 'Earth Genasi'
        FIRBOLG = 'Firbolg'
        FIRE_GENASI = 'Fire Genasi'
        GITH = 'Gith'
        GOLIATH = 'Goliath'
        KALASHTAR = 'Kalashtar'
        KENKU = 'Kenku'
        LOXODON = 'Loxodon'
        MINOTAUR = 'Minotaur'
        SHIFTER = 'Shifter'
        SIMIC_HYBRID = 'Simic Hybrid'
        TABAXI = 'Tabaxi'
        TORTLE = 'Tortle'
        TRITON = 'Triton'
        VEDALKEN = 'Vedalken'
        WARFORGED = 'Warforged'
        WATER_GENASI = 'Water Genasi'
        YUAN_TI_PUREBLOOD = 'Yuan-ti Pureblood'

    race = models.CharField(max_length=50, choices=Races.choices)
    population = models.BigIntegerField(default=1000)
    variance = models.IntegerField(default=10, validators=[MaxValueValidator(100), MinValueValidator(0)])
    exotic = models.IntegerField(default=5, validators=[MaxValueValidator(100), MinValueValidator(0)])

    def to_json_objs(self):
        generate = {}
        settings = {
            'System': self.ttrpg_system,
            'Race': self.race,
            'Population': self.population,
            'Variance': self.variance,
            'Exotic': self.exotic
        }
        return generate, settings
