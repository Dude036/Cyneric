from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template.response import SimpleTemplateResponse
from django.template import engines, Template, Context
import generator.DMToolkit as dmk
from numpy.random import choice, randint


def item_padding(char):
    return '<table class="inventory-table" style="width:100%">' + str(char) + '</table>'



# Create Random Weapon
def item_weapon_create(rarity, content={}, json=False):
    item = dmk.store.items.Weapon(rarity)
    for key, value in content.items():
        if key in item.__dict__ and value is not None:
            item.__dict__[key] = value
    return item.to_dict() if json else item


def item_weapon(request):
    content = {}
    inner_html = item_weapon_create(randint(0, 5), content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_weapon_json(request):
    content = {}
    item = item_weapon_create(randint(0, 5), content=content, json=True)
    return JsonResponse(item)


def item_weapon_r(request, r):
    content = {}
    inner_html = item_weapon_create(r, content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_weapon_r_json(request, r):
    content = {}
    item = item_weapon_create(r, content=content, json=True)
    return JsonResponse(item)


# Create Random Firearm
def item_firearm_create(rarity, content={}, json=False):
    item = dmk.store.items.Firearm(rarity)
    for key, value in content.items():
        if key in item.__dict__ and value is not None:
            item.__dict__[key] = value
    return item.to_dict() if json else item


def item_firearm(request):
    content = {}
    inner_html = item_firearm_create(randint(0, 5), content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_firearm_json(request):
    content = {}
    item = item_firearm_create(randint(0, 5), content=content, json=True)
    return JsonResponse(item)


def item_firearm_r(request, r):
    content = {}
    inner_html = item_firearm_create(r, content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_firearm_r_json(request, r):
    content = {}
    item = item_firearm_create(r, content=content, json=True)
    return JsonResponse(item)


# Create Random Armor
def item_armor_create(rarity, content={}, json=False):
    item = dmk.store.items.Armor(rarity)
    for key, value in content.items():
        if key in item.__dict__ and value is not None:
            item.__dict__[key] = value
    return item.to_dict() if json else item


def item_armor(request):
    content = {}
    inner_html = item_armor_create(randint(0, 5), content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_armor_json(request):
    content = {}
    item = item_armor_create(randint(0, 5), content=content, json=True)
    return JsonResponse(item)


def item_armor_r(request, r):
    content = {}
    inner_html = item_armor_create(r, content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_armor_r_json(request, r):
    content = {}
    item = item_armor_create(r, content=content, json=True)
    return JsonResponse(item)


# Create Random Scroll
def item_scroll_create(rarity, content={}, json=False):
    item = dmk.store.items.Scroll(rarity)
    for key, value in content.items():
        if key in item.__dict__ and value is not None:
            item.__dict__[key] = value
    return item.to_dict() if json else item


def item_scroll(request):
    content = {}
    inner_html = item_scroll_create(randint(0, 10), content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_scroll_json(request):
    content = {}
    item = item_scroll_create(randint(0, 10), content=content, json=True)
    return JsonResponse(item)


def item_scroll_r(request, r):
    content = {}
    inner_html = item_scroll_create(r % 10, content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_scroll_r_json(request, r):
    content = {}
    item = item_scroll_create(r % 10, content=content, json=True)
    return JsonResponse(item)


# Create Random Potion
def item_potion_create(rarity, content={}, json=False):
    item = dmk.store.items.Potion(rarity)
    for key, value in content.items():
        if key in item.__dict__ and value is not None:
            item.__dict__[key] = value
    return item.to_dict() if json else item


def item_potion(request):
    content = {}
    inner_html = item_potion_create(randint(0, 10), content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_potion_json(request):
    content = {}
    item = item_potion_create(randint(0, 10), content=content, json=True)
    return JsonResponse(item)


def item_potion_r(request, r):
    content = {}
    inner_html = item_potion_create(r % 10, content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_potion_r_json(request, r):
    content = {}
    item = item_potion_create(r % 10, content=content, json=True)
    return JsonResponse(item)


# Create Random Enchantment
# Create Random Book
def item_book_create(rarity, content={}, json=False):
    item = dmk.store.items.Book(rarity)
    for key, value in content.items():
        if key in item.__dict__ and value is not None:
            item.__dict__[key] = value
    return item.to_dict() if json else item


def item_book(request):
    content = {}
    inner_html = item_book_create(randint(0, 10), content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_book_json(request):
    content = {}
    item = item_book_create(randint(0, 10), content=content, json=True)
    return JsonResponse(item)


# Create Random Food
def item_food_create(rarity, content={}, json=False):
    item = dmk.store.items.Food(rarity)
    for key, value in content.items():
        if key in item.__dict__ and value is not None:
            item.__dict__[key] = value
    return item.to_dict() if json else item


def item_food(request):
    content = {}
    inner_html = item_food_create(0, content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_food_json(request):
    content = {}
    item = item_food_create(0, content=content, json=True)
    return JsonResponse(item)


# Create Random Trinket
def item_trinket_create(rarity, content={}, json=False):
    item = dmk.store.items.General(rarity, trinket=True)
    for key, value in content.items():
        if key in item.__dict__ and value is not None:
            item.__dict__[key] = value
    return item.to_dict() if json else item


def item_trinket(request):
    content = {}
    inner_html = item_trinket_create(0, content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + item_padding(str(inner_html)) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def item_trinket_json(request):
    content = {}
    item = item_trinket_create(0, content=content, json=True)
    return JsonResponse(item)

