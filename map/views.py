from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Town, Person


def __list_town_data():
    all_towns = Town.objects.all()
    towns = []
    for town in all_towns:
        towns.append({
            'coords': str(town.x_coord_min) + ',' + str(town.y_coord_min) + ',' + str(town.x_coord_max) + ',' + str(town.y_coord_max),
            'link': town.name.lower(),
            'name': town.name
        })
    return towns


# Create your views here.
def index(request):
    context = {
        'towns': __list_town_data(),
        'map_type': 'political'
    }
    return render(request, 'index.html', context)


def map(request, map_type):
    context = {
        'map_type': map_type
    }
    return render(request, 'index.html', context)


def town_info(request, town_name):
    try:
        town_data = Town.objects.all().filter(name=town_name.title())[0]
    except IndexError:
        raise Http404("Unable to find town: '" + town_name + "'")

    context = {
        'town_name': town_name.title(),
        'name': town_data.name,
        'description': town_data.description,
        'government': town_data.government,
        'governing_body': town_data.governing_body,
        'economy': town_data.economy,
        'population': town_data.population,
        'leader': town_data.leader.name + ', ' + town_data.leader.title,
    }

    return render(request, 'town.html', context)


def person_info(request, person_name):
    try:
        person_data = Person.objects.all().filter(name=person_name.title())[0]
    except IndexError:
        raise Http404("Unable to find Person: '" + person_name + "'")

    content = {
        'person_name': person_name,
        'person_title': person_data.title,
        'description': person_data.description,
    }
    return render(request, 'person.html', content)


def person_search(request):
    all_people = Person.objects.all()
    # I need a list of people's names sent. That's it.
    names = []
    for p in all_people:
        names.append(p.name)
    names.sort()
    all_names = {}
    for n in names:
        for m in n.split(' '):
            all_names[m] = n
    sorted_names = sorted(list(all_names.keys()))
    print(all_names)
    print(sorted_names)
    return render(request, 'person_search.html', {'names': names, 'name_dict': all_names, 'sorted_names': sorted_names})
