from numpy.random import randint, choice, random_sample, shuffle
from generator.DMToolkit.resource.names import Antiques, Enchanter, Potions, Tavern, Restaurant, Jeweller, Blacksmith, GeneralStore, Weapons, Jewelling, Brothel, Gunsmithing
from generator.DMToolkit.resource.resources import *
import simplejson as json
from generator.DMToolkit.store.items import *
from generator.DMToolkit.store.masterwork import find_masterwork_traits_weapon, find_masterwork_traits_armor


class Store():
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

    def __str__(self):
        s = '<div class="wrapper-box" style="margin-bottom:60px;padding:5px;"><span class="text-lg bold">'
        s += self.Store_name + '</span><br />\n<span class="bold text-md">Proprietor: </span><span class="text-md">'
        s += str(self.Shopkeeper) + '</div><span class="text-lg bold">Inventory</span>'
        s += '<table style="width:100%;" class="inventory-table"><tr><th style="text-align:left;">Item</th>'
        s += '<th style="text-align:left;">Cost</th><th style="text-align:left;">Type</th></tr>'
        for x in range(len(self.Stock)):
            s += str(self.Stock[x])
        s += '</table>'

        if '(Weapon)' in self.Store_name:
            s += find_masterwork_traits_weapon(self.Stock, 3)
        elif '(Gunsmith)' in self.Store_name:
            s += find_masterwork_traits_weapon(self.Stock, 3)
        elif '(Armor' in self.Store_name:
            s += find_masterwork_traits_armor(self.Stock, 3)

        return s +'</div>'


class Inn(Store):
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
        a = Store(owner, name, inflate, [0, 0])
    else:
        a = Store(owner, name, (sum(random_sample(inflate))), [0, 0])
    a.fill_store(Food, quan)
    a.fill_store(Drink, quan)
    shuffle(a.Stock)
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
