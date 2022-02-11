from generator.DMToolkit.resource.resources import *
from numpy.random import randint, choice, random_sample
from generator.DMToolkit.people.character import create_person
from generator.DMToolkit.resource.names import Antiques, Books, Enchanter, Potions, Tavern, Restaurant, Jeweller, Blacksmith, GeneralStore, Weapons,\
    Jewelling, Brothel, Gunsmithing
from generator.DMToolkit.store.masterwork import special_masterwork_weapon, special_masterwork_armor
from generator.DMToolkit.core.variance import normalize_dict


class Item:
    """Parent Class for All items"""
    Title: str = ""
    Description: str = ""
    Category: str = ""
    Link: str = ""
    Cost: float = 0
    Expandable: bool = False
    Linkable: bool = False

    def __str__(self):
        global MasterID
        # Header Content
        s = '<tr><td style="width:50%;"><span class="text-md"'
        if self.Expandable:
            s += """onclick="show_hide('""" + str(MasterID) + """a')" style="color:blue;" """
        s += '>'

        # Link a potential item
        if self.Linkable:
            s += '<a href="' + self.Link + '">' + self.Title + '</a>'
        else:
            s += self.Title

        # End Header
        s += '</span>'

        # Sub section
        if self.Description != "":
            s += '<br /><span class="text-sm emp"'

            # Add clickable
            if self.Expandable:
                s += ' id=\"' + str(MasterID) + 'a\" style="display: none;"'
                MasterID += 1
            s += '>' + self.Description + '</span>'

        # Cost and Category
        s += '</td><td>' + determine_cost(self.Cost) + '</td><td>' + str(self.Category) + '</td></tr>'
        return s

    def __repr__(self):
        return self.Title + ' (' + str(self.Category) + ')'

    def to_dict(self):
        return {
            "Title:": self.Title,
            "Description": self.Description,
            "Category": self.Category,
            "Link": self.Link,
            "Cost": self.Cost,
            "Expandable": self.Expandable,
            "Linkable": self.Linkable
        }


class Enchant():
    Spell:str = ''
    Description:str = ''
    Level:int = 0
    Cost:float = 0.0
    Uses:int = 0

    def __init__(self, iSpell=None, rechargable=True):
        self.Spell = iSpell

        if self.Spell is not None:
            self.Level = find_spell_level(self.Spell)
        else:
            self.Level = int(choice(list(level_likelihood.keys()), p=list(level_likelihood.values())))
            if self.Level == 0:
                self.Spell = choice(level_0)
            elif self.Level == 1:
                self.Spell = choice(level_1)
            elif self.Level == 2:
                self.Spell = choice(level_2)
            elif self.Level == 3:
                self.Spell = choice(level_3)
            elif self.Level == 4:
                self.Spell = choice(level_4)
            elif self.Level == 5:
                self.Spell = choice(level_5)
            elif self.Level == 6:
                self.Spell = choice(level_6)
            elif self.Level == 7:
                self.Spell = choice(level_7)
            elif self.Level == 8:
                self.Spell = choice(level_8)
            elif self.Level == 9:
                self.Spell = choice(level_9)

        self.__spell_pricing()

        if rechargable:
            self.Uses = int(choice([2, 4, 6, 8, 10, 12], p=[.35, .3, .15, .1, .05, .05]))
            self.Cost += self.Uses * (self.Level + 1)**self.Level
            self.__describe(rechargable)
        else:
            self.Uses = 1
            self.__describe(rechargable)

    def __spell_pricing(self):
        if self.Level == 0:
            self.Cost = 12.5
        elif self.Level == 1:
            self.Cost = 25
        elif self.Level == 2:
            self.Cost = 150
        elif self.Level == 3:
            self.Cost = 375
        elif self.Level == 4:
            self.Cost = 700
        elif self.Level == 5:
            self.Cost = 1125
        elif self.Level == 6:
            self.Cost = 1650
        elif self.Level == 7:
            self.Cost = 2275
        elif self.Level == 8:
            self.Cost = 3000
        elif self.Level == 9:
            self.Cost = 4825
        # Odd pricing for more complex spells
        if self.Spell in odd_price:
            self.Cost *= odd_price[self.Spell]

    def __describe(self, recharge):
        deets = find_spell_details(self.Spell)
        usable = ""
        if recharge:
            usable += "<p>This item has " + str(self.Uses) + " charges. You may cast the spell at a level above the " + \
                     "natural spell level, but for every spell level above, expend an additional charge until " + \
                     "depletion. Once depleted, roll 1d20. On a Natural 1, the item is destroyed. This item " + \
                     "regenerates 1d" + str(self.Uses) + " charges at Sunrise.</P>"
        self.Description = '<p>Name: <a href="' + deets[0] + '">' + self.Spell + '</a> (' + deets[1] + \
                           ')</p><p>Casting: ' + deets[2] + ' | ' + deets[3] + ' | ' + deets[4] + '</p>' + usable + \
                           deets[5]

    def __str__(self):
        return self.Description

    def __repr__(self):
        return self.Spell + ' (' + determine_cost(self.Cost) + ')'

    def to_dict(self):
        return {
            'Spell': self.Spell,
            'Description': self.Description,
            'Level': self.Level, 
            'Cost': self.Cost,
            'Uses': self.Uses,
        }


class Book(Item):
    g = {
        0: 'Children',
        1: 'Drama',
        2: 'Fiction',
        3: 'Horror',
        4: 'Humor',
        5: 'Mystery',
        6: 'Nonfiction',
        7: 'Romance',
        8: 'SciFi',
        9: 'Tome',
    }

    def __init__(self, rarity):
        self.Category = self.g[rarity]
        self.Title = str(Books(genre=self.Category))
        self.Cost = 0.5 + random_sample()


class Room(Item):
    def __init__(self, beds: int, qual: int):
        self.Title = str(beds) + " Beds"
        self.Cost = 0.5 * (qual + 1) * beds
        self.Description = ""
        self.Category = "Lodging"
        self.Link = ""
        self.Expandable = False
        self.Linkable = False
        # Necessary variable for replication
        self.Beds = beds


class Person(Item):
    Person = None

    def __init__(self, useless):
        # Even though this has an argument, It needs it, but it's useless
        self.Person = create_person(None)
        self.Title = self.Person.Name + ' (' + self.Person.Race + ')'
        self.Description = self.Person.Appearance + '; Age ' + str(self.Person.Age)
        self.Category = self.Person.Gender + ' wanting ' + self.Person.Orientation
        self.Cost = random_sample() + .1
        self.Expandable = False
        self.Linkable = False


class Food(Item):
    def __init__(self, rarity):
        s = ""
        meal_option = randint(15) + rarity
        if meal_option <= 10:
            self.Category = "Meat, Bread"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(len(Food_m2))] + " " + Food_m3[randint(
                len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
        elif meal_option == 11:
            self.Category = "Meat, Bread, Fruit"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(len(Food_m2))] + " " + Food_m3[randint(
                len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " and a side of " + Food_f1[randint(len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]

        elif meal_option == 12:
            self.Category = "Meat, Bread, Vegetable"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(len(Food_m2))] + " " + Food_m3[randint(
                len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " and a side of " + Food_v1[randint(len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))]
        elif meal_option == 13:
            self.Category = "Vegetable, Bread, Fruit"
            s += Food_v1[randint(len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " and a side of " + Food_f1[randint(len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]
        elif meal_option == 14:
            self.Category = "Meat, Fruit, Vegetable"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(len(Food_m2))] + " " + Food_m3[randint(len(Food_m3))]
            s += " with " + Food_f1[randint(len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]
            s += " and " + Food_v1[randint(len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))]
        else:
            self.Category = "Meat, Fruit, Vegetable, Bread"
            s += Food_m1[randint(len(Food_m1))] + Food_m2[randint(len(Food_m2))] + " " + Food_m3[randint(
                len(Food_m3))] + " with a "
            s += Food_g1[randint(len(Food_g1))] + Food_g2[randint(len(Food_g2))] + " " + Food_g3[randint(len(Food_g3))]
            s += " with " + Food_f1[randint(len(Food_f1))] + ' ' + Food_f2[randint(len(Food_f2))]
            s += " and " + Food_v1[randint(len(Food_v1))] + ' ' + Food_v2[randint(len(Food_v2))]
        self.Title = s
        if meal_option == 0:
            self.Cost = (len(s) * random_sample() + .5) // 10
        else:
            self.Cost = (len(s) * sum(random_sample(meal_option))) // 10


class Drink(Item):
    def __init__(self, level):
        s = ''
        num = randint(4) + level
        if num < 2:
            self.Category = "Non-Alcoholic"
            s += Drink_d1[randint(len(Drink_d1))]
        else:
            self.Category = "Alcoholic"
            s += Drink_d2[randint(len(Drink_d2))]
        self.Title = s
        if num == 0:
            self.Cost = (len(s) * random_sample() + .5) / 10
        else:
            self.Cost = (len(s) * sum(random_sample(num))) / 10


class Jewel(Item):
    value = [
        10,
        50,
        100,
        500,
        1000,
        5000,
    ]
    Rarity = 0

    def __init__(self, rarity):
        self.Title = Jewelling.j1[randint(len(Jewelling.j1))] + Jewelling.j2[randint(len(Jewelling.j2))] + \
                     Jewelling.j3[randint(len(Jewelling.j3))]
        if rarity >= 5:
            rarity %= 5
        self.Rarity = rarity
        self.Cost = self.value[self.Rarity] * (random_sample() + 1)
        l = [
            'Low Quality Gems', 'Semi Precious Gems', 'Medium Quality Gemstones', 'High Quality Gemstones', 'Jewels',
            'Grand Jewels'
        ]
        self.Category = l[self.Rarity]


class Art(Item):
    materials = [['pewter', 'granite', 'soapstone', 'limestone', 'carved wood', 'ceramic'],
                 ['pewter', 'alabaster', 'silver', 'marble', 'bronze'],
                 ['pewter', 'alabaster', 'silver', 'marble', 'brass'], ['gold', 'adamantine', 'dragonbone', 'crystal']]
    gems = [[
        'n azurite', ' banded agate', ' blue quartz', ' hematite', ' lapis lazuli', ' malachite', ' moss agate',
        'n obsidian piece', ' tiger eye', ' beryl'
    ],
            [
                ' bloodstone', ' carnelian', ' chalcedony', ' citrine', ' jasper', ' moonstone', ' n onyx', ' zircon',
                ' chrysophase'
            ],
            [
                'n amber', 'n amethyst', ' piece of coral', ' garnet', ' piece of jade', ' pearl', ' spinel',
                ' tourmaline'
            ], ['n alexandrite', 'n aquamarine', ' topaz', ' peridot', ' blue spinel', ' black pearl', ' diamond']]
    filigree = [['copper', 'oak wood', 'tin', 'bronze', 'bone'], ['brass', 'maple wood', 'iron', 'glass', 'bone'],
                ['gold', 'mahogany wood', 'glass', 'ivory', 'mythril'], ['platinum', 'ironwood', 'mythril', 'ivory']]
    descriptor = [
        'ugly', 'beautiful', 'ancient', 'old', 'strange', 'antique', 'durable', 'sturdy', 'engraved', 'ornate', 'rough',
        'ornamental'
    ]
    cloth = ['silk', 'wool', 'leather', 'fur', 'angelskin', 'darkleaf', 'griffon mane']
    bad_condition = [
        'in poor condition', 'of poor craftsmanship', 'of shoddy construction', 'in bad shape', 'of low quality'
    ]
    figurine = [
        'a dragon', 'a gryphon', 'a hydra', 'an owlbear', 'a beholder', 'a boar', 'a bear', 'a wolf', 'a fox',
        'a tiger', 'a lion', 'a horse', 'an owl', 'a hawk', 'an eagle', 'a crow', 'a snake', 'a fish', 'a shark',
        'a goblin', 'a skeleton', 'an orc', 'a minotaur', 'a tiefling', 'a warrior', 'a knight', 'a thief', 'a wizard',
        'a ship', 'a castle', 'a tower', 'a boat', 'a king', 'a queen', 'a princess', 'a god', 'a goddess'
    ]
    object = [
        'ring', 'tankard', 'goblet', 'cup', 'drinking horn', 'crown', 'circlet', 'tiara', 'pendant', 'necklace',
        'amulet', 'medallion', 'bowl', 'plate', 'jewelry box', 'music box', 'brooch', 'chess set', 'mask', 'holy text',
        'hourglass', 'vase'
    ]
    magic = [
        'It glows with a soft blue light', 'It glows with a soft green light', 'It glows with a soft red light',
        'It glows with a soft amber light', 'It glows with a soft violet light', 'It is warm to the touch',
        'It is hot to the touch', 'It is cool to the touch', 'It is cold to the touch', 'It hums with gentle music',
        'It hums with melodic music', 'It hums with soft music', 'It is wreathed in blue flames',
        'It is wreathed in green flames', 'It is wreathed in red flames', 'It is wreathed in amber flames',
        'It is wreathed in violet flames'
    ]

    def __init__(self, quality):
        if quality > 5:
            quality %= 6
        c = randint(10)
        if quality == 0:
            c %= 3
            if c == 0:
                self.Title = choice(['Silvered', 'Gilded']) + ' ' + choice(['bottle', 'flask', 'jug']) + \
                                   ' of ' + choice(['dwarven', 'elven', 'Dragonborn']) + ' ' + \
                                   choice(['beer', 'wine', 'ale', 'mead'])
            elif c == 1:
                self.Title = 'Pair of ' + choice(self.descriptor) + ' ' + choice(self.cloth) + ' gloves'
            elif c == 2:
                self.Title = choice(self.descriptor) + ' ' + choice(self.cloth) + ' ' + choice(['hat', 'ribbon'])
        elif quality == 1:
            c %= 6
            if c == 0:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.figurine) + ', ' + choice(self.bad_condition)
            elif c == 1:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.object) + ', ' + choice(self.bad_condition)
            elif c == 2:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[0])
            elif c == 3:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[0])
            elif c == 4:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[0])
            elif c == 5:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[0]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[0])
        elif quality == 2:
            c %= 2
            if c == 0:
                self.Title = choice(self.descriptor) + ' ' + choice(self.cloth) + ' ' + \
                                   choice(['cloth', 'cloak']) + ' with ' + choice(self.materials[1]) + ' clasps'
            elif c == 1:
                self.Title = choice(self.descriptor) + ' belt with a(n) ' + choice(self.materials[1]) + ' buckle'
        elif quality == 3:
            c %= 8
            if c == 0:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 1:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 2:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[2])
            elif c == 3:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[1]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[2])
            elif c == 4:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 5:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[1])
            elif c == 6:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[2])
            elif c == 7:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[2])
        elif quality == 4:
            c %= 5
            if c == 0:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[2])
            elif c == 1:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[2])
            elif c == 2:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[3])
            elif c == 3:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[2]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[3])
            elif c == 4:
                self.Title = choice(self.materials[3]) + ' framed painting of ' + choice(self.figurine)
        elif quality == 5:
            c %= 4
            if c == 0:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.figurine) + ', inlaid with ' + choice(self.filigree[3]) + ' ' + \
                                   choice(self.magic)
            elif c == 1:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.object) + ', inlaid with ' + choice(self.filigree[3]) + ' ' + \
                                   choice(self.magic)
            elif c == 2:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.figurine) + ', set with a' + choice(self.gems[3]) + ' ' + \
                                   choice(self.magic)
            elif c == 3:
                self.Title = choice(self.descriptor) + ' ' + choice(self.materials[3]) + ' ' + \
                                   choice(self.object) + ', set with a' + choice(self.gems[3]) + ' ' + \
                                   choice(self.magic)
        self.Title = self.Title.title()
        cost_factor = [50, 150, 500, 1000, 5000, 10000, 50000]
        self.Cost = cost_factor[quality + 1]
        self.Category = 'Grade ' + str(quality) + ' Art'


class Wondrous(Item):
    Aura = Slot = ''
    CL = Weight = 0

    def __init__(self, cl=-1):
        self.Category = "Wondrous Item"
        self.Linkable = True
        if cl == -1 or SpellSource == 'D&D 5':
            pick = choice(list(MasterWondrous.keys()))
            self.Title = pick
            self.Link = MasterWondrous[pick]['Link']
            self.Cost = int(MasterWondrous[pick]['Price'])
            self.CL = MasterWondrous[pick]['CL']
            self.Aura = MasterWondrous[pick]['Aura']
            self.Slot = MasterWondrous[pick]['Slot']
            self.Weight = MasterWondrous[pick]['Weight']
        elif SpellSource == 'Pathfinder 1' and cl != -1:
            i = 0
            while True:
                pick = choice(list(MasterWondrous.keys()))
                if cl == int(MasterWondrous[pick]['CL']):
                    self.Title = pick
                    self.Link = MasterWondrous[pick]['Link']
                    self.Cost = int(MasterWondrous[pick]['Price'])
                    self.CL = int(MasterWondrous[pick]['CL'])
                    self.Aura = MasterWondrous[pick]['Aura']
                    self.Slot = MasterWondrous[pick]['Slot']
                    self.Weight = MasterWondrous[pick]['Weight']
                    break
                elif i == 100:
                    i = 0
                    cl = int(MasterWondrous[pick]['CL']) + 1
                else:
                    i += 1
        self.Description = 'Aura ' + self.Aura + '; CL ' + str(self.CL) + '; Weight ' + \
                           str(self.Weight) + '; Slot ' + self.Slot


class General(Item):
    from generator.DMToolkit.resource.trinkets import Trinkets, Gear

    def __init__(self, level, trinket=False):
        if not trinket:
            if level == 0:
                self.Title = self.__choose_type__('C')
                self.Cost = self.Gear['C'][self.Title]['Base Price']
                self.Category = self.Gear['C'][self.Title]['Class']
            elif level == 1:
                self.Title = self.__choose_type__('U')
                self.Cost = self.Gear['U'][self.Title]['Base Price']
                self.Category = self.Gear['U'][self.Title]['Class']
            elif level == 2:
                self.Title = self.__choose_type__('R')
                self.Cost = self.Gear['R'][self.Title]['Base Price']
                self.Category = self.Gear['R'][self.Title]['Class']
            elif level == 3:
                self.Title = self.__choose_type__('E')
                self.Cost = self.Gear['E'][self.Title]['Base Price']
                self.Category = self.Gear['E'][self.Title]['Class']
        else:
            self.Title = "Trinket"
            self.Cost = random_sample() * 10
            self.Description = choice(self.Trinkets)
            self.Category = "Trinket"

    def __choose_type__(self, rarity):
        options = {
            'Adventuring Gear/Luxury Items': 250,
            'Tools & Skill Kits': 200,
            'Food & Drink & Lodging': 150,
            'Clothing': 150,
            'Services': 5,
            'Transport': 5,
        }
        c = choice(list(options.keys()), p=list(normalize_dict(options).values()))
        item = choice(list(self.Gear[rarity].keys()))
        while self.Gear[rarity][item]['Class'] != c:
            item = choice(list(self.Gear[rarity].keys()))
        return item


class Wearable(Item):
    Spell = Name = Type = ""
    Level = Cost = 0
    Enchantment = None

    def __init__(self, level, spell=None):
        self.Expandable = True
        if spell is None:
            if level == 0:
                self.Spell = choice(level_0)
                self.Cost = 13
                self.Category = 'Level 0'
            elif level == 1:
                self.Spell = choice(level_1)
                self.Cost = 25
                self.Category = 'Level 1'
            elif level == 2:
                self.Spell = choice(level_2)
                self.Cost = 150
                self.Category = 'Level 2' 
            elif level == 3:
                self.Spell = choice(level_3)
                self.Cost = 375
                self.Category = 'Level 3' 
            elif level == 4:
                self.Spell = choice(level_4)
                self.Cost = 700
                self.Category = 'Level 4' 
            elif level == 5:
                self.Spell = choice(level_5)
                self.Cost = 1125
                self.Category = 'Level 5'
            elif level == 6:
                self.Spell = choice(level_6)
                self.Cost = 1650
                self.Category = 'Level 6'
            elif level == 7:
                self.Spell = choice(level_7)
                self.Cost = 2275
                self.Category = 'Level 7'
            elif level == 8:
                self.Spell = choice(level_8)
                self.Cost = 3000
                self.Category = 'Level 8'
            elif level == 9:
                self.Spell = choice(level_9)
                self.Cost = 4825
                self.Category = 'Level 9'

            if self.Spell in odd_price:
                self.Cost = round(self.Cost * odd_price[self.Spell])

            self.Enchantment = Enchant(iSpell=self.Spell, rechargable=True)
        else:
            if find_spell_level(spell) == level:
                self.Spell = spell
                self.Enchantment = Enchant(iSpell=self.Spell)
                self.Category = 'Level ' + str(level)
        slot = choice(['Ring', 'Necklace', 'Headband'])
        self.Description = self.Enchantment.Description
        self.Title = slot + ' of ' + self.Spell
        self.Category += ' (' + slot + ')'


class Scroll(Item):
    Name = Spell = Add = ''
    Enchantment = None
    Cost = 0

    def __init__(self, level, spell=None, naming=True):
        self.Expandable = True
        if spell is None:
            if level == 0:
                self.Spell = choice(level_0)
                self.Category = 'Level 0'
                self.Cost = 12.5
            elif level == 1:
                self.Spell = choice(level_1)
                self.Category = 'Level 1'
                self.Cost = 25
            elif level == 2:
                self.Spell = choice(level_2)
                self.Category = 'Level 2'
                self.Cost = 150
            elif level == 3:
                self.Spell = choice(level_3)
                self.Category = 'Level 3'
                self.Cost = 375
            elif level == 4:
                self.Spell = choice(level_4)
                self.Category = 'Level 4'
                self.Cost = 700
            elif level == 5:
                self.Spell = choice(level_5)
                self.Category = 'Level 5'
                self.Cost = 1125
            elif level == 6:
                self.Spell = choice(level_6)
                self.Category = 'Level 6'
                self.Cost = 1650
            elif level == 7:
                self.Spell = choice(level_7)
                self.Category = 'Level 7'
                self.Cost = 2275
            elif level == 8:
                self.Spell = choice(level_8)
                self.Category = 'Level 8'
                self.Cost = 3000
            elif level == 9:
                self.Spell = choice(level_9)
                self.Category = 'Level 9'
                self.Cost = 4825

            if self.Spell in odd_price:
                self.Cost = round(self.Cost * odd_price[self.Spell])

            self.Enchantment = Enchant(iSpell=self.Spell, rechargable=False)
        else:
            if find_spell_level(spell) == level:
                self.Spell = spell
                self.Enchantment = Enchant(iSpell=self.Spell, rechargable=False)
                self.Category = 'Level ' + level

        if naming:
            self.Title = Scroll_Name_Potential[randint(len(Scroll_Name_Potential))] + self.Spell
        else:
            self.Title = self.Spell
            self.Add = '+'

        self.Description = self.Enchantment.Description


class Potion(Item):
    Spell = Name = ""
    Cost = 0
    Enchantment = None

    def __init__(self, level, spell=None):
        self.Expandable = True
        if spell is None:
            if level == 0:
                self.Spell = choice(level_0)
                self.Category = 'Level 0'
                self.Cost = 13
            elif level == 1:
                self.Spell = choice(level_1)
                self.Category = 'Level 1'
                self.Cost = 25
            elif level == 2:
                self.Spell = choice(level_2)
                self.Category = 'Level 2'
                self.Cost = 150
            elif level == 3:
                self.Spell = choice(level_3)
                self.Category = 'Level 3'
                self.Cost = 375
            elif level == 4:
                self.Spell = choice(level_4)
                self.Category = 'Level 4'
                self.Cost = 700
            elif level == 5:
                self.Spell = choice(level_5)
                self.Category = 'Level 5'
                self.Cost = 1125
            elif level == 6:
                self.Spell = choice(level_6)
                self.Category = 'Level 6'
                self.Cost = 1650
            elif level == 7:
                self.Spell = choice(level_7)
                self.Category = 'Level 7'
                self.Cost = 2275
            elif level == 8:
                self.Spell = choice(level_8)
                self.Category = 'Level 8'
                self.Cost = 3000
            elif level == 9:
                self.Spell = choice(level_9)
                self.Category = 'Level 9'
                self.Cost = 4825

            if self.Spell in odd_price:
                self.Cost = round(self.Cost * odd_price[self.Spell])

            self.Enchantment = Enchant(iSpell=self.Spell, rechargable=False)
        else:
            if find_spell_level(spell) == level:
                self.Spell = spell
                self.Category = 'Level ' + level
                self.Enchantment = Enchant(iSpell=self.Spell, rechargable=False)

        self.Title = Potion_Name_Potential[randint(len(Potion_Name_Potential))] + self.Spell
        self.Description = self.Enchantment.Description


class Wand(Item):
    Spell = Name = ""
    Level = Cost = 0
    Enchantment = None

    def __init__(self, level, spell=None):
        if spell is None:
            if level == 0:
                self.Spell = choice(level_0)
                self.Category = 'Level 0'
                self.Cost = 13
            elif level == 1:
                self.Spell = choice(level_1)
                self.Category = 'Level 1'
                self.Cost = 25
            elif level == 2:
                self.Spell = choice(level_2)
                self.Category = 'Level 2'
                self.Cost = 150
            elif level == 3:
                self.Spell = choice(level_3)
                self.Category = 'Level 3'
                self.Cost = 375
            elif level == 4:
                self.Spell = choice(level_4)
                self.Category = 'Level 4'
                self.Cost = 700
            elif level == 5:
                self.Spell = choice(level_5)
                self.Category = 'Level 5'
                self.Cost = 1125
            elif level == 6:
                self.Spell = choice(level_6)
                self.Category = 'Level 6'
                self.Cost = 1650
            elif level == 7:
                self.Spell = choice(level_7)
                self.Category = 'Level 7'
                self.Cost = 2275
            elif level == 8:
                self.Spell = choice(level_8)
                self.Category = 'Level 8'
                self.Cost = 3000
            elif level == 9:
                self.Spell = choice(level_9)
                self.Category = 'Level 9'
                self.Cost = 4825

            if self.Spell in odd_price:
                self.Cost = round(self.Cost * odd_price[self.Spell])

            self.Enchantment = Enchant(iSpell=self.Spell)
        else:
            if find_spell_level(spell) == level:
                self.Spell = spell
                self.Enchantment = Enchant(iSpell=self.Spell)
                self.Category = 'Level ' + level

        self.Title = Wand_Name_Potential[randint(len(Wand_Name_Potential))] + self.Spell
        self.Description = self.Enchantment.Description


class Weapon(Item):
    """
    Cost should be in GP
    Rarity [0, 4] - Common, Uncommon, Rare, Very Rare, Legendary
        Rarity will also determine what types of material to use as well as the
            price for an item. Also note, that the prices are how much they cost
            to make, not the cost they'll be sold for.
    """
    Weight = Cost = Rarity = Masterwork = 0
    Name = Dice = Crit = Class = Special = Text = ''
    Damage = []
    Enchantment = None

    def __init__(self, rare, iClass=None, iName=None, iTrait=None):
        self.Rarity = rare
        self.Name = iName
        self.__choose_type(iClass)
        self.__choose_metal()

        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_enchantment(Enchant())
        if randint(1, 101) + self.Rarity * self.Rarity >= 75:
            self.add_masterwork(determine_rarity([1, 9]))
            if randint(1, 101) + self.Rarity * self.Rarity >= 75:
                special_masterwork_weapon(self, iTrait)

        # Item conversion portion
        self.Title = self.Name.title() + ' (' + self.Class + ')'
        self.Expandable = True if self.Enchantment is not None or self.Special != '' else False

        self.Category = ''
        if self.Masterwork is not None:
            self.Category += 'Masterwork '
        self.Category += ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary'][self.Rarity]
        if self.Enchantment is not None:
            self.Category += ', Level ' + [str(x) for x in range(10)][self.Enchantment.Level]


        self.Description = 'Damage: ' + self.Dice + ' (' + self.Crit + ') ' + str(self.Damage) + ' Weight: ' + str(self.Weight) + ' lbs' + self.Text
        if self.Enchantment is not None:
            self.Description += str(self.Enchantment)


    def __choose_type(self, requirement=None):
        if requirement is None:
            # Make a pick with each weapon type
            if randint(2):
                self.Class = choice(list(possible_melee.keys()))
                self.Name = choice(list(possible_melee[self.Class])).title()
            else:
                self.Class = choice(list(possible_ranged.keys()))
                self.Name = choice(list(possible_ranged[self.Class])).title()
        # Existing requirement
        elif requirement in list(possible_melee.keys()):
            self.Class = requirement
            self.Name = choice(list(possible_melee[self.Class])).title()

        elif requirement in list(possible_ranged.keys()):
            self.Class = requirement
            self.Name = choice(list(possible_ranged[self.Class])).title()

        else:
            print("The requirement is not in the list of possible weapons.")
            return None

        # We have a class of weapon. Get weapon Damage
        self.Dice = str(int(self.Rarity / 2) + 1) + 'd' + str(choice(die_values[self.Class]))

        # Give Damage Types
        if self.Class == 'Heavy Axe' or self.Class == 'Light Axe':
            self.Damage = ['S']
        elif self.Class == 'Heavy Blade' or self.Class == 'Light Blade':
            self.Damage = ['S', 'P']
        elif self.Class == 'Close':
            self.Damage = ['B', 'P']
        elif self.Class == 'Double':
            self.Damage = ['S', 'B', 'P']
        elif self.Class == 'Flail':
            self.Damage = ['B', 'S']
        elif self.Class == 'Hammer':
            self.Damage = ['B']
        elif self.Class == 'Monk':
            self.Damage = ['B', 'S', 'P']
        elif self.Class == 'Polearm':
            self.Damage = ['P', 'S']
        elif self.Class == 'Spear':
            self.Damage = ['P']
        elif self.Class == 'Bows':
            self.Damage = ['Ra', 'P', choice(['30', '40', '50', '60', '70', '80', '90', '100', '110', '120']) + ' ft.']
        elif self.Class == 'Crossbow':
            self.Damage = ['Ra', 'P', choice(['60', '70', '80', '90', '100', '110', '120']) + ' ft.']
        elif self.Class == 'Thrown':
            self.Damage = ['Ar', 'P', 'S', choice(['15', '20', '25', '30', '35', '40']) + ' ft.']
        return

    def __choose_metal(self):
        if self.Rarity > 4:
            self.Rarity %= 4

        if self.Rarity == 1:  # Uncommon Materials
            m = self.__verify_metal(uncommon_material)

        elif self.Rarity == 2:  # Rare Materials
            m = self.__verify_metal(rare_material)

        elif self.Rarity == 3:  # Very Rare Materials
            m = self.__verify_metal(very_rare_material)

        elif self.Rarity == 4:  # Legendary Materials
            m = self.__verify_metal(legendary_material)

        else:  # Common Materials
            m = self.__verify_metal(common_material)

        if m[0] in ['Cold Iron', 'Cold Siccatite']:
            self.Damage.append('Cold')
        elif m[0] in ['Elysian Bronze']:
            self.Damage.append('Radiant')
        elif m[0] in ['Hot Siccatite']:
            self.Damage.append('Fire')
        elif m[0] in ['Mindglass']:
            self.Damage.append('Psychic')

        self.Name = m[0] + ' ' + self.Name
        self.__weigh(m[0], m[1])

    def __verify_metal(self, cl):
        metal = None
        while metal is None:
            metal = choice(list(cl.keys()))
            # print(metal, '=', cl[metal])
            t = 0
            while t < len(self.Damage):
                if self.Damage[t] not in cl[metal]['Type']:
                    if 'ft.' not in self.Damage[t]:
                        # print(metal, 'Not compatible with a', self.Name, '(\''+self.Damage[t]+'\')')
                        metal = None
                        t = len(self.Damage)
                t += 1
        return metal, cl

    def __crit(self):
        chance = randint(100) + self.Rarity * 10
        if chance < 80:
            self.Crit = 'x2'
        elif chance < 92:
            self.Crit = '19-20 x2'
        elif chance < 97:
            self.Crit = '18-20 x2'
        elif chance < 100:
            self.Crit = 'x3'
        elif chance < 130:
            self.Crit = '19-20 x3'
        else:
            self.Crit = '18-20 x3'
        return chance

    def __weigh(self, metal, cl):
        dice_incriment = int(eval(self.Dice.split('d')[1]) / 2) * 2**eval(self.Dice.split('d')[0])
        crit_val = (self.__crit() // 20)
        cost_factor = max([weapon_cost_and_weight[self.Class][0], dice_incriment * crit_val])

        self.Cost = float(round(cost_factor * cl[metal]['Cost'] * (self.Rarity + 1)**self.Rarity, 2))
        self.Weight = round(weapon_cost_and_weight[self.Class][1] * cl[metal]['Weight'] * 14, 1)

    def add_enchantment(self, ench):
        if self.Enchantment is None:
            self.Enchantment = ench
            self.Cost = float(self.Cost + self.Enchantment.Cost)
        else:
            print("This Item is already enchanted.")

    def add_trait(self, trait):
        if self.Special == '':
            special_masterwork_weapon(self, trait)

    def add_masterwork(self, mlevel):
        if mlevel < 10:
            if self.Masterwork == 0:
                self.Masterwork = int(mlevel)
                self.Cost += (1 + mlevel) * 1000
                self.Name = "+" + str(mlevel) + ' ' + self.Name
                self.Dice += "+" + str(mlevel)


class Firearm(Item):
    cost_and_weight = {
        'Pistol': [100, .8],
        'Rifle': [250, 2],
        'Sniper': [1000, 5],
        'Shotgun': [500, 3],
    }
    Weight = Cost = Rarity = Masterwork = Range = Capacity = 0
    Name = Dice = Crit = Class = Special = Text = ''
    Enchantment = None
    Misfire = []
    Damage = []

    def __init__(self, rarity, iClass=None, iName=None, iTrait=None):
        if iClass is None or iClass not in list(possible_guns.keys()):
            self.Class = choice(list(possible_guns.keys()))
        else:
            self.Class = iClass
        if rarity > 4:
            rarity %= 4
        self.Rarity = rarity
        self.Crit = 'x' + str(choice([3, 4, 5, 6], p=[.5625, .25, .125, 0.0625]))
        self.Damage = ['P']
        self.__choose_metal()
        self.Name += choice(possible_guns[self.Class])

        if self.Class == 'Pistol':
            self.Capacity = int(choice([1, 2, 4, 6]))
            self.Range = 10 + randint(2, 4) * 5 * (self.Rarity + 1)
            self.Dice = str(int(self.Rarity + 1)) + 'd' + str(choice([4, 6, 8], p=[.625, .25, .125]))
            self.Max_Range = 5 * round((self.Range * 2.5) / 5)

        elif self.Class == 'Rifle':
            self.Capacity = int(randint(1, 8) * 5)
            self.Range = 10 + randint(2, 10) * 5 * (self.Rarity + 1)
            self.Dice = str(int(self.Rarity + 1)) + 'd' + str(choice([6, 8, 10], p=[.625, .25, .125]))
            self.Max_Range = self.Range * 3

        elif self.Class == 'Shotgun':
            self.Capacity = int(choice([1, 2, 3, 4]))
            self.Range = 10 + randint(2, 5) * 5 * ((self.Rarity + 1) // 2)
            self.Dice = str(int(self.Rarity + 1)) + 'd' + str(choice([6, 8, 10], p=[.625, .25, .125]))
            self.Max_Range = self.Range * 2

        elif self.Class == 'Sniper':
            self.Capacity = int(choice([1, 2, 4, 6]))
            self.Range = 30 + randint(3, 7) * 10 * (self.Rarity + 1)
            self.Dice = str(int(self.Rarity + 1)) + 'd' + str(choice([10, 12, 20], p=[.625, .25, .125]))
            self.Max_Range = self.Range * 4
        if self.Class != 'Sniper' and self.Rarity > 0:
            self.Dice = str(int(self.Dice[0]) - 1) + self.Dice[1:]

        if iName is not None:
            self.Name = iName

        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_enchantment(Enchant())
        if randint(1, 101) + self.Rarity * self.Rarity >= 75:
            self.add_masterwork(determine_rarity([1, 9]))
            if randint(1, 101) + self.Rarity * self.Rarity >= 75:
                special_masterwork_weapon(self, iTrait)

        self.Misfire = [1]
        if self.Class == 'Sniper' or self.Class == 'Shotgun':
            self.Misfire += [2, 3]
        elif self.Class == 'Rifle':
            self.Misfire += [2]
        if self.Masterwork > 0:
            self.Misfire.pop()

        # Item conversion portion
        self.Title = self.Name.title() + ' (' + self.Class + ')'
        self.Expandable = True if self.Enchantment is not None or self.Special != '' else False

        self.Category = ''
        if self.Masterwork is not None:
            self.Category += 'Masterwork '
        self.Category += ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary'][self.Rarity]
        if self.Enchantment is not None:
            self.Category += ', Level ' + [str(x) for x in range(10)][self.Enchantment.Level]

        misfire = "Misfire: N/A"
        if len(self.Misfire) > 0:
            misfire = "Misfire: " + str(self.Misfire)

        self.Description = 'Damage: ' + self.Dice + ' (' + self.Crit + ') ' + str(self.Damage) + ' Weight: ' + str(self.Weight) + ' lbs. Range: '
        self.Description += str(self.Range) + ' / ' + str(self.Max_Range) + ' ft. Mag: ' + str(self.Capacity) + ' ' + misfire + self.Text
        if self.Enchantment is not None:
            self.Description += str(self.Enchantment)

    def __choose_metal(self):
        if self.Rarity > 4:
            self.Rarity %= 4

        cl = [common_material, uncommon_material, rare_material, very_rare_material, legendary_material][self.Rarity]
        metal = None
        while metal is None:
            metal = choice(list(cl.keys()))
            if 'HA' in cl[metal]['Type'] and 'P' in cl[metal]['Type']:
                self.Name += metal + ' '
            else:
                metal = None
        self.Cost = self.cost_and_weight[self.Class][0] * cl[metal]['Cost'] * (self.Rarity + 2)**self.Rarity * (
            int(self.Crit[1]) / 2)
        self.Weight = round(self.cost_and_weight[self.Class][1] * cl[metal]['Weight'] * 4, 1)

    def add_enchantment(self, ench):
        if self.Enchantment is None:
            self.Enchantment = ench
            self.Cost = self.Cost + self.Enchantment.Cost
        else:
            print("This Item is already enchanted.")

    def add_masterwork(self, mlevel):
        if mlevel < 10:
            if self.Masterwork == 0:
                self.Masterwork = int(mlevel)
                self.Cost += (1 + mlevel) * (1 + mlevel) * 1000
                self.Name = "+" + str(mlevel) + ' ' + self.Name
                self.Dice += "+" + str(mlevel)


class Armor(Item):
    light_armor = {
        # Name  :           HP, AC, Cost, Weight
        'Padded': [5, 1, 5, 10],
        'Leathered': [10, 1, 10, 15],
        'Studded': [15, 2, 25, 20],
        'Chained': [20, 2, 100, 25],
    }
    medium_armor = {
        # Name  :           HP, AC, Cost, Weight
        'Hide': [
            15,
            2,
            15,
            25,
        ],
        'Scale mail': [
            20,
            2,
            50,
            30,
        ],
        'Chainmail': [
            25,
            3,
            150,
            40,
        ],
        'Breastplate': [
            25,
            3,
            200,
            30,
        ],
    }
    heavy_armor = {
        # Name  :           HP, AC, Cost, Weight
        'Splint mail': [
            30,
            3,
            200,
            45,
        ],
        'Banded mail': [
            30,
            3,
            250,
            35,
        ],
        'Half-plate': [
            35,
            4,
            600,
            50,
        ],
        'Full plate': [
            40,
            4,
            1500,
            50,
        ],
    }
    shield = {
        # Name  :           HP, AC, Cost, Weight
        'Buckler': [
            5,
            1,
            5,
            5,
        ],
        'Light Shield': [
            10,
            1,
            9,
            6,
        ],
        'Heavy Shield': [
            20,
            2,
            20,
            15,
        ],
        'Tower Shield': [
            20,
            4,
            30,
            45,
        ],
    }

    Weight = Cost = Rarity = Masterwork = AC = 0
    Name = Class = Special = Text = ''
    Metal = Enchantment = None

    def __init__(self, rare, iClass=None, iName=None, iTrait=None):
        self.Rarity = rare
        self.Name = iName
        self.Class = iClass
        self.__choose_metal()
        self.__choose_type()

        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_enchantment(Enchant())
        if randint(1, 101) + self.Rarity * self.Rarity >= 95:
            self.add_masterwork(determine_rarity([1, 9]))
            if randint(1, 101) + self.Rarity * self.Rarity >= 75:
                special_masterwork_armor(self, iTrait)

        # Item conversion portion
        self.Title = self.Name.title() + ' (' + self.Class + ')'
        self.Expandable = True if self.Enchantment is not None or self.Special != '' else False

        self.Category = ''
        if self.Masterwork is not None:
            self.Category += 'Masterwork '
        self.Category += ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary'][self.Rarity]
        if self.Enchantment is not None:
            self.Category += ', Level ' + [str(x) for x in range(10)][self.Enchantment.Level]

        self.Description = 'AC: +' + str(self.AC) + ' Weight: ' + str(self.Weight) + ' lbs.' + self.Text
        if self.Enchantment is not None:
            self.Description += str(self.Enchantment)

    def __choose_metal(self):
        if self.Rarity > 4:
            self.Rarity %= 4

        if self.Rarity == 0:
            self.Metal = choice(list(common_material.keys()))
            self.AC = round(common_material[self.Metal]['AC'] / 10)
            self.Cost = common_material[self.Metal]['Cost']
            self.Weight = common_material[self.Metal]['Weight']
        elif self.Rarity == 1:
            self.Metal = choice(list(uncommon_material.keys()))
            self.AC = round(uncommon_material[self.Metal]['AC'] / 10)
            self.Cost = uncommon_material[self.Metal]['Cost']
            self.Weight = uncommon_material[self.Metal]['Weight']
        elif self.Rarity == 2:
            self.Metal = choice(list(rare_material.keys()))
            self.AC = round(rare_material[self.Metal]['AC'] / 10)
            self.Cost = rare_material[self.Metal]['Cost']
            self.Weight = rare_material[self.Metal]['Weight']
        elif self.Rarity == 3:
            self.Metal = choice(list(very_rare_material.keys()))
            self.AC = round(very_rare_material[self.Metal]['AC'] / 10)
            self.Cost = very_rare_material[self.Metal]['Cost']
            self.Weight = very_rare_material[self.Metal]['Weight']
        elif self.Rarity == 4:
            self.Metal = choice(list(legendary_material.keys()))
            self.AC = round(legendary_material[self.Metal]['AC'] / 10)
            self.Cost = legendary_material[self.Metal]['Cost']
            self.Weight = legendary_material[self.Metal]['Weight']

    def __choose_type(self):
        if self.Class not in ['Light', 'Medium', 'Heavy', 'Shield'] or self.Class is None:
            self.Class = choice(['Light', 'Medium', 'Heavy', 'Shield'])
        if self.Class == 'Light':
            c = choice(list(self.light_armor.keys()))
            self.AC += self.light_armor[c][1]
            self.Cost = round(self.Cost * self.light_armor[c][2] * (self.Rarity + 1)**self.Rarity)
            self.Weight *= round(self.light_armor[c][3], 1)
            self.Name = c + " " + self.Metal
            if c == 'Leathered' and self.Metal == "Leather":
                self.Name = "Leather"
        elif self.Class == 'Medium':
            c = choice(list(self.medium_armor.keys()))
            self.AC += self.medium_armor[c][1]
            self.Cost = round(self.Cost * self.medium_armor[c][2] * (self.Rarity + 1)**self.Rarity)
            self.Weight *= round(self.medium_armor[c][3], 1)
            self.Name = self.Metal + " " + c
        elif self.Class == 'Heavy':
            c = choice(list(self.heavy_armor.keys()))
            self.AC += self.heavy_armor[c][1]
            self.Cost = round(self.Cost * self.heavy_armor[c][2] * (self.Rarity + 1)**self.Rarity)
            self.Weight *= round(self.heavy_armor[c][3], 1)
            self.Name = self.Metal + " " + c
        else:
            c = choice(list(self.shield.keys()))
            self.AC += self.shield[c][1]
            self.Cost = round(self.Cost * self.shield[c][2] * (self.Rarity + 1)**self.Rarity)
            self.Weight *= round(self.shield[c][3], 1)
            self.Name = self.Metal + " " + c

    def add_enchantment(self, ench):
        if self.Enchantment is None:
            self.Enchantment = ench
            self.Cost = round(self.Cost + self.Enchantment.Cost)
        else:
            print("This Item is already enchanted.")

    def add_trait(self, trait):
        if self.Special == '':
            special_masterwork_armor(self, trait)

    def add_masterwork(self, mlevel):
        if mlevel > 10:
            mlevel %= 9
        if self.Masterwork == 0:
            self.Masterwork = int(mlevel)
            self.Cost += 2 * mlevel * mlevel * 1000
            self.Name = "+" + str(mlevel) + ' ' + self.Name
            self.AC += mlevel