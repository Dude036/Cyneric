from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
import simplejson as json
import bs4
import re
import requests


# Create your views here.
def editor(request):
    return render(request, 'editor.html', {})


def parser(request):
    if request.method != 'POST':
        return Http404("Unable to parse POST request")
    page_data = json.loads(request.body.decode('utf8'))
    print(page_data)
    new_data = None
    if page_data['Edition'] == '5':
        pass
    elif page_data['Edition'] == '2':
        new_data = parse_archives(page_data['URL'])
    elif page_data['Edition'] == '1':
        pass

    # Validate correctly configured info
    if new_data is None:
        return JsonResponse({"ERROR": "That link is not currently not supported. If you wish for it to be supported, contact support found at the bottom of this page."})

    return JsonResponse(new_data)


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
        if match is None:
            self.Description = text[0 : text.index('Recall Knowledge')]
            self.Description = self.Description.encode(encoding='utf-8', errors='replace')
        else:
            self.Description = text[text.find(match.group(1)) + 1 : text.index('Recall Knowledge')]

        print("\t\tSetting Recall")
        dc = text.find('DC ', text.index('Recall Knowledge'))
        s = text.find('(', text.index('Recall Knowledge'))
        e = text.find(')', text.index('Recall Knowledge'))
        self.Recall = text[s+1 : e] + ': ' + text[dc: dc+5]

    def set_traits(self, uncommon, align, size, traits):
        print("\t\tSetting Traits")
        if uncommon is not None:
            self.Traits.append('Uncommon')
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
                self.Ac = new_line.text.split('; ')[0][3:]
                new_line = new_line.text.split('; ')[1]

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
                for d in data:
                    match = re.match(r'\s?(HP|Immunities|Resistances|Weaknesses)\s(.*)', d)
                    if match.group(1) == 'HP':
                        self.Hp = match.group(2)
                    elif match.group(1) == 'Immunities':
                        self.Immune = match.group(2)
                    elif match.group(1) == 'Resistances':
                        self.Resist = match.group(2)
                    elif match.group(1) == 'Weaknesses':
                        self.Weak = match.group(2)

            elif line.startswith('<b>Arcane') or line.startswith('<b>Divine') or line.startswith('<b>Occult') or line.startswith('<b>Primal') or line.startswith('<b>Monk') or line.startswith('<b>Champion'):
                print('\t\t\tSpell Work Begins')
                dc = int(line[line.index('DC ')+3 : line.index('DC ')+5])

                data = bs4.BeautifulSoup(line, 'html.parser')
                # print(type(data.find_all('b')[1].next_sibling.next_sibling.next_sibling))
                # print(data.find_all('b')[1].next_sibling.next_sibling.next_sibling)
                data_split = line.split('<b>')
                for line in data_split[2:]:
                    level, spells = line.split('</b>')
                    print('\t\t\t\tProcessing ' + level + ' level spells')
                    spells = bs4.BeautifulSoup(spells, 'html.parser')
                    for link in spells.find_all('a'):
                        print('\t\t\t\t\t' + link.text.title())
                        temp_spell = {
                            'Name': link.text.title(),
                            'Level': level,
                            'Link': "https://2e.aonprd.com/" + link['href'],
                            'DC': dc
                        }
                        self.Spells.append(temp_spell)

            else:
                print('\t\t\tAdding Ability')
                try:
                    temp_ab = {
                        'Name': line[line.index('<b>')+3 : line.index('</b>')]
                    }
                    print('\t\t\t\t' + temp_ab['Name'])
                    if temp_ab['Name'] in ['Critical Success', 'Critical Failure', 'Success', 'Failure']:
                        self.Abilities[-1]['Description'] += line[line.index('</b>'):].strip()
                    else:
                        temp_ab['Description'] = line[line.index('</b>')+4:].strip()
                        self.Abilities.append(temp_ab)
                except Exception as e:
                    print('!! Unparsable Ability:')
                    print(line)

    def put_ability(self, action, cost):
        data = bs4.BeautifulSoup(action, 'html.parser')
        temp_a = {
            'Name': data.b.text.strip(),
            'Description': data.text[len(data.b.text):].strip(),
            'Cost': cost

        }
        self.Actions.append(temp_a)

    def handle_actions(self, action):
        data = bs4.BeautifulSoup(action, 'html.parser')
        actions =  data.find_all('span')
        for a in actions:
            cost = -2
            image = a.find('img', alt=True)
            if image is None:
                cost = 0
            elif image['alt'] == "Reaction":
                cost = -1
            elif image['alt'] == "Free Action":
                cost = 0
            elif image['alt'] == "Single Action":
                cost = 1
            elif image['alt'] == "Two Actions":
                cost = 2
            elif image['alt'] == "Three Actions":
                cost = 3
            print('\t\t\t\tAction: ' + a.b.text)
            temp_a = {
                'Name': str(a.b.text),
                'Description': a.text[len(a.b.text):].strip(),
                'Cost': cost
            }
            self.Actions.append(temp_a)

    def get_dict(self):
        return self.__dict__


def parse_archives(url):
    # Make a request call to the website
    file = requests.get(url)
    soup = bs4.BeautifulSoup(file.text, 'html.parser')

    # Create monster
    body = soup.find('div', class_='main')
    name = body.find_all('h1', class_='title')
    monster = Creature(name[0].text, url)

    # Traits and CR
    temp = name[1]
    monster.set_cr(temp.find('span').text.replace('Creature', '').strip())
    monster.set_traits(
        body.find('span', class_=['traituncommon']),
        body.find('span', class_=['traitalignment']),
        body.find('span', class_=['traitsize']),
        body.find_all('span', class_=['trait'])
    )

    # Grab form Raw to get Source
    raw_text_split = re.split(r'<br />|<hr />', file.text)
    source_index = 0
    while source_index < len(raw_text_split):
        if raw_text_split[source_index].startswith('<b>Source</b>'):
            break
        source_index += 1


    print(monster.get_dict())
    base = {
        "Edition": "2",
        "Name": monster.Name,
        "Cr": monster.Cr,
        "Description": "<p></p>",
        "Alignment": "",
        "Traits": monster.Traits,
        "Hp": "",
        "Speed": "",
        "Size": "",
        "Ac": "",
        "FortSave": "",
        "WillSave": "",
        "RefSave": "",
        "Skills": "",
        "Recall": "",
        "DamImmune": "",
        "DamResist": "",
        "DamWeak": "",
        "Sense": "",
        "Language": "",
        "Str": "",
        "Dex": "",
        "Con": "",
        "Int": "",
        "Wis": "",
        "Cha": "",
        "Actions": [
            {
                "Name": "",
                "Cost": "1 Action",
                "Text": "<p></p>"
            }
        ],
        "Spells": [
            {
                "Dc": 0,
                "List": [
                    {
                        "Name": "",
                        "Link": "",
                    }
                ],
                "Usage": "<p></p>"
            }
        ],
        "Treasure": {
            "Data": []
        }
    }

    return base
