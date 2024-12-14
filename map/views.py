from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Schedule, Choice
from .forms import ChoiceForm, ScheduleForm
from django.contrib import auth
import simplejson as json


# Create your views here.
def index(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    context = {
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


def admin_redirect(request):
    return HttpResponseRedirect('/admin/')


def magic_phrases(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    return render(request, 'phrases.html', {'is_admin': user.is_authenticated})


def schedule_reroute(request):
    try:
        most_recent_poll = Schedule.objects.order_by("-pub_date")[0]
        return HttpResponseRedirect('/schedule/' + str(most_recent_poll.id) + '/')
    except IndexError:
        return HttpResponseRedirect('/schedule/create/')


def schedule(request, question_id):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    if question_id is not None:
        try:
            recent_poll = Schedule.objects.get(id=question_id)
        except ObjectDoesNotExist:
            print("Question '" + question_id + "' not found, Printing failure message")

    if recent_poll is None:
        return Http404('Invalid Pill ID')

    context = {'is_admin': user.is_authenticated}
    date_options = recent_poll.date_options

    context['question'] = recent_poll.question_text

    calendar = [['Submitter', ], ]
    for op in date_options:
        calendar[0].append(op)

    submissions = Choice.objects.filter(question=recent_poll.id)

    for sub in submissions:
        row = [sub.submitter, ]
        for date in date_options:
            row.append(sub.available_dates[date])
        calendar.append(row)

    context['calendar'] = calendar
    context['question_id'] = recent_poll.id

    open_polls = {}
    for poll in Schedule.objects.order_by("-pub_date"):
        if not poll.closed:
            open_polls[str(poll.id)] = poll.question_text
    context['poll_list'] = open_polls

    return render(request, 'schedule.html', context)


def schedule_delete(request, question_id):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    try:
        recent_poll = Schedule.objects.get(id=question_id)
    except IndexError:
        recent_poll = None

    if recent_poll is None:
        return HttpResponse("You must have a Schedule created before you can query for responses")

    if request.method == 'POST':
        if user.is_authenticated:
            incoming = json.loads(request.body.decode('utf8'))
            if 'DELETE' == incoming['action']:
                entry = Choice.objects.get(question=recent_poll, submitter=incoming['name'])
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
        recent_poll = Schedule.objects.get(id=question_id)
    except ObjectDoesNotExist as e:
        return HttpResponseRedirect('/schedule/')

    # Check user exists for poll
    try:
        choice = Choice.objects.get(question=recent_poll.id, submitter=submitter)
    except ObjectDoesNotExist as e:
        return HttpResponseRedirect('/schedule/')

    # Redirect with
    context = {
        'question_text': recent_poll.question_text,
        'poll_id': recent_poll.id,
        'dates': recent_poll.date_options,
        'options': json.dumps(choice.available_dates),
        'is_admin': user.is_authenticated
    }

    return render(request, 'schedule_add.html', context)


def schedule_form(request, question_id):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)
    try:
        recent_poll = Schedule.objects.get(id=question_id)
    except IndexError:
        recent_poll = None

    if recent_poll is None:
        return HttpResponse("You must have a Schedule created before you can query for responses")

    if request.method == 'POST':
        # Parse available dates here
        available = {}
        for date in recent_poll.date_options:
            available[date] = request.POST[date]

        form = ChoiceForm(question_id=recent_poll.id, available_dates=available, submitter=request.POST['submitter'])

        # check whether it's valid:
        if form.is_valid():
            new_entry, created = Choice.objects.get_or_create(question=recent_poll, submitter=form.submitter)
            new_entry.available_dates = available

            new_entry.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/schedule/form/success/')
        else:
            return HttpResponse('The content was malformed, and unable to be processed. Please verify your submission is valid, and try again.')

    context = {
        'question_text': recent_poll.question_text,
        'poll_id': recent_poll.id,
        'dates': recent_poll.date_options,
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

    # Create Schedule Form
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

    # Get form to fill out
    else:
        return render(request, 'schedule_create.html', {'is_admin': user.is_authenticated})


def cast_list(request):
    user = auth.get_user(request)
    return render(request, 'cast.html', {'is_admin': user.is_authenticated})
