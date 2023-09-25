import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from enum import Enum, auto


# Create your models here.
class Person(models.Model):
    name = models.CharField(default='', max_length=50)
    title = models.CharField(default='', max_length=50)
    description = models.TextField(default='')
    admin_description = models.TextField(default='', blank=True, null=True)
    img_source = models.CharField(default='', max_length=100, blank=True, null=True)

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
    quest_shop_llo = models.IntegerField(default=5)
    quest_shop_lhi = models.IntegerField(default=10)
    quest_shop_inf = models.IntegerField(default=10)
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


class Town(models.Model):
    name = models.CharField(default='', max_length=50)
    description = models.TextField(default='')
    admin_description = models.TextField(default='', blank=True, null=True)
    government = models.TextField(default='')
    governing_body = models.CharField(default='', max_length=200)
    economy = models.TextField(default='')
    population = models.BigIntegerField(default=0)
    leader = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)
    generator_settings = models.ForeignKey(GeneratorShop, on_delete=models.SET_NULL, blank=True, null=True)
    x_coord_max = models.IntegerField(default=0)
    y_coord_max = models.IntegerField(default=0)
    x_coord_min = models.IntegerField(default=0)
    y_coord_min = models.IntegerField(default=0)
    magic_phrase = models.CharField(default='', max_length=200)
    img_source = models.CharField(default='', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class InitEntry(models.Model):
    name = models.CharField(default='', max_length=200)
    ac = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    initiative = models.IntegerField(default=0)
    conditions = models.TextField(default='', blank=True)

    def __str__(self):
        return str(self.initiative) + " - " + self.name


class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    # This will be a list of date strings
    date_options = models.JSONField()
    closed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ' (' + str(self.question_text) + ')'

    def __repr__(self):
        return str(self.id) + ' (' + str(self.question_text) + ')'


class Choice(models.Model):
    class Options(Enum):
        Yes_Remote = auto()
        Maybe_Remote = auto()
        Yes = auto()
        Maybe = auto()
        No = auto()

        @staticmethod
        def is_valid(op):
            return op in set(item.name for item in Choice.Options) or op in set(item.value for item in Choice.Options)

    question = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    # This will be a dictionary of date keys, and availability
    available_dates = models.JSONField()
    submitter = models.CharField(max_length=100)

    def __str__(self):
        return str(self.submitter) + ' (' + str(self.question) + ')'

    def __repr__(self):
        return str(self.submitter) + ' (' + str(self.question) + ')'


class VehicleEntity(Enum):
    Train = "Murder Train (Engine)"
    Lab = "Murder Train (Lab)"
    Sleeper = "Murder Train (Passenger Car)"
    Planar_Skiff = "Icarus"
    Mobile_Inn = "Murder Bus"
    Speedster_1 = "Magicycle 1"
    Speedster_2 = "Magicycle 2"
    Inventory = "Inventory"

    @staticmethod
    def get_name(entity):
        if entity == 'Train':
            return VehicleEntity.Train
        elif entity == 'Lab':
            return VehicleEntity.Lab
        elif entity == 'Sleeper':
            return VehicleEntity.Sleeper
        elif entity == 'Planar_Skiff':
            return VehicleEntity.Planar_Skiff
        elif entity == 'Mobile_Inn':
            return VehicleEntity.Mobile_Inn
        elif entity == 'Speedster_1':
            return VehicleEntity.Speedster_1
        elif entity == 'Speedster_2':
            return VehicleEntity.Speedster_2
        elif entity == 'Inventory':
            return VehicleEntity.Inventory

    @staticmethod
    def choices():
        return [[ve.name, ve.value] for ve in list(VehicleEntity)]


class VehicleEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entity = models.CharField(max_length=20, null=True, choices=VehicleEntity.choices(), default=None)
    deleted = models.BooleanField(default=False)
    title = models.CharField(default='', max_length=1000, blank=True)
    content = models.TextField(default='', blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __lt__(self, other):
        return self.modified_on < other.modified_on

    def __gt__(self, other):
        return self.modified_on > other.modified_on

    def __eq__(self, other):
        return self.modified_on == other.modified_on

    def __hash__(self):
        return super().__hash__()

    def to_dict(self):
        return {
            'id': self.id,
            'entity': self.entity,
            'deleted': self.deleted,
            'title': self.title,
            'content': self.content,
            'modified_on': self.modified_on,
            'created_on': self.created_on,
        }

    @staticmethod
    def from_dict(incoming):
        entry, created = VehicleEntry.objects.get_or_create(entity=incoming['entity'], title=incoming['title'], content=incoming['content'])
        return entry
