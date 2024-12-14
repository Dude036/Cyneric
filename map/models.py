import uuid
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from enum import Enum, auto


# Create your models here.
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
    available_dates = models.JSONField(default=dict, blank=True)
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
