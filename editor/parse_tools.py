import bs4
import re
from urllib import parse
import requests
import simplejson as json
import os
from datetime import datetime, timedelta

github_link = 'https://raw.githubusercontent.com/5etools-mirror-1/5etools-mirror-1.github.io/master/data/'

sources_5etools = {}

spells_5etools_by_source = {}

def remake_cache():
    try:
        print("Downloading and updating Beastiary Cache")
        # Download index for dynamic download
        file = requests.get(github_link + 'bestiary/' + 'index.json')
        index = json.loads(file.text)
        json.dump(index, open(os.path.join(os.getcwd(), 'static', 'cache', 'bestiary-index.json'), 'w'))

        # Fill cache with Bestiary
        for key, bestiary in index.items():
            file = requests.get(github_link + 'bestiary/' + bestiary)
            json.dump(json.loads(file.text), open(os.path.join(os.getcwd(), 'static', 'cache', bestiary), 'w'))

        print("Downloading and updating Spell Cache")
        # Download index for dynamic download
        file = requests.get(github_link + 'spells/' + 'index.json')
        index = json.loads(file.text)
        json.dump(index, open(os.path.join(os.getcwd(), 'static', 'cache', 'spells-index.json'), 'w'))

        # Fill cache with Spells
        for key, spells in index.items():
            file = requests.get(github_link + 'spells/' + spells)
            json.dump(json.loads(file.text), open(os.path.join(os.getcwd(), 'static', 'cache', spells), 'w'))

        # Success
        return {}
    except Exception as e:
        return {"ERROR": e}


def cache_5etools_json(force=False):
    # Forced Execution
    if force:
        return remake_cache()

    # If there's no cache, make it
    if not os.path.exists(os.path.join(os.getcwd(), 'static', 'cache')):
        os.mkdir(os.path.join(os.getcwd(), 'static', 'cache'))
        return remake_cache()

    # If the cache is empty, fill it
    if len(os.listdir(os.path.join(os.getcwd(), 'static', 'cache'))) == 0:
        return remake_cache()

    # Check last update. If the update is more than 3 days ago, 
    last_update = datetime.fromtimestamp(os.path.getmtime(os.path.join(os.getcwd(), 'static', 'cache', 'bestiary-phb.json')))
    if datetime.now() - timedelta(days=30) > last_update:
        return remake_cache()

    return {}


def get_book_from_code(code):
    already_coded = ['ai', 'aitfr-avt', 'egw', 'ftd', 'ggr', 'idrotf', 'llk', 'phd', 'scc', 'tcc', 'xge']
    if code in already_coded:
        return code
    elif code == 'ua-2020por':
        return 'ua2020psionicoptionsrevisited'
    elif code == 'ua-2020smt':
        return 'ua2020spellsandmagictattoos'
    elif code == 'ua-2021do':
        return 'ua2021draconicoptions'
    elif code == 'ua-2022wotm':
        return 'ua2022wondersofthemultiverse'
    elif code == 'ua-ar':
        return 'uaartificerrevisited'
    elif code == 'ua-frw':
        return 'uafighterroguewizard'
    elif code == 'ua-mm':
        return 'uamodernmagic'
    elif code == 'ua-saw':
        return 'uasorcererandwarlock'
    elif code == 'ua-ss':
        return 'uastarterspells'
    elif code == 'ua-tobm':
        return 'uathatoldblackmagic'
    else:
        return ''

def get_code_from_book(book):
    if book == 'psa':
        return 'ps-a'
    elif book == 'psd':
        return 'ps-d'
    elif book == 'psi':
        return 'ps-i'
    elif book == 'psk':
        return 'ps-k'
    elif book == 'psx':
        return 'ps-x'
    elif book == 'psz':
        return 'ps-z'
    elif book == 'ua2021magesofstrixhaven':
        return 'ua-2021mos'
    elif book == 'ua2022giantoptions':
        return 'ua-2022go'
    elif book == 'uaclericdruidwizard':
        return 'ua-cdw'
    elif book == 'uaclassfeaturevariants':
        return 'ua-cfv'
    elif book == 'ua2020subclassespt2':
        return 'ue-20s2'
    elif book == 'ua2020psionicoptionsrevisited':
        return 'ua-2020por'
    elif book == 'ua2020spellsandmagictattoos':
        return 'ua-2020smt'
    elif book == 'ua2021draconicoptions':
        return 'ua-2021do'
    elif book == 'ua2022wondersofthemultiverse':
        return 'ua-2022wotm'
    elif book == 'uaartificerrevisited':
        return 'ua-ar'
    elif book == 'uafighterroguewizard':
        return 'ua-frw'
    elif book == 'uamodernmagic':
        return 'ua-mm'
    elif book == 'uasorcererandwarlock':
        return 'ua-saw'
    elif book == 'uastarterspells':
        return 'ua-ss'
    elif book == 'uathatoldblackmagic':
        return 'ua-tobm'
    else:
        return book

def populate_5e_json_helpers():
    global sources_5etools, spells_5etools_by_source
    print("Filling 'sources_5etools' from cache")
    sources_5etools = json.load(open(os.path.join(os.getcwd(), 'static', 'cache', 'bestiary-index.json'), 'r'))
    print("Filling 'spells_5etools_by_source' from cache")
    for file_name in os.listdir(os.path.join(os.getcwd(), 'static', 'cache')):
        if 'spells' in file_name and 'index' not in file_name:
            spell_dict = json.load(open(os.path.join(os.getcwd(), 'static', 'cache', file_name), 'r'))
            book_code = file_name[file_name.find('-')  + 1 : file_name.rfind('.')]
            for spell in spell_dict['spell']:
                spells_5etools_by_source[spell['name'].lower()] = parse.quote(spell['name'].lower()) + '_' + get_book_from_code(book_code)


def de_dict(d):
    s = ''
    for k, v in d.items():
        s += k + ' ' + str(v) + ', '
    return s[:-2]


def de_list(l):
    s = ''
    for x in l:
        s += x + ', '
    return s[:-2]


class Creature:
    def __init__(self, name, link):
        self.Name = name
        self.Link = link

        # Add new variables as Empty
        self.Perception = ''
        self.Recall = ''
        self.Source = ''
        self.Speed = ''
        self.Size = ''
        self.Description = ''
        self.Alignment = ''
        self.Traits = []
        self.Languages = []
        self.Skills = {}
        self.Actions = []
        self.Abilities = []
        self.Spells = []
        self.Str = -2
        self.Dex = -2
        self.Con = -2
        self.Wis = -2
        self.Int = -2
        self.Cha = -2
        self.Ac = ''
        self.Hp = -2
        self.Cr = -2
        self.Fort = ''
        self.Ref = ''
        self.Will = ''
        self.Resist = ''
        self.Immune = ''
        self.Weak = ''

    def validate(self):
        state = True
        for key, value in vars(self).items():
            if isinstance(value, str):
                if value == '':
                    print("!! Missing", key)
                    state = False
            elif isinstance(value, int):
                if value == -2:
                    print("!! Missing", key)
                    state = False
            elif isinstance(value, list):
                if len(value) == 0:
                    print("!! Missing", key)
                    state = False
            elif isinstance(value, dict):
                if len(value.keys()) == 0:
                    print("!! Missing", key)
                    state = False
        return state

    def set_from_raw_text(self, text):
        print("\t\tSetting Description")
        match = re.search(r'([a-z\)][A-Z])', text)
        if 'Recall Knowledge' in text:
            if match is None:
                self.Description = text[0: text.index('Recall Knowledge')]
                self.Description = self.Description.encode(encoding='utf-8', errors='replace')
            else:
                self.Description = text[text.find(match.group(1)) + 1: text.index('Recall Knowledge')]
            print("\t\tSetting Recall")
            dc = text.find('DC ', text.index('Recall Knowledge'))
            s = text.find('(', text.index('Recall Knowledge'))
            e = text.find(')', text.index('Recall Knowledge'))
            self.Recall = text[s + 1: e] + ': ' + text[dc: dc + 5]
        else:
            self.Description = text[0: text.index('|')]
            r = 10 + self.Cr
            if 'Uncommon' in self.Traits:
                r += 2
            if 'Rare' in self.Traits:
                r += 5
            if 'Unique' in self.Traits:
                r += 10
            self.Recall = '?: DC' + str(r)

    def set_traits(self, uncommon, rare, unique, align, size, traits):
        print("\t\tSetting Traits")
        if uncommon is not None:
            self.Traits.append('Uncommon')
        if rare is not None:
            self.Traits.append('Rare')
        if unique is not None:
            self.Traits.append('Unique')
        if align is not None:
            self.Traits.append(align.text)
            self.Alignment = align.text
        if size is not None:
            self.Traits.append(size.text)
            self.Size = size.text

        for t in traits:
            self.Traits.append(str(t.string))

    def set_source(self, line):
        print("\t\tSetting Source")
        self.Source = line.i.string

    def set_cr(self, line):
        print("\t\tSetting CR")
        self.Cr = int(line)

    def set_perception(self, line):
        print("\t\tSetting Perception")
        self.Perception = line.text.replace('Perception ', '')

    def set_languages(self, line):
        print("\t\tSetting Language")
        self.Languages = [x.strip() for x in re.split(r'[\,\;]', line.text.replace('Languages ', ''))]

    def set_skills(self, line):
        print("\t\tSetting Skills")
        for x in re.split(r'[\,\;]', line.text.replace('Skills ', '')):
            match = re.match(r'\s*(\w+)\s(.*)', x)
            self.Skills[match.group(1)] = match.group(2)

    def set_stats(self, line):
        print("\t\tSetting Stats")
        for x in re.split(r'[\,\;]', line.text):
            match = re.match(r'\s?([\w]{3}) ([\+\-]\d*)', x)
            if match.group(1) == 'Str':
                self.Str = match.group(2)
            elif match.group(1) == 'Dex':
                self.Dex = match.group(2)
            elif match.group(1) == 'Con':
                self.Con = match.group(2)
            elif match.group(1) == 'Int':
                self.Int = match.group(2)
            elif match.group(1) == 'Wis':
                self.Wis = match.group(2)
            elif match.group(1) == 'Cha':
                self.Cha = match.group(2)

    def remaining_parser(self, lines):
        print("\t\tParsing Remaining")
        for line in lines:
            if line.startswith('<span class="hanging-indent">'):
                print('\t\t\tBegin Bulk action parsing')
                self.handle_actions(line)

            elif 'alt="Reaction"' in line:
                print('\t\t\tReaction found. Adding to Abilities')
                self.put_ability(line, -1)
            elif 'alt="Free Action"' in line:
                print('\t\t\tFree Action found. Adding to Abilities')
                self.put_ability(line, 0)
            elif 'alt="Single Action"' in line:
                print('\t\t\tSingle Action found. Adding to Abilities')
                self.put_ability(line, 1)
            elif 'alt="Two Actions"' in line:
                print('\t\t\tTwo Actions found. Adding to Abilities')
                self.put_ability(line, 2)
            elif 'alt="Three Actions"' in line:
                print('\t\t\tThree Actions found. Adding to Abilities')
                self.put_ability(line, 3)

            elif '<b>Items</b>' in line:
                print('\t\t\tItems found. Adding to Items')
            elif '<b>Speed</b>' in line:
                print('\t\t\tSpeed found')
                self.Speed = line[13:]

            elif '<b>AC</b>' in line:
                print('\t\t\tAC and Saves found')
                new_line = bs4.BeautifulSoup(line, 'html.parser')
                match = re.search(r'b>([^<]*)<b', str(new_line))
                if match is None:
                    self.Ac = new_line.text.split('; ')[0][3:]
                    new_line = new_line.text.split('; ')[1]
                else:
                    self.Ac = match[0].strip()
                    new_line = ''.join(str(new_line).split('<b>')[2:]).replace('</b>', '')

                for x in re.split(r'\,', new_line):
                    match = re.match(r'\s*(Fort|Ref|Will) (.*)', x)
                    if match.group(1) == 'Fort':
                        self.Fort = match.group(2)
                    elif match.group(1) == 'Ref':
                        self.Ref = match.group(2)
                    elif match.group(1) == 'Will':
                        self.Will = match.group(2)

            elif '<b>HP</b>' in line:
                new_line = bs4.BeautifulSoup(line, 'html.parser')
                data = re.split(r'\;', new_line.text)
                latest = None
                for d in data:
                    match = re.match(r'\s?(HP|Immunities|Resistances|Weaknesses)\s(.*)', d)
                    if match is None and latest is not None:
                        exec(latest)
                    elif match.group(1) == 'HP':
                        self.Hp = match.group(2)
                        latest = "self.Hp += d"
                    elif match.group(1) == 'Immunities':
                        self.Immune = match.group(2)
                        latest = "self.Immune += d"
                    elif match.group(1) == 'Resistances':
                        self.Resist = match.group(2)
                        latest = "self.Resist += d"
                    elif match.group(1) == 'Weaknesses':
                        self.Weak = match.group(2)
                        latest = "self.Weak += d"

            elif line.startswith('<b>Arcane') or line.startswith('<b>Divine') or line.startswith(
                    '<b>Occult') or line.startswith('<b>Primal') or line.startswith('<b>Monk') or line.startswith(
                    '<b>Champion'):
                print('\t\t\tSpell Work Begins')
                dc = int(line[line.index('DC ') + 3: line.index('DC ') + 5])

                data = bs4.BeautifulSoup(line, 'html.parser')
                # print(type(data.find_all('b')[1].next_sibling.next_sibling.next_sibling))
                # print(data.find_all('b')[1].next_sibling.next_sibling.next_sibling)
                data_split = line.split('<b>')
                for line in data_split[2:]:
                    level, spells = line.split('</b>')
                    temp_spell_line = {
                        'Dc': dc,
                        'Uses': level,
                        'List': [],
                    }
                    print('\t\t\t\tProcessing ' + level + ' level spells')
                    spells = bs4.BeautifulSoup(spells, 'html.parser')
                    for link in spells.find_all('a'):
                        print('\t\t\t\t\t' + link.text.title())
                        temp_spell = {
                            'Name': link.text.title(),
                            'Link': "https://2e.aonprd.com/" + link['href'],
                        }
                        temp_spell_line['List'].append(temp_spell)
                    self.Spells.append(temp_spell_line)

            else:
                print('\t\t\tAdding Ability')
                try:
                    temp_ab = {
                        'Name': line[line.index('<b>') + 3: line.index('</b>')]
                    }
                    print('\t\t\t\t' + temp_ab['Name'])
                    if temp_ab['Name'] in ['Critical Success', 'Critical Failure', 'Success', 'Failure']:
                        self.Abilities[-1]['Description'] += line[line.index('</b>'):].strip()
                    else:
                        temp_ab['Description'] = line[line.index('</b>') + 4:].strip()
                        self.Abilities.append(temp_ab)
                except Exception as e:
                    print('!! Unparsable Ability:')
                    print(line)

    def put_ability(self, action, cost):
        data = bs4.BeautifulSoup(action, 'html.parser')
        temp_a = {
            'Name': data.b.text.strip(),
            'Text': '<p>' + data.text[len(data.b.text):].strip() + '</p>',
            'Cost': cost

        }
        self.Actions.append(temp_a)

    def handle_actions(self, action):
        data = bs4.BeautifulSoup(action, 'html.parser')
        actions = data.find_all('span', recursive=False)
        for a in actions:
            cost = -2
            action = a.find('span')
            if action is None:
                cost = "1 Action"
            elif action['title'] == "Reaction":
                cost = "Reaction"
            elif action['title'] == "Free Action":
                cost = "Free"
            elif action['title'] == "Single Action":
                cost = "1 Action"
            elif action['title'] == "Two Actions":
                cost = "2 Action"
            elif action['title'] == "Three Actions":
                cost = "3 Action"
            print('\t\t\t\tAction: ' + a.b.text)
            temp_a = {
                'Name': str(a.b.text),
                'Text': '<p>' + a.text[len(a.b.text):].strip() + '</p>',
                'Cost': cost
            }
            self.Actions.append(temp_a)

    def get_dict(self):
        return self.__dict__


def fix_dict_diff(old, new):
    for key in old.keys():
        if key == '_copy':
            continue
        if key in new.keys():
            new[key] = old[key]
    return new


def modify_title(s):
    if ' Of ' in s:
        s = s.replace(' Of ', ' of ')
    if ' And ' in s:
        s = s.replace(' And ', ' and ')
    if ' The ' in s:
        s = s.replace(' The ', ' the ')
    if '-O\'-' in s:
        s = s.replace('-O\'-', '-o\'-')
    if 'Yuan-Ti' in s:
        s = s.replace('Yuan-Ti', 'Yuan-ti')
    if 'Parasite-Infested' in s:
        s = s.replace('Parasite-Infested', 'Parasite-infested')
    if 'Kuo-Toa' in s:
        s = s.replace('Kuo-Toa', 'Kuo-toa')
    if 'Thri-Kreen' in s:
        s = s.replace('Thri-Kreen', 'Thri-kreen')
    if 'Mend-Nets' in s:
        s = s.replace('Mend-Nets', 'Mend-nets')
    if 'Leuk-O' in s:
        s = s.replace('Leuk-O', 'Leuk-o')
    if 'Su-Monster' in s:
        s = s.replace('Su-Monster', 'Su-monster')
    if 'Ki-Rin' in s:
        s = s.replace('Ki-Rin', 'Ki-rin')
    if 'Tri-Flower' in s:
        s = s.replace('Tri-Flower', 'Tri-flower')
    if 'Play-By-Play' in s:
        s = s.replace('Play-By-Play', 'Play-by-Play')
    if "'S " in s:
        s = s.replace("'S ", "'s ")
    if "Blit'Zen" in s:
        s = s.replace("Blit'Zen", "Blit'zen")
    if "K'Thriss Drow'B" in s:
        s = s.replace("K'Thriss Drow'B", "K'thriss Drow'b")
    if "Bol'Bara" in s:
        s = s.replace("Bol'Bara", "Bol'bara")
    if "F'Yorl" in s:
        s = s.replace("F'Yorl", "F'yorl")
    if "Kith'Rak" in s:
        s = s.replace("Kith'Rak", "Kith'rak")
    if "Graz'Zt" in s:
        s = s.replace("Graz'Zt", "Graz'zt")
    if "Skr'A S'Orsk" in s:
        s = s.replace("Skr'A S'Orsk", "Skr'a S'orsk")
    if 'Aribeth De Tylmarande' in s:
        s = s.replace('Aribeth De Tylmarande', 'Aribeth de Tylmarande')
    if "Crokek'Toeck" in s:
        s = s.replace("Crokek'Toeck", "Crokek'toeck")
    if "D'Avenir" in s:
        s = s.replace("D'Avenir", "d'Avenir")
    if "Druu'Giir" in s:
        s = s.replace("Druu'Giir", "Druu'giir")
    if "Urb'Luu" in s:
        s = s.replace("Urb'Luu", "Urb'luu")
    if "Ur'Gray" in s:
        s = s.replace("Ur'Gray", "Ur'gray")
    if "Uk'Otoa" in s:
        s = s.replace("Uk'Otoa", "Uk'otoa")
    if "Talro'A" in s:
        s = s.replace("Talro'A", "Talro'a")
    if "Pu'Pu" in s:
        s = s.replace("Pu'Pu", "Pu'pu")
    if "O'Tamu" in s:
        s = s.replace("O'Tamu", "O'tamu")
    if "Fel'Rekt" in s:
        s = s.replace("Fel'Rekt", "Fel'rekt")
    if "Grum'Shar" in s:
        s = s.replace("Grum'Shar", "Grum'shar")
    if "Masq'Il'Yr" in s:
        s = s.replace("Masq'Il'Yr", "Masq'il'yr")
    if "Nar'L" in s:
        s = s.replace("Nar'L", "Nar'l")
    if "Al'Chaia" in s:
        s = s.replace("Al'Chaia", "Al'chaia")
    if "N'Ghathrod" in s:
        s = s.replace("N'Ghathrod", "N'ghathrod")
    if "Kol'Daan" in s:
        s = s.replace("Kol'Daan", "Kol'daan")
    if ' Von ' in s:
        s = s.replace(' Von ', ' von ')
    if 'Duloc' in s:
        s = s.replace('Duloc', 'DuLoc')
    if ' Van Der ' in s:
        s = s.replace(' Van Der ', ' van der ')
    if "Brain In Iron" in s:
        s = s.replace("Brain In Iron", "Brain in Iron")
    if "Brain In A Jar" in s:
        s = s.replace("Brain In A Jar", "Brain in a Jar")
    if " Devir" in s:
        s = s.replace(" Devir", " DeVir")
    if 'Ii' in s:
        s = s.replace('Ii', 'II')

    if 'Archon of Redemption' in s:
        s = s.replace('Archon of Redemption', 'Archon Of Redemption')
    if 'Nurvureem, the Dark Lady' in s:
        s = s.replace('Nurvureem, the Dark Lady', 'Nurvureem, The Dark Lady')

    return s


def process_actions_5etools(content, legendary):
    actions = []
    for action in content:
        if 'name' not in action.keys():
            continue
        if len(action['entries']) == 1 and isinstance(action['entries'][0], dict):
            text = de_dict(action['entries'][0])
        elif len(action['entries']) == 1:
            text = de_list(action['entries'])
        else:
            text = str(action['entries'])
        text = text.replace('{@atk mw}', '').replace('{@atk rw}', '').replace('{@atk mw,rw}', '').replace('{@atk rw,mw}', '')
        actions.append({'Name': action['name'], 'Text': text.strip(), 'Legendary': legendary})
    return actions


def get_spell_link(spell_name):
    try:
        return 'https://5e.tools/spells.html#' + spells_5etools_by_source[spell_name.lower()]
    except Exception as e:
        return 'Unable to find in 5e.tools'


def process_spells_5etools(content):
    all_spells = []
    spell_dc = '?'
    if 'headerEntries' in content.keys():
        match = re.search(r"@dc ([0-9]{2})", str(content))
        if match is not None:
            spell_dc = match.group(1)
    if 'daily' in content.keys():
        for uses in content['daily'].keys():
            temp_level = {
                'Uses': uses,
                'Dc': spell_dc,
                'List': []
            }
            for spell in content['daily'][uses]:
                if isinstance(spell, dict):
                    continue
                spell_name = spell.replace('{@spell', '').replace('}', '').strip()
                spell_link = get_spell_link(spell_name)
                temp_level['List'].append({'Name': spell_name.title(), 'Link': spell_link})
            all_spells.append(temp_level)
    if 'will' in content.keys():
        temp_level = {
            'Uses': 'At Will',
            'Dc': spell_dc,
            'List': []
        }
        for cantrip in content['will']:
            if isinstance(cantrip, dict):
                continue
            spell_name = cantrip.replace('{@spell', '').replace('}', '').strip()
            spell_link = get_spell_link(spell_name)
            temp_level['List'].append({'Name': spell_name.title(), 'Link': spell_link})
        all_spells.append(temp_level)
    return all_spells
