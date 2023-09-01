from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Town, Person, Critical, Schedule, Choice, VehicleEntry
from .forms import CritForm, ChoiceForm, ScheduleForm
from django.contrib import auth
import simplejson as json


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

def schedule(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    try:
        most_recent_poll = Schedule.objects.order_by("-pub_date")[0]
    except IndexError:
        most_recent_poll = None

    if most_recent_poll is None:
        return HttpResponse('No polls currently available')

    context = {'is_admin': user.is_authenticated}
    date_options = most_recent_poll.date_options

    context['question'] = most_recent_poll.question_text

    calendar = [['Submitter', ], ]
    for op in date_options:
        calendar[0].append(op)

    submissions = Choice.objects.filter(question=most_recent_poll.id)

    for sub in submissions:
        row = [sub.submitter, ]
        for date in date_options:
            row.append(sub.available_dates[date])
        calendar.append(row)

    print(calendar)
    context['calendar'] = calendar

    return render(request, 'schedule.html', context)


def schedule_update(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    try:
        most_recent_poll = Schedule.objects.order_by("-pub_date")[0]
    except IndexError:
        most_recent_poll = None

    if most_recent_poll is None:
        return HttpResponse("You must have a Schedule created before you can query for responses")

    if request.method == 'POST':
        if user.is_authenticated:
            incoming = json.loads(request.body.decode('utf8'))
            if 'DELETE' == incoming['action']:
                entry = Choice.objects.get(question=most_recent_poll, submitter=incoming['name'])
                entry.delete()
    else:
        return HttpResponseRedirect('/schedule/')

    response = {}

    return JsonResponse(response)


def schedule_form(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)
    try:
        most_recent_poll = Schedule.objects.order_by("-pub_date")[0]
    except IndexError:
        most_recent_poll = None

    if most_recent_poll is None:
        return HttpResponse("You must have a Schedule created before you can query for responses")

    if request.method == 'POST':
        # Parse available dates here
        available = {}
        for date in most_recent_poll.date_options:
            available[date] = request.POST[date]

        form = ChoiceForm(question_id=most_recent_poll.id, available_dates=available, submitter=request.POST['submitter'])

        # check whether it's valid:
        if form.is_valid():
            new_entry = Choice(question=most_recent_poll, available_dates=available, submitter=form.submitter)

            new_entry.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/schedule/form/success/')
        else:
            return HttpResponse('The content was malformed, and unable to be processed. Please verify your submission is valid, and try again.')

    context = {
        'question_text': most_recent_poll.question_text,
        'dates': most_recent_poll.date_options,
        'is_admin': user.is_authenticated
    }

    return render(request, 'schedule_add.html', context)


def schedule_success(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    return render(request, 'schedule_add_success.html', {'is_admin': user.is_authenticated})


def schedule_create(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)
    try:
        most_recent_poll = Schedule.objects.order_by("-pub_date")[0]
    except IndexError:
        most_recent_poll = None

    if most_recent_poll is None:
        return HttpResponse("You must have a Schedule created before you can query for responses")

    if request.method == 'POST':
        print(request.POST)

        # Parse available dates here
        dates = []
        for key, value in request.POST.items():
            if key.startswith('option_'):
                dates.append(value)

        form = ScheduleForm(question_text=request.POST['question'], date_options=dates)

        # check whether it's valid:
        if form.is_valid():
            new_entry = Schedule(question_text=form.question_text, date_options=form.date_options)

            new_entry.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/schedule/form/success/')
        else:
            return HttpResponse('The content was malformed, and unable to be processed. Please verify your submission is valid, and try again.')

    return render(request, 'schedule_create.html', {'is_admin': user.is_authenticated})


def cast_list(request):
    user = auth.get_user(request)
    return render(request, 'cast.html', {'is_admin': user.is_authenticated})
