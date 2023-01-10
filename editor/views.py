from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.contrib import auth
import simplejson as json
import bs4
import re
import requests
from .parse_tools import *


# Create your views here.
def admin_view(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)
    if user.is_authenticated:
        return render(request, 'editor_admin.html', {'is_admin': user.is_authenticated})
    else:
        return HttpResponseRedirect('/editor/')


def admin_action(request, action):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)
    if not user.is_authenticated:
        HttpResponseRedirect('/editor/')

    if request.method != 'POST':
        return Http404("Unable to parse POST request")

    page_data = json.loads(request.body.decode('utf8'))

    if action == 1:
        print("FLUSHING 5E.TOOLS CACHE FROM LOCAL")

        cache_results = cache_5etools_json(force=True)
        populate_5e_json_helpers()
        return JsonResponse(cache_results, safe=False)
    else:
        return JsonResponse({'ERROR': 'Unknown Action Requested!'}, safe=False)


def editor(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)
    return render(request, 'editor.html', {'is_admin': user.is_authenticated})


def parser(request):
    if request.method != 'POST':
        return Http404("Unable to parse POST request")
    page_data = json.loads(request.body.decode('utf8'))

    new_data = None
    if page_data['Type'] == "Hazard":
        # Handle hazard Parsing
        try:
            if page_data['Edition'] == '5' and '5e.tools' in page_data['URL']:
                new_data = {
                    "ERROR": "This feature is currently in Development. Contact support via the email found on the bottom of the screen if your request is urgent.",
                    "EXCEPTION": ""
                }
            elif page_data['Edition'] == '5' and 'donjon.bin.sh' in page_data['URL']:
                new_data = {
                    "ERROR": "This feature is currently in Development. Contact support via the email found on the bottom of the screen if your request is urgent.",
                    "EXCEPTION": ""
                }
            elif page_data['Edition'] == '2' and '2e.aonprd.com' in page_data['URL']:
                new_data = parse_archive_hazard(page_data['URL'])
            elif page_data['Edition'] == '1' and 'd20pfsrd.com' in page_data['URL']:
                new_data = {
                    "ERROR": "This feature is currently in Development. Contact support via the email found on the bottom of the screen if your request is urgent.",
                    "EXCEPTION": ""
                }
            else:
                new_data = {
                    "ERROR": "The link we recieved is to a site that is not supported. If you would like to request a site be added as importable, contact support using the email found on the bottom of the page.",
                    "EXCEPTION": ""
                }
        except Exception as e:
            print('\n!! Type: ', type(e))
            print('!! Args: ', e.args)
            print('!! Stack:', e, '\n')
            return JsonResponse({
                "ERROR": "There was a problem parsing that link. Please contact support found at the bottom of the page with the link you provided.",
                "EXCEPTION": str(e)
            }, safe=False)

    elif page_data['Type'] == "Monster":
        # Handle creature Parsing
        try:
            if page_data['Edition'] == '5' and '5e.tools' in page_data['URL']:
                new_data = parse_5etools(page_data['URL'])
            elif page_data['Edition'] == '5' and 'donjon.bin.sh' in page_data['URL']:
                new_data = {
                    "ERROR": "This feature is currently in Development. Contact support via the email found on the bottom of the screen if your request is urgent.",
                    "EXCEPTION": ""
                }
            elif page_data['Edition'] == '2' and '2e.aonprd.com' in page_data['URL']:
                new_data = parse_archives(page_data['URL'])
            elif page_data['Edition'] == '1' and 'd20pfsrd.com' in page_data['URL']:
                new_data = {
                    "ERROR": "This feature is currently in Development. Contact support via the email found on the bottom of the screen if your request is urgent.",
                    "EXCEPTION": ""
                }
            else:
                new_data = {
                    "ERROR": "The link we recieved is to a site that is not supported. If you would like to request a site be added as importable, contact support using the email found on the bottom of the page.",
                    "EXCEPTION": ""
                }
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


def parse_archive_hazard(url):
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

    base = {
        "Edition": "2",
        "Name": '',
        "Cr": '',
        "Traits": [],
        "Complexity": '',
        "Stealth": '',
        "Description": '',
        "Disable": '',
        "Custom": []
    }
    try:
        soup = bs4.BeautifulSoup(file.text, 'html.parser')

        # Hazard Parsing with Title
        body = soup.find('div', class_='main')
        name = body.find_all('h1', class_='title')
        title = name[0].text[:name[0].text.find("Hazard")]
        base['Name'] = title
        cr = name[0].text[name[0].text.find("Hazard") + 6:]
        base['Cr'] = cr

        # Add Traits and split into sections
        raw_traits = body.find_all('span', class_=['trait'])
        base['Traits'] = [t.text for t in raw_traits]
        sections = re.split(r'<br\s*/>|<hr\s*/>', file.text)

        for s in sections:
            if not s.startswith("<b>") or s.startswith("<b>Source"):
                # Skip all section that don't start with <b>
                continue
            elif s.startswith("<b>Complexity") or s.startswith("<b>Stealth") or s.startswith("<b>Description") or s.startswith("<b>Disable"):
                # Standard sections with every trap
                contents = re.match(r'<b>([^\<]*)<\/b>(.*)', s)
                base[contents.group(1)] = contents.group(2).strip()
            elif s.startswith("<b>AC"):
                # AC has several sections inside it. Fill out seperately
                contents = re.findall(r'<b>([^\<]*)<\/b>([^\<]*)', s)
                for c in contents:
                    base['Custom'].append({c[0]: re.sub('<[^<]+?>', '', c[1].strip())})
            else:
                # Special cases go into custom
                contents = re.match(r'<b>([^\<]*)<\/b>(.*)', s)
                base['Custom'].append({contents.group(1): re.sub('<[^<]+?>', '', contents.group(2).strip())})
                
        return base
    except Exception as e:
        base['Description'] = 'ERROR! There was an error processing this Hazard. See Stack trace below\n----------------\n' + str(e) + ' \n----------------\n' + base['Description']
        return base


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
        "Type": "Monster",
        "Edition": "2",
        "Name": monster.Name,
        "Cr": monster.Cr,
        "Xp": '',
        "Description": '<p>' + monster.Description + '</p>',
        "Alignment": monster.Alignment,
        "Traits": monster.Traits,
        "HP": monster.Hp,
        "Speed": monster.Speed,
        "Size": monster.Size,
        "AC": monster.Ac,
        "Fortitude Save": monster.Fort,
        "Will Save": monster.Will,
        "Reflex Save": monster.Ref,
        "Skills": de_dict(monster.Skills),
        "Recall Knowledge": monster.Recall,
        "Damage Immunities": monster.Immune,
        "Damage Resistances": monster.Resist,
        "Damage Weakness": monster.Weak,
        "Senses": monster.Perception,
        "Languages": str(monster.Languages)[1:-1],
        "STR": monster.Str,
        "DEX": monster.Dex,
        "CON": monster.Con,
        "INT": monster.Int,
        "WIS": monster.Wis,
        "CHA": monster.Cha,
        "Actions": monster.Actions,
        "Spells": monster.Spells,
        "Treasure": {
            "Type": "",
            "Data": []
        }
    }

    return base


def parse_donjon(url):
    pass


def parse_5etools(url):
    print("Parsing '", url, "' from 5e/tools")
    source_book = url[url.rfind('_')+1:]
    special_book_list = {x.lower():x for x in sources_5etools.keys()}
    if source_book not in special_book_list.keys():
        return {'ERROR': "This book is currently not supported. Please contact support via email below."}
    try:
        print(special_book_list[source_book])
        with open(os.path.join(os.getcwd(), 'static', 'cache', sources_5etools[special_book_list[source_book]]), 'r') as inf:
            file = inf.read()
    except Exception as e:
        return {
            "ERROR": "There was a problem importing from " + url,
            "EXCEPTION": str(e)
        }
    data = json.loads(file)
    unparsed_name = parse.unquote_plus(url[url.find('#')+1 : url.rfind('_')])
    name = modify_title(unparsed_name.title())
    target = {
        'Type': 'Monster',
        'Edition': '5',
        'Description': '<p></p>',
        "Treasure": {
            "Type": "",
            "Data": []
        }
    }

    try:
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

        # Creature Established, building JSON
        # Static Elements First
        target["CHA"] = creature['cha']
        target["CHA Save"] = True if 'save' in creature.keys() and 'cha' in creature['save'] else False
        target["CON"] = creature['con']
        target["CON Save"] = True if 'save' in creature.keys() and 'con' in creature['save'] else False
        target["Cr"] = creature['cr'] if 'cr' in creature.keys() else ''
        target["DEX"] = creature['dex']
        target["DEX Save"] = True if 'save' in creature.keys() and 'dex' in creature['save'] else False
        target["INT"] = creature['int']
        target["INT Save"] = True if 'save' in creature.keys() and 'int' in creature['save'] else False
        target["Language"] = de_list(creature['languages']) if 'languages' in creature.keys() and creature['languages'] is not None else ''
        target["Name"] = modify_title(unparsed_name.title())
        target["Sense"] = de_list(creature['senses']) if 'senses' in creature.keys() and creature['senses'] is not None else ''
        target["Size"] = elongate_size(creature['size'])
        target["Skills"] = de_dict(creature['skill']) if 'skill' in creature.keys() else ''
        target["Speed"] = de_dict(creature['speed'])
        target["STR"] = creature['str']
        target["STR Save"] = True if 'save' in creature.keys() and 'str' in creature['save'] else False
        target["WIS"] = creature['wis']
        target["WIS Save"] = True if 'save' in creature.keys() and 'wis' in creature['save'] else False
        target["Xp"] = xp_by_cr(creature['cr'])

        # Potential mixup could kill the following.
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
        target['Damage Resistances'] = resist

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
        target['Damage Immunities'] = immune
        
        vulnerable = ''
        if 'vulnerable' in creature.keys() and creature['vulnerable'] is not None:
            for p in creature['vulnerable']:
                if isinstance(p, str):
                    vulnerable += p + ', '
                if isinstance(p, dict):
                    vulnerable += de_dict(p) + ', '
        target['Damage Weakness'] = vulnerable

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
        target['AC'] = ac

        actions = []
        if 'action' in creature.keys() and creature['action'] is not None:
            actions += process_actions_5etools(creature['action'], False)
        if 'trait' in creature.keys() and creature['trait'] is not None:
            actions += process_actions_5etools(creature['trait'], False)
        if 'legendary' in creature.keys() and creature['legendary'] is not None:
            actions += process_actions_5etools(creature['legendary'], True)
        target['Actions'] = actions

        spells = []
        if 'spellcasting' in creature.keys() and creature['spellcasting'] is not None:
            spells = process_spells_5etools(creature['spellcasting'][0])
        target['Spells'] = spells


        align = ''
        if 'alignment' not in creature.keys():
            align = ''
        elif isinstance(creature['alignment'][0], str):
            align = ''.join(creature['alignment']) 
        else:
            align = str(creature['alignment'])
        target['Alignment'] = align

        hp_info = ''
        if 'special' in creature['hp'].keys():
            hp_info += str(creature['hp']['special'])
        else: 
            hp_info += str(creature['hp']['average'])
            if 'formula' in creature['hp'].keys():
                hp_info += ' (' + creature['hp']['formula'] + ')'
        target['HP'] = hp_info

    except Exception as e:
        target['EXCEPTION'] = e 
        print("Error while parsing: " + url)
        print(e)
        print('-------------------------')
    finally:
        return target
