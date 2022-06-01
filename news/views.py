from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.defaulttags import register
from django.contrib import auth
from .forms import NewsForm
from .models import Article, Month, Era

# Create your views here.
def today():
    return {
        "Era": Era.Sixth_Age,
        "Year": 98,
        "Day": 7,
        "Month": Month.Fruiting
    }


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



def calender(request):
    return calender_era(request, today()['Year'], list(Era).index(today()['Era']))


def calender_year(request, year):
    return calender_era(request, year, list(Era).index(today()['Era']))


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
        'today': today(),
        'current_year': year,
        'previous_year': year - 1,
        'next_year': year + 1,
        'era': era,
        'era_name': list(Era)[era],
        'year': months,
        'is_admin': user.is_authenticated,
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
        'is_admin': user.is_authenticated,
        'id': article_id,
        'title': article.title,
        'article': article.article,
    }
    return render(request, 'news_article.html', context)


def article_list(request):
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
            }

            return render(request, 'news_list.html', context)
    else:
        return  HttpResponseRedirect('/news/')


def article_latest(request):
    latest = Article.objects.all()[::-1]
    return render(request, 'news_list.html', { 'article_list': [{ 'title': article.title, 'article': article.article } for article in latest[:5]]})
