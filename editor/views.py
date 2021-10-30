from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
import simplejson as json
import bs4
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


def parse_archives(url):
    file = requests.get(url)
    soup = bs4.BeautifulSoup(file.text, 'html.parser')
    base = {
        "Edition": "2",
        "Name": "",
        "Cr": "",
        "Description": "<p></p>",
        "Alignment": "",
        "Traits": [],
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
        "Actions": [],
        "Spells": [],
        "Treasure": {
            "Data": []
        }
    }

    return base
