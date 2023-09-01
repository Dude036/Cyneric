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
            outgoing[entry.entity].append(entry.to_dict())
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
        if incoming['function'] == 'add' and user.is_authenticated:
            pass

        # Update Database entry
        elif incoming['function'] == 'update' and user.is_authenticated:
            pass

        # Remove an entry
        elif incoming['function'] == 'remove' and user.is_authenticated:
            pass

        # Clear table
        elif incoming['function'] == 'clear' and user.is_authenticated:
            pass

    # Read from database
    return JsonResponse(format_vehicle_data(), safe=False)
