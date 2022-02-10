from numpy.random import randint, choice, random_sample
from generator.DMToolkit.resource.names import Antiques, Enchanter, Potions, Tavern, Restaurant, Jeweller, Blacksmith, GeneralStore, Weapons, Jewelling, Brothel, Gunsmithing
from generator.DMToolkit.store.masterwork import special_masterwork_weapon, special_masterwork_armor
from generator.DMToolkit.resource.resources import *
import simplejson as json
from generator.DMToolkit.store.items import *


class Store(object):
    """Everyone needs things!
    Inflation is the upsell rate at which things are sold for. this could be due
        to the amount of market dominance, rarity of items, or accessibility
    Quality is the spectrum of item rarity and quantity. There will be 3 digits
        First and Second: Low and High End of the Item spawn rate
        Third: Quantity of item generation
    """
    Shopkeeper = None
    Store_name = ''
    Quality = Stock = []
    Inflation = 0.0

    def __init__(self, keeper, name, service, qual):
        self.Shopkeeper = keeper
        self.Store_name = name
        self.Inflation = float(service)
        self.Quality = qual
        self.Stock = []

    def fill_store(self, Item, quantity):
        for _ in range(quantity):
            same = True
            while same:
                # qual = randint(self.Quality[0], self.Quality[1] + 1)
                qual = int(determine_rarity(self.Quality))
                i = Item(qual)
                i.Cost = float(i.Cost * self.Inflation)
                if i not in self.Stock:
                    self.Stock.append(i)
                    same = False

    def add_relic(self, Item):
        # qual = randint(self.Quality[0], self.Quality[1] + 1)
        if isinstance(Item, Weapon):
            typ = choice([
                "Axe",
                "Bow",
                "Dagger",
                "Hammer",
                "Mace",
                "Spear",
                "Sword",
            ])
            name = str(Weapons(typ))
            if typ == "Sword":
                typ = choice(['Light', 'Heavy']) + " Sword"
            elif typ == "Axe":
                typ = choice(['Light', 'Heavy']) + " Axe"
            elif typ == "Dagger":
                typ = "Close"
            elif typ == "Bow":
                typ = str(choice(["", "Cross"]) + "bow").title()

            self.Stock.append(Item(4, iName=name, iClass=typ))

    def add_enchanted(self, Item, Enchantment=None):
        qual = randint(self.Quality[0], self.Quality[1] + 1)
        i = Item(qual)
        if Enchantment is None:
            ench = Enchant()
            i.add_enchantment(ench)
        else:
            i.add_enchantment(Enchantment)
        self.Stock.append(i)

    def to_dict(self):
        d = {
            "Shopkeeper": self.Shopkeeper,
            "Store_name": self.Store_name,
            "Quality": self.Quality,
            "Stock_quantity": len(self.Stock),
            "Inflation": self.Inflation
        }
        if "Variety" in self.Store_name:
            d["Stock_type"] = "Variety"
        else:
            d["Stock_type"] = str(type(self.Stock[0]).__name__)
        return d

    def from_dict(self, new_self):
        new_class = new_self.pop("Stock_type")
        new_quan = new_self.pop("Stock_quantity")

        self.__dict__.update(new_self)
        if new_class == 'Variety':
            for _ in range(new_quan):
                num = randint(0, 12)
                if num == 0:
                    self.Stock.append(Weapon(randint(1, 5)))
                elif num == 1:
                    self.Stock.append(Armor(randint(1, 5)))
                elif num == 2:
                    self.Stock.append(Firearm(randint(1, 5)))
                elif num == 3:
                    self.Stock.append(Ring(randint(1, 10)))
                elif num == 4:
                    self.Stock.append(Scroll(randint(1, 10)))
                elif num == 5:
                    self.Stock.append(Wand(randint(1, 10)))
                elif num == 6:
                    self.Stock.append(Potion(randint(1, 10)))
                elif num == 7:
                    self.Stock.append(Book(randint(1, 10)))
                elif num == 8:
                    self.Stock.append(Wondrous())
                elif num == 9:
                    self.Stock.append(Jewel(randint(1, 10)))
                elif num == 10:
                    self.Stock.append(General(randint(1, 5)))
                elif num == 11:
                    self.Stock.append(General(0, True))
        else:
            self.fill_store(eval(new_class), new_quan)
            if new_class == 'General':
                for _ in range(2):
                    self.Stock.append(General(0, True))


class Armor(object):
    light_armor = {
        # Name	: 			HP, AC, Cost, Weight
        'Padded': [5, 1, 5, 10],
        'Leathered': [10, 1, 10, 15],
        'Studded': [15, 2, 25, 20],
        'Chained': [20, 2, 100, 25],
    }
    medium_armor = {
        # Name	: 			HP, AC, Cost, Weight
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
        # Name	: 			HP, AC, Cost, Weight
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
        # Name	: 			HP, AC, Cost, Weight
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
        # print(c)

    def __str__(self):
        global MasterID
        r = ['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary']
        l = [
            "Level 0",
            "Level 1",
            "Level 2",
            "Level 3",
            "Level 4",
            "Level 5",
            "Level 6",
            "Level 7",
            "Level 8",
            "Level 9",
        ]

        if self.Enchantment is None:
            enchant_lvl = ''
            enchanted = ''
        else:
            enchant_lvl = ', ' + l[self.Enchantment.Level]
            enchanted = str(self.Enchantment)

        master = "Masterwork " if self.Masterwork > 0 else ""
        if self.Enchantment is None and self.Special == '':
            s = """<tr><td style="width:50%;"><span class="text-md">""" + self.Name + ' (' + self.Class + \
                """) </span><br /><span class="text-sm emp">""" + 'AC: +' + str(self.AC) + ' Weight: ' + \
                str(self.Weight) + """ lbs</span></td><td>""" + determine_cost(self.Cost) + """</td><td>""" + \
                master + r[self.Rarity] + """</td></tr>"""
        else:
            s = '<tr><td style="width:50%;"><span class="text-md" onclick="show_hide(\'' + str(MasterID) + '\')"' + \
                ' style="color:blue;">' + self.Name + ' (' + self.Class + ') </span><br /><span class="text-sm ' + \
                'emp" id=\"' + str(MasterID) + '\" style="display: none;">' + 'AC: +' + str(self.AC) + ' Weight: ' + \
                str(self.Weight) + " lbs " + self.Text + enchanted + '</span></td><td>' + determine_cost(self.Cost) + \
                '</td><td>' + master + r[self.Rarity] + enchant_lvl + '</td></tr>'
            MasterID += 1
        return s

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
        # else:
        #     print("This Item is already Masterwork")

    def to_string(self):
        ench = ''
        if self.Enchantment is not None:
            ench = ' ' + self.Enchantment.to_string()
        return self.Name + ench + ' (' + determine_cost(self.Cost) + ')'

    def to_dict(self):
        return {
            'Weight': self.Weight,
            'Cost': self.Cost,
            'Rarity': self.Rarity,
            'Masterwork': self.Masterwork,
            'AC': self.AC,
            'Name': self.Name,
            'Class': self.Class,
            'Special': self.Special,
            'Text': self.Text,
            'Metal': self.Metal,
            'Enchantment': None if self.Enchantment is None or isinstance(self.Enchantment, dict) else self.Enchantment.to_dict(),
        }

    def __repr__(self):
        return self.Name + " (" + self.Class + ")"


class Inn(object):
    Store_name = ""
    Shopkeeper = Rooms = None
    Edibles = Stock = []
    Cost = Inflation = Quality = 0

    def __init__(self, keeper, name, service, rooms, quan):
        self.Shopkeeper = keeper
        self.Store_name = name
        self.Inflation = service
        self.Stock = []

        self.__fill_rooms(rooms)
        self.__fill_stock(quan)

    def __fill_rooms(self, rooms):
        self.Rooms = []
        for n in range(1, rooms + 1):
            r = Room(n, self.Quality)
            r.Cost *= self.Inflation
            self.Rooms.append(r)

    def __fill_stock(self, quan):
        # Add room Price
        for item in self.Rooms:
            self.Stock.append(item)
        for _ in range(quan):
            d = Drink(self.Quality)
            d.Cost *= self.Inflation
            self.Stock.append(d)
            f = Food(self.Quality)
            f.Cost *= self.Inflation
            self.Stock.append(f)

    def from_dict(self, new_self):
        rooms = new_self.pop('Rooms')
        if rooms:
            num_rooms = max([v['Beds'] for v in rooms])
            self.__fill_rooms(num_rooms)
        stock = new_self.pop('Stock')
        self.__fill_stock(len(stock))
        self.__dict__.update(new_self)


def create_variety_shop(owner, quan, inflate=1):
    if isinstance(inflate, float):
        inflation = inflate
    else:
        inflation = (sum(random_sample(inflate))) + .5

    a = Store(owner, "Travelling Salesmen (Variety)", inflation, [0, 0])
    for _ in range(quan):
        item = None
        num = randint(0, 12)

        if num == 0:
            item = Weapon(randint(1, 5))
        elif num == 1:
            item = Armor(randint(1, 5))
        elif num == 2:
            item = Firearm(randint(1, 5))
        elif num == 3:
            item = Wearable(randint(1, 10))
        elif num == 4:
            item = Scroll(randint(1, 10))
        elif num == 5:
            item = Wand(randint(1, 10))
        elif num == 6:
            item = Potion(randint(1, 10))
        elif num == 7:
            item = Book(randint(1, 10))
        elif num == 8:
            item = Wondrous()
        elif num == 9:
            item = Jewel(randint(1, 10))
        elif num == 10:
            item = General(randint(1, 5))
        elif num == 11:
            item = General(0, True)

        a.Stock.append(item)

    return a


def create_book_shop(owner, genres, quan, inflate=1):
    for b in genres:
        if b not in Books.Genres:
            print(b, "Not in genre List. See: ", Books.Genres)
            return None
    if isinstance(inflate, float):
        a = Store(owner, str(Antiques()) + " (Library)", inflate, [0, 9])
    else:
        a = Store(owner, str(Antiques()) + " (Library)", (sum(random_sample(inflate))) + .5, [0, 9])
    a.fill_store(Book, quan)
    return a


def create_enchantment_shop(owner, rarity, quan, inflate=1):
    name = str(Enchanter()) + " (Enchantments)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate))) + .5, rarity)
    if quan <= 2:
        quan = 3
    remain = randint(quan)
    a.fill_store(Scroll, remain)
    a.fill_store(Wand, quan - remain)
    return a


def create_enchanter_shop(owner, rarity, quan, inflate=1):
    name = str(Enchanter()) + " (Enchanter)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate))) + .5, rarity)
    for _ in range(quan):
        item = Scroll(randint(rarity[0], rarity[1]), naming=False)
        item.Cost *= inflate
        a.Stock.append(item)
    return a


def create_weapon_shop(owner, rarity, quan, inflate=1):
    name = str(Blacksmith()) + " (Weapon)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate))) + .5, rarity)
    if quan <= 2:
        quan = 3
    a.fill_store(Weapon, quan)
    return a


def create_armor_shop(owner, rarity, quan, inflate=1):
    name = str(Blacksmith()) + " (Armor)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate))) + .5, rarity)
    if quan <= 2:
        quan = 3
    a.fill_store(Armor, quan)
    return a


def create_potion_shop(owner, rarity, quan, inflate=1):
    name = str(Potions()) + " (Alchemist)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate))) + .5, rarity)
    a.fill_store(Potion, quan)
    return a


def create_tavern(owner, rooms, quan, inflate=1):
    # def __init__(self, keeper, name, service, qual, rooms, quan):
    name = str(Tavern()) + " (Inn)"
    if isinstance(inflate, float):
        a = Inn(owner, name, inflate, rooms, quan)
    else:
        a = Inn(owner, name, (sum(random_sample(inflate))), rooms, quan)
    return a


def create_jewel_shop(owner, rarity, quan, inflate=1):
    name = str(Jeweller()) + " (Jeweller)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate))) + .5, rarity)
    a.fill_store(Jewel, quan)
    return a


def create_restaurant(owner, quan, inflate=1):
    name = str(Restaurant()) + " (Restaurant)"
    if isinstance(inflate, float):
        a = Inn(owner, name, inflate, 0, quan)
    else:
        a = Inn(owner, name, (sum(random_sample(inflate))), 0, quan)
    return a


def create_general_store(owner, rarity, quan, trink, inflate=1):
    name = str(GeneralStore()) + " (General)"
    if trink < 0:
        trink = 0
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate))) + .5, rarity)
    a.fill_store(General, quan)
    for _ in range(trink):
        a.Stock.append(General(0, True))
    return a


def create_brothel(owner, quan, inflate=1):
    name = str(Brothel()) + " (Brothel)"
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, [0, 0])
    else:
        a = Store(owner, name, (sum(random_sample(inflate))) + .5, [0, 0])
    a.fill_store(Person, quan)
    return a


def create_gunsmith(owner, rarity, quan, inflate=1):
    name = str(Gunsmithing()) + ' (Gunsmith)'
    if isinstance(inflate, float):
        a = Store(owner, name, inflate, rarity)
    else:
        a = Store(owner, name, (sum(random_sample(inflate))) + .5, rarity)
    a.fill_store(Firearm, quan)
    return a


if __name__ == '__main__':
    from pprint import pprint
    from numpy import median
    totals = {}
    cap = 1000
    for t in ['Pistol', 'Rifle', 'Shotgun', 'Sniper']:
        for i in range(5):
            cost_list = []
            damage = []
            weapon = largest = average = crit = 0
            smallest = 99999999
            rang = 0
            dice = {4: 0, 6: 0, 8: 0, 10: 0, 12: 0, 20: 0}
            for _ in range(cap):
                item = Firearm(i, iClass=t)
                if item.Cost < smallest:
                    smallest = item.Cost
                elif item.Cost > largest:
                    largest = item.Cost
                d_amount = item.Dice[2:]
                if '+' in d_amount:
                    dice[int(d_amount.split('+')[0])] += 1
                    damage.append(
                        int(item.Dice[0]) * ((int(d_amount.split('+')[0]) // 2) + .5) + int(d_amount.split('+')[1]))
                    # print(int(item.Dice[0]), ((int(d_amount.split('+')[0]) // 2) +.5))
                else:
                    dice[int(item.Dice[2:])] += 1
                    damage.append(int(item.Dice[0]) * ((int(item.Dice[2:]) // 2) + .5))
                average += item.Cost
                cost_list.append(item.Cost)
                crit += int(item.Crit[1:])
                rang += item.Range
            totals[i] = {
                "Average GP per Damage": round(median(cost_list) / (sum(damage) / cap), 2),
                "Damage Average": round(sum(damage) / cap, 2),
                "Cost Max": largest,
                "Cost Min": smallest,
                "Cost Median": median(cost_list),
                "Cost Average": round(average / cap, 2),
                "Range": rang / cap,
                "Critical": crit / cap,
                "Dice": dice
            }

        print(t)
        pprint(totals)
        print()
