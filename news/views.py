from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.defaulttags import register
from django.contrib import auth
from .forms import NewsForm
from .models import *

# Helper functions
Holidays = [
    Holiday(Date(15, Month.Fruiting, 1, Era.First_Age), "Midsummer", "An Elven celebration of their Fey Heritage"),
]

today = Date(1, Month.Play, 98, Era.Sixth_Age)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def is_int(thing):
    return isinstance(thing, int)


def calender_enumeration(name):
    month = {}
    month['name'] = name
    month['days'] = []
    for week in range(4):
        new_week = []
        for day in range(7):
            new_week.append(1 + day + week * 7)
        month['days'].append(new_week)
    return month


def add_day(article, month):
    day = article.day
    week = (day - 1) // 7
    i = day - 1 - (week * 7)
    if isinstance(month['days'][week][i], int):
        month['days'][week][i] = {
            "link": '',
            "links": [article.id],
            "number": day,
        }
    else:
        month['days'][week][i]['links'].append(article.id)


def text_to_html(text):
    # Swap out newlines with paragraph tags
    text = '<p>' + text.replace('\n', '</p><p>') + '</p>'
    return text


def holiday_css():
    css = ""
    for holi in Holidays:
        css += "#" + str(holi.Date.Month) + str(holi.Date.Day) + " { border-bottom: 4px solid #483D8B; position: relative; border-radius: 10px; }\n"
        css += "#" + str(holi.Date.Month) + str(holi.Date.Day) + "::after { content: \"" + holi.Name + ": " + holi.Description + "\"; top: 0; left: 50%; transform: translate(-50%, calc(-100% - 10px)); padding: 10px 15px; border-radius: 10px; background-color: #483D8B; color: #DCDCDC; display: none; position: absolute; z-index: 999; }\n"
        css += "#" + str(holi.Date.Month) + str(holi.Date.Day) + ":hover::after { display: block; }\n"
    return css


# Views
def calender(request):
    return calender_era(request, today.Year, int(today.Era))


def calender_year(request, year):
    return calender_era(request, year, int(today.Era))


def calender_era(request, year, era):
    if year > 100:
        year -= 100
        era += 1
        HttpResponseRedirect('news/' + str(year) + '/' + str(era))
    elif year <= 0:
        year += 100
        era -= 1
        HttpResponseRedirect('news/' + str(year) + '/' + str(era))

    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    months = []

    for m in Month:
        current = calender_enumeration(m)
        current_articles = Article.objects.all().filter(month=m, year=year, era=list(Era)[era])
        for article in current_articles:
            add_day(article, current)

        months.append(current)

    context = {
        'today': today.to_dict(),
        'current_year': year,
        'previous_year': year - 1,
        'next_year': year + 1,
        'era': era,
        'era_name': list(Era)[era],
        'year': months,
        'is_admin': user.is_authenticated,
        'holiday_css': holiday_css(),
    }
    return render(request, 'news.html', context)


def create_article(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    if request.method == 'POST':
        # Handle incoming request
        form = NewsForm(request.POST)
        if form.is_valid():
            new_article = Article(
                title=form.data['title'],
                article=form.data['article'],
                day=form.data['day'],
                month=form.data['month'],
                year=form.data['year'],
                era=form.data['era'],
            )
            new_article.save()
            return HttpResponseRedirect('/news/add/success/')
        else:
            return HttpResponse('The content was malformed, and unable to be processed. Please verify your submission is valid, and try again.')
    else:
        context = {
            'is_admin': user.is_authenticated,
            'form': NewsForm
        }
        return render(request, 'news_add.html', context)


def article_success(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    return render(request, 'news_add_success.html', {'is_admin': user.is_authenticated})


def article(request, article_id):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    article = get_object_or_404(Article, pk=article_id)

    context = {
        'article_list': [{ 'is_admin': user.is_authenticated, 'title': article.title, 'article': text_to_html(article.article) }]
    }
    return render(request, 'news_list.html', context)


def article_list(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    if request.method == 'POST':
        # Receive '[#, #, etc]' or '[#]'
        all_links = request.POST['links'][1:-1]
        print(all_links, type(all_links))
        all_links = [int(s) for s in all_links.strip(',').split(', ') if s.isdigit()]
        print(all_links, type(all_links))

        # Only one Link
        if len(all_links) == 1:
            return article(request, all_links[0])
        else:
            all_articles = [get_object_or_404(Article, pk=article_id) for article_id in all_links]
            context = {
                'article_list': [{ 'title': article.title, 'article': article.article } for article in all_articles],
                'is_admin': user.is_authenticated,
            }

            return render(request, 'news_list.html', context)
    else:
        return  HttpResponseRedirect('/news/')


def article_latest(request):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    latest = Article.objects.all()[::-1]
    context = {
        'is_admin': user.is_authenticated,
        'article_list': [{ 'title': article.title, 'article': article.article } for article in latest[:5]]
    }
    return render(request, 'news_list.html', context)