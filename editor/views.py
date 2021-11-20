from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
import simplejson as json
import bs4
import re
import requests
from .parse_tools import *


# Create your views here.
def editor(request):
    return render(request, 'editor.html', {})


def parser(request):
    if request.method != 'POST':
        return Http404("Unable to parse POST request")
    page_data = json.loads(request.body.decode('utf8'))

    # Handle creature Parsing
    new_data = None
    try:
        if page_data['Edition'] == '5' and '5e.tools' in page_data['URL']:
            new_data = parse_5etools(page_data['URL'])
        elif page_data['Edition'] == '5' and 'donjon.bin.sh' in page_data['URL']:
            pass
        elif page_data['Edition'] == '2' and '2e.aonprd.com' in page_data['URL']:
            new_data = parse_archives(page_data['URL'])
        elif page_data['Edition'] == '1':
            pass
    except Exception as e:
        print('\n!! Type: ', type(e))
        print('!! Args: ', e.args)
        print('!! Stack:', e, '\n')
        return JsonResponse({
            "ERROR": "There was a problem parsing that link. Please contact support found at the bottom of the page with the link you provided.",
            "EXCEPTION": str(e)
        }, safe=False)

    # Validate correctly configured info
    if new_data is None:
        return JsonResponse({"ERROR": "That link is not currently supported. If you wish for it to be supported, contact support found at the bottom of this page."})

    return JsonResponse(new_data, safe=False)


def parse_archives(url):
    # Make a request call to the website
    try:
        if 'AspxAutoDetectCookieSupport=1' not in url:
            url += '&AspxAutoDetectCookieSupport=1'
        file = requests.get(url)
    except Exception as e:
        return {
            "ERROR": "There was a problem importing from " + url,
            "EXCEPTION": str(e)
        }
    soup = bs4.BeautifulSoup(file.text, 'html.parser')

    # Create monster
    body = soup.find('div', class_='main')
    name = body.find_all('h1', class_='title')
    monster = Creature(name[0].text, url)

    # Traits and CR
    temp = name[1]
    monster.set_cr(temp.find('span').text.replace('Creature', '').strip())
    print("\tStarting body search")
    body = body.find_all('span')[4]

    # Get data from Raw Text
    monster.set_traits(
        body.find('span', class_=['traituncommon']),
        body.find('span', class_=['traitrare']),
        body.find('span', class_=['traitunique']),
        body.find('span', class_=['traitalignment']),
        body.find('span', class_=['traitsize']),
        body.find_all('span', class_=['trait'])
    )
    monster.set_from_raw_text(body.text)

    # Grab form Raw to get Source
    raw_text_split = re.split(r'<br />|<hr />', file.text)
    source_index = 0
    while source_index < len(raw_text_split):
        if raw_text_split[source_index].startswith('<b>Source</b>'):
            break
        source_index += 1

    # Source and other Boldened Text setters
    monster.set_source(bs4.BeautifulSoup(raw_text_split[source_index], 'html.parser'))
    executed = 0
    exists = 0
    for check in ['<b>Perception', '<b>Language', '<b>Skills', '<b>Str']:
        exists += 1 if check in str(body) else 0

    while executed < exists:
        source_index += 1
        if raw_text_split[source_index].startswith('<b>Perception'):
            monster.set_perception(bs4.BeautifulSoup(raw_text_split[source_index], 'html.parser'))
            executed += 1
        elif raw_text_split[source_index].startswith('<b>Language'):
            monster.set_languages(bs4.BeautifulSoup(raw_text_split[source_index], 'html.parser'))
            executed += 1
        elif raw_text_split[source_index].startswith('<b>Skills'):
            monster.set_skills(bs4.BeautifulSoup(raw_text_split[source_index], 'html.parser'))
            executed += 1
        elif raw_text_split[source_index].startswith('<b>Str'):
            monster.set_stats(bs4.BeautifulSoup(raw_text_split[source_index], 'html.parser'))
            executed += 1

    # Grab the remaining information
    raw_text_split = raw_text_split[source_index+1:]
    remaining = []
    for line in raw_text_split:
        if '<script' in line:
            break
        elif 'title="Sidebar - Additional Lore"' in line:
            remaining.append(line)
            break
        elif '</span><b>' in line:
            action, spell = line.split('</span><b>')
            remaining.append(action + '</span>')
            remaining.append('<b>' + spell)
        else:
            remaining.append(line)

    # Everything is now up in the air for how things are setup.
    monster.remaining_parser(remaining)

    print(monster.get_dict())
    base = {
        "Edition": "2",
        "Name": monster.Name,
        "Cr": monster.Cr,
        "Description": '<p>' + monster.Description + '</p>',
        "Alignment": monster.Alignment,
        "Traits": monster.Traits,
        "Hp": monster.Hp,
        "Speed": monster.Speed,
        "Size": monster.Size,
        "Ac": monster.Ac,
        "FortSave": monster.Fort,
        "WillSave": monster.Will,
        "RefSave": monster.Ref,
        "Skills": de_dict(monster.Skills),
        "Recall": monster.Recall,
        "DamImmune": monster.Immune,
        "DamResist": monster.Resist,
        "DamWeak": monster.Weak,
        "Sense": monster.Perception,
        "Language": str(monster.Languages)[1:-1],
        "Str": monster.Str,
        "Dex": monster.Dex,
        "Con": monster.Con,
        "Int": monster.Int,
        "Wis": monster.Wis,
        "Cha": monster.Cha,
        "Actions": monster.Actions,
        "Spells": monster.Spells,
        "Treasure": {
            "Data": []
        }
    }

    return base


def parse_donjon(url):
    pass


def parse_5etools(url):
    print("Parsing '", url, "' from 5e/tools")
    source_book = url[url.rfind('_')+1:]
    if source_book not in sources_5etools.keys():
        return {'ERROR': "This book is current;y not supported. Please contact support via email below."}
    try:
        file = requests.get(sources_5etools[source_book])
    except Exception as e:
        return {
            "ERROR": "There was a problem importing from " + url,
            "EXCEPTION": str(e)
        }
    data = json.loads(file.text)
    unparsed_name = parse.unquote_plus(url[url.find('#')+1 : url.rfind('_')])
    name = modify_title(unparsed_name.title())

    # Query for creature in received JSON
    creature = None
    for c in data['monster']:
        if c['name'] == name:
            creature = c
    if creature is None:
        return {"ERROR": "Unable to locate creature from 5e.tools"}

    # Validate if the creature is a copy
    while '_copy' in creature.keys():
        name = modify_title(creature['_copy']['name'])
        source = creature['_copy']['source']
        file = requests.get(sources_5etools[source.lower()])
        data = json.loads(file.text)
        old_creature = creature
        creature = None
        for c in data['monster']:
            if c['name'] == name:
                creature = c
        if creature is None:
            return {"ERROR": "Unable to locate creature from 5e.tools"}
        creature = fix_dict_diff(old_creature, creature)

    resist = ''
    if 'resist' in creature.keys():
        for point in creature['resist']:
            if isinstance(point, str):
                resist += point + ', '
            elif isinstance(point, dict):
                if 'resist' in point.keys() and 'note' in point.keys():
                    resist += de_list(point['resist']) + ' ' + point['note']
                elif 'special' in point.keys():
                    resist += point['special'] + ', '
    immune = ''
    if 'conditionImmune' in creature.keys():
        for p in creature['conditionImmune']:
            if isinstance(p, str):
                immune += p + ', '
            if isinstance(p, dict):
                immune += de_dict(p) + ', '
    if 'immune' in creature.keys() and creature['immune'] is not None:
        for p in creature['immune']:
            if isinstance(p, str):
                immune += p + ', '
            if isinstance(p, dict):
                immune += de_dict(p) + ', '

    vulnerable = ''
    if 'vulnerable' in creature.keys() and creature['vulnerable'] is not None:
        for p in creature['vulnerable']:
            if isinstance(p, str):
                vulnerable += p + ', '
            if isinstance(p, dict):
                vulnerable += de_dict(p) + ', '

    ac = ''
    if isinstance(creature['ac'][0], int):
        ac = str(creature['ac'][0])
    elif isinstance(creature['ac'][0], dict):
        if 'special' in creature['ac'][0].keys():
            ac = creature['ac'][0]['special']
        else:
            ac = str(creature['ac'][0]['ac'])
            if 'from' in creature['ac'][0].keys():
                ac += ' (' + str(creature['ac'][0]['from']) + ')'

    actions = []
    if 'action' in creature.keys() and creature['action'] is not None:
        actions += process_actions_5etools(creature['action'], False)
    if 'trait' in creature.keys() and creature['trait'] is not None:
        actions += process_actions_5etools(creature['trait'], False)
    if 'legendary' in creature.keys() and creature['legendary'] is not None:
        actions += process_actions_5etools(creature['legendary'], True)

    spells = []
    if 'spellcasting' in creature.keys() and creature['spellcasting'] is not None:
        spells = process_spells_5etools(creature['spellcasting'][0])

    align = ''
    if 'alignment' not in creature.keys():
        align = ''
    elif isinstance(creature['alignment'][0], str):
        align = ''.join(creature['alignment']) 
    else:
        align = str(creature['alignment'])

    hp_info = ''
    if 'special' in creature['hp'].keys():
        hp_info += str(creature['hp']['special'])
    else: 
        hp_info += str(creature['hp']['average'])
        if 'formula' in creature['hp'].keys():
            hp_info += ' (' + creature['hp']['formula'] + ')'

    target = {
        "Ac": ac,
        "Actions": actions,
        "Alignment": align,
        "Cha": creature['cha'],
        "ChaSave": True if 'save' in creature.keys() and 'cha' in creature['save'] else False,
        "Con": creature['con'],
        "ConSave": True if 'save' in creature.keys() and 'con' in creature['save'] else False,
        "Cr": creature['cr'] if 'cr' in creature.keys() else '',
        "DamImmune": immune,
        "DamResist": resist,
        "DamWeak": vulnerable,
        "Description": "<p></p>",
        "Dex": creature['dex'],
        "DexSave": True if 'save' in creature.keys() and 'dex' in creature['save'] else False,
        "Edition": "5",
        "Hp": hp_info,
        "Int": creature['int'],
        "IntSave": True if 'save' in creature.keys() and 'int' in creature['save'] else False,
        "Language": de_list(creature['languages']) if 'languages' in creature.keys() and creature['languages'] is not None else '',
        "Name": modify_title(unparsed_name.title()),
        "Sense": de_list(creature['senses']) if 'senses' in creature.keys() and creature['senses'] is not None else '',
        "Size": creature['size'],
        "Skills": de_dict(creature['skill']) if 'skill' in creature.keys() else '',
        "Speed": de_dict(creature['speed']),
        "Spells": spells,
        "Str": creature['str'],
        "StrSave": True if 'save' in creature.keys() and 'str' in creature['save'] else False,
        "Treasure": {"Data": []},
        "Wis": creature['wis'],
        "WisSave": True if 'save' in creature.keys() and 'wis' in creature['save'] else False,
    }
    
    return target
