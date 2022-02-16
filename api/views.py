from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template.response import SimpleTemplateResponse
from django.template import engines, Template, Context
import generator.DMToolkit as dmk
from numpy.random import choice, randint


CR_SELECTION = [
    '0.13',
    '0.17',
    '0.25',
    '0.33',
    '0.5',
    '1.0',
    '2.0',
    '3.0',
    '4.0',
    '5.0',
    '6.0',
    '7.0',
    '8.0',
    '9.0',
    '10.0',
    '11.0',
    '12.0',
    '13.0',
    '14.0',
    '15.0',
    '16.0',
    '17.0',
    '18.0',
    '19.0',
    '20.0',
    '21.0',
    '22.0',
    '23.0',
    '24.0',
    '25.0',
    '26.0',
    '27.0',
    '28.0',
    '29.0',
    '30.0',
    '35.0',
    '37.0',
    '39.0'
]


# Usage Guide content and General funtions
def api(request):
    return render(request, 'api.html', {})


# Random NPCs
def npc_padding(char):
    return '<div class="wrapper-box" style="margin-bottom:60px;"><div style="padding:10px;"><b>Name:</b> ' + str(char) + '</div>'


def npc_create(content={}, json=False):
    person = dmk.people.character.create_person(dmk.core.variance.normal_settings())
    for key, value in content.items():
        if key in person.__dict__ and value is not None:
            person.__dict__[key] = value
    return person.__dict__ if json else person


def npc(request):
    content = {}
    inner_html = npc_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + npc_padding(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def npc_json(request):
    content = {}
    return JsonResponse(npc_create(content=content, json=True))


# Random PCs
def pc_padding(char):
    return '<div class="wrapper-box" style="margin-bottom:60px;"><div style="padding:10px;"><b>Name:</b> ' + str(char) + '</div>'


def pc_create(content={}, json=False):
    person = dmk.people.PC.PC(dmk.people.character.create_person(dmk.core.variance.normal_settings()))
    for key, value in content.items():
        if key in person.__dict__ and value is not None:
            person.__dict__[key] = value
    return person.__dict__ if json else person


def pc(request):
    content = {}
    inner_html = pc_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + pc_padding(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def pc_json(request):
    content = {}
    person = pc_create(content=content, json=True)
    person['Weapon'][0] = person['Weapon'][0].to_dict()
    person['Weapon'][1] = person['Weapon'][1].to_dict()
    return JsonResponse(person)


# Create Monster
def beast_create(version, content={}, json=True):
    name, beast = dmk.beasts.beastiary.random_monster(version)
    beast['Name'] = name
    return beast if json else dmk.beasts.beastiary.print_monster((name, beast), to_file=False)


def beast(request):
    content = {}
    return HttpResponse(beast_create('All', content=content, json=False))


def beast_json(request):
    content = {}
    return JsonResponse(beast_create('All', content=content, json=True))


def beast_5e(request):
    content = {}
    return HttpResponse(beast_create('D&D 5', content=content, json=False))


def beast_5e_json(request):
    content = {}
    return JsonResponse(beast_create('D&D 5', content=content, json=True))


def beast_pf1(request):
    content = {}
    return HttpResponse(beast_create('Pathfinder 1', content=content, json=False))


def beast_pf1_json(request):
    content = {}
    return JsonResponse(beast_create('Pathfinder 1', content=content, json=True))


# Create Random Treasure
def treasure_create(version, cr=0.0, json=True):
    return dmk.beasts.treasure.print_treasure(monster_cr=cr, monster_json=json)


def treasure_pf1(request):
    content = {}
    cr = choice(CR_SELECTION)
    return HttpResponse(treasure_create('Pathfinder 1', cr=cr, json=False))


def treasure_pf1_json(request):
    content = {}
    cr = choice(CR_SELECTION)
    return JsonResponse(treasure_create('Pathfinder 1', cr=cr, json=True), safe=False)


def treasure_pf1_cr(request, cr):
    content = {}
    if str(float(cr)) not in CR_SELECTION:
        raise Http404("Disallowed CR setting. Choose a number between 1 and 39")
    return HttpResponse(treasure_create('Pathfinder 1', cr=str(float(cr)), json=False))


def treasure_pf1_cr_json(request, cr):
    content = {}
    if str(float(cr)) not in CR_SELECTION:
        raise Http404("Disallowed CR setting. Choose a number between 1 and 39")
    treasure = treasure_create('Pathfinder 1', cr=str(float(cr)), json=True)
    return JsonResponse(treasure, safe=False)


# Choose Random Gear
# Choose Random Weapon
# Choose Random Firearm
# Choose Random Armor

