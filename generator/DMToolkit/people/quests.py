#!/usr/bin/python3

from generator.DMToolkit.resource.trinkets import Trinkets
from generator.DMToolkit.people.character import create_person, Character
from generator.DMToolkit.people.traits import quest_location
from generator.DMToolkit.beasts.treasure import treasure_samples, Campaign_Speed
from generator.DMToolkit.resource.names import TownNamer
from generator.DMToolkit.store.stores import determine_cost
from generator.DMToolkit.beasts.beastiary import *
from generator.DMToolkit.people.PC import PC
from bs4 import BeautifulSoup as bs

questHTML = '<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width" /><title></title><style>' \
           'body{max-width:800px;margin-left:auto;margin-right:auto;padding-left:5px;padding-right:5px;} html{' \
           'font-family:Arial;}h1, h2 {color:black;text-align:center;} .center{text-align:center;} .bold{font-weight:' \
           'bold;}.emp{font-style:italic;} table{border:1px solid black;border-spacing:0px;}table tr th {' \
           'background-color:gray;color:white;padding:5px;}table tr td {margin:0px;padding:5px;}.text-xs{font-size:' \
           '12px;}.text-sm{font-size:14px;}.text-md{font-size:18px;}.text-lg{font-size:24px;}.text-xl{font-size:' \
           '32px;}.col-1-3{width:33.3%;float: left;}.col-2-3{width:50%;float:left;}.col-3-3{width:100%;float:left;}' \
           '.col-1-2{width:50%;float:left;}.col-2-2{width:100%;float:left;}.col-1-4{width:25%;float:left;}.col-2-4{' \
           'width:33.3%;float:left;}.col-3-4{width:50%;float:left;}.col-4-4{width:100%;float:left;}</style><style ' \
           'type="text/css">.inventory-table td{border-bottom:1px solid black;}.wrapper-box{width:100%;border:2px ' \
           'solid black;padding:5px;}</style></head><body><script>function show_hide(ident){\nvar a = document.' \
           'getElementById(ident);\nif (a.style.display === \'none\'){\na.style.display = \'block\';} else {' \
           'a.style.display = \'none\';}}</script>'


class QuestBoard(object):
    Low = High = Quantity = 0
    Board = []
    Members = list()
    Positions = list()
    TownName = ''
    HTML = ''

    def __init__(self, low, high, quan, town_name, to_file=True):
        if low > high:
            low, high = high, low
        if high > 55:
            high = 55
        if low < 1:
            low = 1
        self.Low = low
        self.High = high
        self.Quantity = quan
        self.TownName = town_name

        self.fill_board(to_file)

    def fill_board(self, to_file):
        global questHTML
        ret_html = questHTML
        for _ in range(self.Quantity):
            num = randint(self.Low, self.High + 1)
            q = Quest(num)
            self.Board.append(q)

            if isinstance(q.Other, Character):
                # No NPC allocated, create a monster
                print(q.Other.Name, ':: NPC :: created for', q.Title)
                p = PC(q.Other)
                self.Members.append(p)
                self.Positions.append(q.Title)
                ret_html += '<table class="wrapper-box"><tr><td><span class="text-md">' + q.Title + ': ' + \
                             str(p) + '</div></td></tr></table><br />'
            elif q.Other != 'Monster':
                # Specific Monster
                print_monster(pick_monster(name=q.Other))
                ret_html += '<iframe src="beasts/' + q.Other + '.html" height="500" width="100%" style="padding: 10px"></iframe><br>'
                print(q.Other, ":: Specific Monster :: created for", q.Title)
            else:
                m = pick_monster(cr=str(q.Level) + '.0')
                print_monster(m)
                ret_html += '<iframe src="beasts/' + m[
                    0] + '.html" height="500" width="100%" style="padding: 10px"></iframe><br />'
                print(m[0], ":: Monster :: created for", q.Title)
        ret_html += '</body></html>'
        if to_file:
            with open(self.TownName + ' questboard.html', 'w') as outf:
                outf.write(bs(ret_html, 'html5lib').prettify())
        else:
            self.HTML = ret_html

    def __str__(self):
        line = '<center class="bold text-md" style="font-size: 150%;"><a href="' + self.TownName + \
               ' questboard.html">Quest Board</a></center><br/>'
        for x in self.Board:
            line += str(x)
        return line


class Quest(object):
    Title = Hook = ''
    Reward = Level = 0
    Reporter = Other = None

    def __init__(self, level):
        self.Level = int(level)
        # Create Person of interest and Reward
        self.Reporter = create_person(None)
        self.Reward = int(sum(treasure_samples(1, ['Coins'], Campaign_Speed[self.Level])))

        # Quest picker
        r = randint(0, 4)
        if r == 0:
            self.__fetch()
        elif r == 1:
            self.__bounty()
        elif r == 2:
            self.__escort()
        elif r == 3:
            self.__guild()

    def __fetch(self):
        # Retrieve stolen or rare item
        when = choice([
            'yesterday',
            'the other day',
            'a while ago',
            'today',
            'a fortnight ago',
            'this week',
            'this morning',
            'last evening',
            'last morning',
            'a week ago',
            'two days ago',
            'three days ago',
            'four days ago',
            'five days ago',
            'six days ago',
            'recently',
            'very recently',
        ])
        self.Other = create_person(None)
        location = quest_location[randint(len(quest_location))].lower()
        r = randint(0, 5)
        if r == 0:
            self.Title = 'Missing Item'
            item = choice(Trinkets)
            heritage = choice([
                'Brother',
                'Sister',
                'Mom',
                'Dad',
                'Parent',
                'Sibling',
                'Step-Brother',
                'Step-Sister',
                'Step-Mom',
                'Step-Dad',
                'Grandma',
                'Grandpa',
                'Uncle',
                'Aunt',
                'Great-Grandma',
                'Great-Grandpa',
                'Great-Uncle',
                'Great-Aunt',
            ])

            self.Hook = "I seem to have lost something very close to me. It's \"" + item + '". My ' + heritage + \
                        ' gave it to me forever ago, and seem to have lost it. If you find it, please bring it to ' + \
                        self.Reporter.Name + ' ' + location + '.'
        if r == 1:
            self.Title = 'Stolen Item! HELP!'
            item = choice(Trinkets)
            self.Hook = 'A trinket of mine was rudely taken from me ' + when + '. I reported it to the police, but ' + \
                        'no effort to capture them has been made! I believe the crook to be ' + self.Other.Name + ' (' + \
                        self.Other.Gender + ' / ' + self.Other.Race + ' / ' + str(self.Other.Age) + ' years old)\n' + \
                        'If you apprehend them, see ' + self.Reporter.Name + ' ' + location + '. The trinket is "' + \
                        item + '".'
        elif r == 2:
            self.Title = 'Missing Person: ' + self.Reporter.Name
            self.Hook = 'NOTICE: ' + self.Reporter.Name + ' has gone missing. They were last seen with ' + \
                        self.Other.Name + ' (' + self.Other.Gender + ' / ' + self.Other.Race + ' / ' + \
                        str(self.Other.Age) + ' years old)' + '. If you have any information, please contact the' + \
                        ' authorities.\nRace: ' + self.Reporter.Race + '\nAge: ' + str(self.Reporter.Age) + \
                        '\nAppearance: ' + self.Reporter.Appearance
        elif r == 3:
            self.Title = 'Kidnapped Person: ' + self.Reporter.Name
            self.Hook = 'NOTICE: ' + self.Reporter.Name + ' has been kidnapped. They were last seen with ' + \
                        self.Other.Name + ' ( ' + self.Other.Gender + ' / ' + self.Other.Race + ' / ' + \
                        str(self.Other.Age) + ' years old).' + ' If you have any information, please contact the' +\
                        ' authorities.\nRace: ' + self.Reporter.Race + '\nAge: ' + str(self.Reporter.Age) + \
                        '\nAppearance: ' + self.Reporter.Appearance
        elif r == 4:
            timing = str(randint(1, 13)) + ':' + str(choice(['00', 15, 30, 45]))
            self.Title = 'Search Party: ' + self.Other.Name
            self.Hook = 'NOTICE: ' + self.Reporter.Name + ' has gone missing. ' + self.Other.Name + ' has organized' + \
                        ' a searching party. If you have any information, report it to the authorities.\nIf you ' + \
                        'wish to join the search party, please see ' + self.Other.Name + ' ' + location + ' at ' + \
                        timing + '. \nRace: ' + self.Reporter.Race + '\nAge: ' + str(self.Reporter.Age) + \
                        '\nAppearance: ' + self.Reporter.Appearance

    def __bounty(self):
        Beasts = {}
        BeastSource = 'D&D 5'
        if BeastSource == 'D&D 5':
            Beasts.update(json.load(open(os.path.join('generator', 'DMToolkit', 'resource', '5e_beasts.json'), 'r'), encoding='utf-8'))
        elif BeastSource == 'Pathfinder 1':
            Beasts.update(json.load(open(os.path.join('generator', 'DMToolkit', 'resource', 'beasts.json'), 'r'), encoding='utf-8'))
        # Kill a Monster or a Criminal
        r = randint(0, 6)
        if r == 0:
            self.Title = 'Bounty: '
        elif r == 1:
            self.Title = 'Wanted: '
        elif r == 2:
            self.Title = 'Wanted (Dead of Alive): '
        elif r == 3:
            self.Title = 'Wanted (Dead): '
        elif r == 4:
            self.Title = 'Wanted (Alive): '
        elif r == 5:
            self.Title = 'Beware: '
        # Assassination target
        if randint(2) == 0:
            # Beast
            badCR = True
            while badCR:
                name = choice(list(Beasts.keys()))
                if int(float(Beasts[name]['CR'])) == self.Level:
                    badCR = False
            self.Other = name
            place = choice(['North', 'South', 'North-East', 'South-East', 'North-West', 'South-West', 'East', 'West'])
            self.Hook = 'A "' + name + '" has taken refuge ' + place + ' of town. They have cause great harm to us ' + \
                        'and we are looking for able bodies to help defeat this foe. If you are able, report to ' + \
                        self.Reporter.Name + ' for more information.'
        else:
            # Criminal
            self.Other = create_person(None)
            self.Title += self.Other.Name
            self.Hook = 'Name: ' + self.Other.Name + '\nGender: ' + self.Other.Gender + '\nRace: ' + self.Other.Race + \
                        '\nAge: ' + str(self.Other.Age) + ' years old\nAppearance: ' + self.Other.Appearance + \
                        '\nIf you have any information, please see ' + self.Reporter.Name

    def __escort(self):
        # Nobel seeking help through a shady place
        r = randint(0, 4)
        if r == 0:
            self.Title = 'Hired Hand Needed'
        elif r == 1:
            self.Title = 'Sellsword Wanted'
        elif r == 2:
            self.Title = 'Hired Hand Wanted'
        elif r == 3:
            self.Title = 'Sellsword Needed'
        elif r == 4:
            self.Title = 'Hiring Adventurers'

        r = randint(0, 3)
        location = quest_location[randint(len(quest_location))].lower()
        destination = str(TownNamer())
        self.Other = 'Monster'
        if r == 0:
            self.Hook = 'I need some assistance taking some items to ' + destination + '. If you are available, ' + \
                        ' please see ' + self.Reporter.Name + ' ' + location + '.'
        elif r == 1:
            self.Hook = 'I need to get to ' + destination + " in a week. I'm nervous about travelling alone, and " + \
                        'need a companion for the journey. Please see ' + self.Reporter.Name + ' ' + location + '.'
        elif r == 2:
            items = choice([
                'Weapons', 'Armor', 'Scrolls', 'Equipment', 'Staffs', 'Supplies', 'Food', 'Wands', 'Slaves', 'Gems',
                'Spell books', 'Books', 'Swords', 'Bows', 'Potions'
            ]).lower()
            self.Hook = "I'm transporting a shipment of " + items + ' to ' + destination + ', and need some help.' + \
                        ' Food and shelter will be covered for your assistance. Serious Inquiries only. See ' + \
                        self.Reporter.Name + ' ' + location + ' before the end of the week.'

    def __guild(self):
        # All possible guild quests
        r = randint(0, 11)
        if r == 0:
            self.Title = 'Adventurers Guild'
        elif r == 1:
            self.Title = 'Arcane Guild'
        elif r == 2:
            self.Title = 'Laborers Guild'
        elif r == 3:
            self.Title = 'Performers Guild'
        elif r == 4:
            self.Title = 'Scholastic Guild'
        elif r == 5:
            self.Title = 'Merchant Guild'
        elif r == 6:
            self.Title = 'Bardic Guild'
        elif r == 7:
            self.Title = 'Military Guild'
        elif r == 8:
            self.Title = 'Thieves Guild'
        elif r == 9:
            self.Title = 'Assassin Guild'
        elif r == 10:
            self.Title = 'Gladiator Guild'

        location = quest_location[randint(len(quest_location))].lower()
        self.Other = create_person(None)
        self.Hook = "We're a new chapter of the " + self.Title + ' and we are looking for some new talent and faces' + \
                    '. If you are interested in joining, please see ' + self.Reporter.Name + ' ' + location + \
                    '.\nFor more information, please see ' + self.Other.Name + '.'

    def __str__(self):
        line = '<table class="wrapper-box"><tbody><tr><td><center class="bold text-md">' + self.Title + ' (Level ' + \
               str(self.Level) + ')</center>'
        for l in self.Hook.split('\n'):
            line += '<p>&emsp;' + l + '</p>'
        line += '<center><span class="bold text-md">Reward:</span>' + determine_cost(self.Reward) + '</center></td>' + \
                '</tr></tbody></table><br/>'
        return line
