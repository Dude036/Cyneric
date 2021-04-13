from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Town, Person


# Create your views here.
def index(request):
    all_towns = Town.objects.all()
    towns = []
    for town in all_towns:
        towns.append({
            'coords': str(town.x_coord_min) + ',' + str(town.y_coord_min) + ',' + str(town.x_coord_max) + ',' + str(town.y_coord_max),
            'link': town.name.lower(),
            'name': town.name
        })
    context = {
        'towns': towns,
        'map_type': 'political'
    }
    return render(request, 'index.html', context)


def map(request, map_type):
    all_towns = Town.objects.all()
    context = {
        'map_type': map_type
    }
    return render(request, 'index.html', context)


def town_info(request, town_name):
    try:
        town_data = Town.objects.all().filter(name=town_name.title())[0]
    except Town.DoesNotExist:
        raise Http404("Unable to find town: '" + town_name + "'")

    context = {
        'town_name': town_name.title(),
        'name': town_data.name,
        'description': town_data.description,
        'government': town_data.government,
        'governing_body': town_data.governing_body,
        'economy': town_data.economy,
        'population': town_data.population,
        'leader': "Placeholder",
    }

    return render(request, 'town.html', context)


def person_info(request, person_name):
    return render(request, 'index.html', {'map_type': 'political'})
