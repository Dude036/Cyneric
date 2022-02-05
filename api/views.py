from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template.response import SimpleTemplateResponse
from django.template import engines, Template, Context
import generator.DMToolkit as dmk

# Usage Guide content
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


# Create Random Weapon
# Create Random Firearm
# Create Random Armor
# Create Random Scroll
# Create Random Potion
# Create Random Enchantment
# Create Random Book
# Create Random Food
# Create Random Trinket

# Choose Random Gear
# Choose Random Weapon
# Choose Random Firearm
# Choose Random Armor

