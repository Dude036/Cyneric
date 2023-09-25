from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Town, Person, Schedule, Choice
from .forms import ChoiceForm, ScheduleForm
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


def admin_redirect(request):
    return HttpResponseRedirect('/admin/')


def magic_phrases(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    return render(request, 'phrases.html', {'is_admin': user.is_authenticated})


def schedule(request, question_id=None):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    try:
        most_recent_poll = Schedule.objects.order_by("-pub_date")[0]
    except IndexError:
        most_recent_poll = None

    if question_id is not None:
        try:
            most_recent_poll = Schedule.objects.get(id=question_id)
        except ObjectDoesNotExist:
            print("Question '" + question_id + "' not found. Defaulting")

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

    context['calendar'] = calendar
    context['question_id'] = most_recent_poll.id

    open_polls = {}
    for poll in Schedule.objects.order_by("-pub_date"):
        if not poll.closed:
            open_polls[str(poll.id)] = poll.question_text
    context['poll_list'] = open_polls

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


def schedule_edit(request, question_id, submitter):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    # Check poll exists
    try:
        most_recent_poll = Schedule.objects.get(id=question_id)
    except ObjectDoesNotExist as e:
        return HttpResponseRedirect('/schedule/')

    # Check user exists for poll
    try:
        choice = Choice.objects.get(question=most_recent_poll.id, submitter=submitter)
    except ObjectDoesNotExist as e:
        return HttpResponseRedirect('/schedule/')

    # Redirect with

    context = {
        'question_text': most_recent_poll.question_text,
        'dates': most_recent_poll.date_options,
        'options': json.dumps(choice.available_dates),
        'is_admin': user.is_authenticated
    }

    return render(request, 'schedule_add.html', context)


def schedule_form(request, question_id):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)
    try:
        most_recent_poll = Schedule.objects.get(id=question_id)
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
            new_entry, created = Choice.objects.get_or_create(question=most_recent_poll, submitter=form.submitter)
            new_entry.available_dates = available

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
