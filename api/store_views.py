from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.template.response import SimpleTemplateResponse
from django.template import engines, Template, Context
import generator.DMToolkit as dmk
from numpy.random import choice, randint
from . import views


def store_to_dict(store):
    store['Shopkeeper'] = store['Shopkeeper'].to_dict()
    for i in range(len(store['Stock'])):
        store['Stock'][i] = store['Stock'][i].to_dict()
    return store


# Create Weapon Store
def store_weapon_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_weapon_shop(views.npc_create(), [0, 4], quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_weapon(request):
    content = {}
    inner_html = store_weapon_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_weapon_json(request):
    content = {}
    store = store_weapon_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Random Armor Store
def store_armor_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_armor_shop(views.npc_create(), [0, 4], quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_armor(request):
    content = {}
    inner_html = store_armor_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_armor_json(request):
    content = {}
    store = store_armor_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Firearm Store
def store_firearm_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_gunsmith(views.npc_create(), [0, 4], quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_firearm(request):
    content = {}
    inner_html = store_firearm_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_firearm_json(request):
    content = {}
    store = store_firearm_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Random Book Store
def store_book_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_book_shop(views.npc_create(), ['Children', 'Drama', 'Fiction', 'Horror', 'Humor', 'Mystery', 'Nonfiction', 'Romance', 'SciFi', 'Tome'], quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_book(request):
    content = {}
    inner_html = store_book_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_book_json(request):
    content = {}
    store = store_book_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Random Enchantment Store
def store_enchanter_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_enchanter_shop(views.npc_create(), [0, 9], quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_enchanter(request):
    content = {}
    inner_html = store_enchanter_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_enchanter_json(request):
    content = {}
    store = store_enchanter_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Random Scroll Store
def store_scroll_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_enchantment_shop(views.npc_create(), [0, 9], quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_scroll(request):
    content = {}
    inner_html = store_scroll_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_scroll_json(request):
    content = {}
    store = store_scroll_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Random Potion Store
def store_potion_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_potion_shop(views.npc_create(), [0, 9], quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_potion(request):
    content = {}
    inner_html = store_potion_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_potion_json(request):
    content = {}
    store = store_potion_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Random Jewel Store
def store_jewel_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_jewel_shop(views.npc_create(), [0, 6], quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_jewel(request):
    content = {}
    inner_html = store_jewel_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_jewel_json(request):
    content = {}
    store = store_jewel_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Random General Store
def store_general_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_general_store(views.npc_create(), [0, 4], quantity, 3)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_general(request):
    content = {}
    inner_html = store_general_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_general_json(request):
    content = {}
    store = store_general_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Random Food Store
def store_food_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_restaurant(views.npc_create(), quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_food(request):
    content = {}
    inner_html = store_food_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_food_json(request):
    content = {}
    store = store_food_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Random Inn
def store_inn_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_tavern(views.npc_create(), 3, quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_inn(request):
    content = {}
    inner_html = store_inn_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_inn_json(request):
    content = {}
    store = store_inn_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))


# Create Random Variety Store
def store_variety_create(content={}, json=False):
    if 'Quantity' in content.keys():
        quantity = content['Quantity']
    else:
        quantity = 15
    store = dmk.store.stores.create_variety_shop(views.npc_create(), quantity)
    for key, value in content.items():
        if key in store.__dict__ and value is not None:
            store.__dict__[key] = value
    return store.__dict__ if json else store


def store_variety(request):
    content = {}
    inner_html = store_variety_create(content=content)
    template = Template("{% extends 'base.html' %}{% load static %}{% block content %}" + str(inner_html) + "{% endblock %}")
    return HttpResponse(template.render(Context({})))


def store_variety_json(request):
    content = {}
    store = store_variety_create(content=content, json=True)
    return JsonResponse(store_to_dict(store))

