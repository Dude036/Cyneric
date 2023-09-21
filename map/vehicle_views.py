from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render

from .models import VehicleEntity, VehicleEntry
import simplejson as json


def vehicles(request):
    user = auth.get_user(request)
    return render(request, 'vehicles.html', {'is_admin': user.is_authenticated})


def format_vehicle_data():
    outgoing = {ve.name: [] for ve in list(VehicleEntity)}

    # Populate Items into lists
    for entry in VehicleEntry.objects.all().order_by('modified_on'):
        if not entry.deleted:
            outgoing[str(entry.entity)].append(entry.to_dict())
    return outgoing


def vehicle_form_validate(incoming):
    return True


def vehicles_request(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)
    if request.method == 'POST':
        # Handle POST data
        incoming = json.loads(request.body.decode('utf8'))
        print("New request for Vehicles:", incoming)

        if not vehicle_form_validate(incoming):
            print("Initiative form filled out incorrectly. Ignoring...")
            return JsonResponse(format_vehicle_data(), safe=False)

        # Add to Database
        if incoming['function'] == 'add':
            to_add = VehicleEntry(entity=VehicleEntity.Inventory.name)
            to_add.save()

        # Move Database entry to different vehicle
        elif incoming['function'] == 'move':
            to_move = VehicleEntry.objects.get(id=incoming['data']['id'])
            to_move.entity = incoming['data']['entity']
            to_move.save()

        # Update Database entry
        elif incoming['function'] == 'update':
            to_update = VehicleEntry.objects.get(id=incoming['data']['id'])
            to_update.title = incoming['data']['title']
            to_update.content = incoming['data']['content']
            to_update.save()

        # Remove an entry
        elif incoming['function'] == 'remove':
            to_delete = VehicleEntry.objects.get(id=incoming['data']['id'])
            to_delete.deleted = True
            to_delete.save()

    # Read from database
    return JsonResponse(format_vehicle_data(), safe=False)
