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
# Random Item (Created)
# Random Item (Existing)
# Random Gear

