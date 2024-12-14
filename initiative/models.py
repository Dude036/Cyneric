import uuid

from django.db import models

# Create your models here.
class InitEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default='', max_length=200, db_comment='Name of the player/NPC')
    aon_link = models.CharField(default='', max_length=200, db_comment='Archives of Nethys Link', blank=True)
    skills = models.CharField(default='', max_length=200, db_comment='List of Skills not including perception', blank=True)

    # Modifiable
    ac = models.IntegerField(default=0, blank=True)
    hp = models.IntegerField(default=0, blank=True)
    will_save = models.IntegerField(default=0, blank=True)
    fortitude_save = models.IntegerField(default=0, blank=True)
    reflex_save = models.IntegerField(default=0, blank=True)
    initiative = models.IntegerField(default=0, blank=True)
    perception = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name + " - " +str(self.initiative)

    def as_dict(self):
        return {
            'name': self.name,
            'aon_link': self.aon_link,
            'skills': self.skills,
            'ac': self.ac,
            'hp': self.hp,
            'will_save': self.will_save,
            'fortitude_save': self.fortitude_save,
            'reflex_save': self.reflex_save,
            'initiative': self.initiative,
            'perception': self.perception,
        }


class ConditionOption(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default='', max_length=200, db_comment='Name of the Condition')
    description = models.TextField(default='', db_comment='Description pulled from Archives of Nethys')
    has_value = models.BooleanField(default=False, db_comment='Whether the condition has a value')

    # Modifiers
    ac_mod = models.IntegerField(default=0)
    hp_mod = models.IntegerField(default=0)
    will_mod = models.IntegerField(default=0)
    fortitude_mod = models.IntegerField(default=0)
    reflex_mod = models.IntegerField(default=0)
    perception_mod = models.IntegerField(default=0)


class Conditions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    affected = models.ForeignKey(InitEntry, on_delete=models.CASCADE)
    status = models.ForeignKey(ConditionOption, on_delete=models.CASCADE)
    value = models.IntegerField(default=0, db_comment='Condition Value')
