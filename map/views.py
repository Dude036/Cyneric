from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Town, Person, Critical, InitEntry
from .forms import CritForm
from django.contrib import auth
from os import path
import simplejson as json
from generator.DMToolkit.beasts.beastiary import roll_hp
from numpy.random import randint


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
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    context = {
        'towns': __list_town_data(),
        'map_type': 'political',
        'is_admin': user.is_authenticated,
    }
    return render(request, 'index.html', context)


def map_info(request, map_type):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    context = {
        'map_type': map_type,
        'is_admin': user.is_authenticated
    }
    return render(request, 'index.html', context)


def town_info(request, town_name):
    try:
        town_data = Town.objects.all().filter(name=town_name.title())[0]
    except IndexError:
        raise Http404("Unable to find town: '" + town_name + "'")

    if town_data.leader is not None:
        leader_info = town_data.leader.name + ', ' + town_data.leader.title
        leader_link = town_data.leader.name
        leader_desc = town_data.leader.description
    else:
        leader_info = 'N/A'
        leader_link = ''
        leader_desc = ''

    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    context = {
        'town_name': town_name.title(),
        'img_src': 'img/' + town_data.img_source if town_data.img_source is not None and town_data.img_source != '' else '',
        'name': town_data.name,
        'description': town_data.description,
        'government': town_data.government,
        'governing_body': town_data.governing_body,
        'economy': town_data.economy,
        'population': format(town_data.population, ',d'),
        'leader': leader_info,
        'leader_desc': leader_desc,
        'leader_link': leader_link,
        'is_admin': user.is_authenticated,
        'magic_phrase': town_data.magic_phrase,
        'admin_description': town_data.admin_description,
    }

    return render(request, 'town.html', context)


def town_search(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    town_data = Town.objects.all()
    names = []
    for p in town_data:
        names.append(p.name)
    names.sort()
    all_names = {}
    for n in names:
        for m in n.split(' '):
            all_names[m] = n
    sorted_names = sorted(list(all_names.keys()))
    return render(request, 'town_search.html', {'names': names, 'name_dict': all_names, 'sorted_names': sorted_names, 'is_admin': user.is_authenticated})


def person_info(request, person_name):
    try:
        person_data = Person.objects.all().filter(name=person_name.title())[0]
        town_link = ''
        for town in Town.objects.all():
            if town.leader is not None and town.leader.name == person_name:
                town_link = town.name
    except IndexError:
        raise Http404("Unable to find Person: '" + person_name + "'")

    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    content = {
        'person_name': person_name,
        'person_title': person_data.title,
        'description': person_data.description,
        'town_link': town_link,
        'is_admin': user.is_authenticated,
        'admin_description': person_data.admin_description,
        'img_src': 'img/' + person_data.img_source if person_data.img_source is not None and person_data.img_source != '' else '',
    }
    return render(request, 'person.html', content)


def person_search(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

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
    return render(request, 'person_search.html', {'names': names, 'name_dict': all_names, 'sorted_names': sorted_names, 'is_admin': user.is_authenticated})


def crit(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    return render(request, 'crit.html', {'is_admin': user.is_authenticated})


def add_crit(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CritForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            success_bool = True if form.data['success'] == 'Success' else False

            new_crit = Critical(
                category=form.data['category'],
                severity=form.data['severity'],
                success=success_bool,
                flavor_text=form.data['flavor_text']
            )
            new_crit.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/crit/form/success/')
        else:
            return HttpResponse('The content was malformed, and unable to be processed. Please verify your submission is valid, and try again.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CritForm()
    return render(request, 'add_crit.html', {'form': form, 'is_admin': user.is_authenticated})


def add_crit_success(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    return render(request, 'add_crit_success.html', {'is_admin': user.is_authenticated})


def admin_redirect(request):
    return HttpResponseRedirect('/admin/')


def magic_phrases(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    return render(request, 'phrases.html', {'is_admin': user.is_authenticated})


def initiative(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    return render(request, 'initiative.html', {'is_admin': user.is_authenticated})


def format_initiative_tracker(user):
    outgoing = []

    for entry in InitEntry.objects.all().order_by('-initiative'):
        data_point = {
            'Name': entry.name,
            'Init': entry.initiative
        }
        if user.is_authenticated:
            data_point['AC'] = entry.ac
            data_point['HP'] = entry.hp
            data_point['Conditions'] = entry.conditions
        outgoing.append(data_point)
    return outgoing


def initiative_form_validate(incoming):
    # Name validation
    if 'Name' not in incoming['data'].keys():
        print("Name missing from form")
        return False
    elif not isinstance(incoming['data']['Name'], str):
        print("Name is not a string")
        return False
    elif len(incoming['data']['Name']) == 0:
        print("Name does not contain any data.")
        return False

    return True


def initiative_data_form_validate(incoming):
    for num in ['Init', 'AC', 'HP']:
        if num not in incoming['data'].keys():
            print(num + " missing from form.")
            return False
        elif not isinstance(incoming['data'][num], int):
            print(num + " is not an integer.")
            return False

    return True


def bulk_initiative_data_form_validate(incoming):
    for num in ['Init', 'AC', 'Quantity']:
        if num not in incoming['data'].keys():
            print(num + " missing from form.")
            return False
        elif not isinstance(incoming['data'][num], int):
            print(num + " is not an integer.")
            return False

    if 'HD' not in incoming['data'].keys():
        print("HD missing from form.")
        return False
    elif not isinstance(incoming['data']['HD'], str):
        print("HD is not a string")
        return False

    return True


def initiative_request(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)
    if request.method == 'POST':
        # Handle POST data
        incoming = json.loads(request.body.decode('utf8'))
        print("New request for Initiative:", incoming)

        if not initiative_form_validate(incoming):
            print("Initiative form filled out incorrectly. Ignoring...")
            return JsonResponse(format_initiative_tracker(user), safe=False)

        # Add to Database
        if incoming['function'] == 'add' and user.is_authenticated:
            print("Adding " + incoming['data']['Name'] + " to the initiative tracker")
            initiative_data_form_validate(incoming)
            new_entry = InitEntry(name=incoming['data']['Name'], initiative=incoming['data']['Init'], ac=incoming['data']['AC'], hp=incoming['data']['HP'])
            new_entry.save()

        # Bulk funtionality
        if incoming['function'] == 'bulk' and user.is_authenticated:
            print("Adding " + incoming['data']['Name'] + " to the initiative tracker")
            bulk_initiative_data_form_validate(incoming)
            for i in range(1, incoming['data']['Quantity'] + 1):
                hp = roll_hp(incoming['data']['HD'])
                init = randint(1, 21) + incoming['data']['Init']
                new_entry = InitEntry(name=incoming['data']['Name'] + ' (' + str(i) + ')', initiative=init, ac=incoming['data']['AC'], hp=hp)
                new_entry.save()

        # Update Database entry
        elif incoming['function'] == 'update' and user.is_authenticated:
            print("Updating " + incoming['data']['Name'] + " in the initiative tracker")
            # Checks the database for existance
            to_update = InitEntry.objects.get(name=incoming['data']['Name'])
            if 'AC' in incoming['data'].keys() and isinstance(incoming['data']['AC'], int):
                to_update.ac = incoming['data']['AC']
                to_update.save(update_fields=['ac'])

            if 'HP' in incoming['data'].keys() and isinstance(incoming['data']['HP'], int):
                to_update.hp = incoming['data']['HP']
                to_update.save(update_fields=['hp'])

            if 'Init' in incoming['data'].keys() and isinstance(incoming['data']['Init'], int):
                to_update.initiative = incoming['data']['Init']
                to_update.save(update_fields=['initiative'])

            if 'Conditions' in incoming['data'].keys() and isinstance(incoming['data']['Conditions'], str):
                to_update.conditions = incoming['data']['Conditions']
                to_update.save(update_fields=['conditions'])


        # Remove an entry
        elif incoming['function'] == 'remove' and user.is_authenticated:
            to_delete = InitEntry.objects.filter(name=incoming['data']['Name'])
            print("Deleting ", to_delete[0].name, " from the initiative tracker")
            InitEntry.objects.filter(id=to_delete[0].id).delete()

        # Clear table
        elif incoming['function'] == 'clear' and user.is_authenticated:
            for entry in InitEntry.objects.all():
                InitEntry.objects.filter(id=entry.id).delete()

    # Read from database
    return JsonResponse(format_initiative_tracker(user), safe=False)
