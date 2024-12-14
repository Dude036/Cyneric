from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render

from .models import InitEntry
from numpy.random import randint
import re
import simplejson as json


def roll_hp(dice: str):
    if '+' in dice:
        m = re.match(r'(\d+)d(\d+)\s?\+\s?(\d+)', dice)
    elif '-' in dice:
        m = re.match(r'(\d+)d(\d+)(\s?-\s?\d+)', dice)
    else:
        m = re.match(r'(\d+)d(\d+)', dice)
    total = 0
    if m is None:
        return dice
    for _ in range(int(m.group(1))):
        total += randint(int(m.group(2))) + 1
    if len(m.groups()) == 3:
        total += int(''.join(m.group(3).split(' ')))
    return str(total)


def initiative(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    return render(request, 'initiative.html', {'is_admin': user.is_authenticated})


def format_initiative_tracker(user):
    outgoing = []

    for entry in InitEntry.objects.all().order_by('-initiative'):
        data_point = {
            'Name': entry.name,
            'Init': entry.initiative,
            'Conditions': entry.conditions
        }
        if user.is_authenticated:
            data_point['AC'] = entry.ac
            data_point['HP'] = entry.hp
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
                to_update.conditions = incoming['data']['Conditions'].strip()
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

