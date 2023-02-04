from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.defaulttags import register
from django.contrib import auth
from .forms import NewsForm
from .models import *

# Helper functions
Holidays = [
    Holiday(Date(15, Month.Apex, 1, Era.First_Age), "Midsummer", "An Elven celebration of their Fey Heritage"),
    Holiday(Date(15, Month.Bottom, 1, Era.First_Age), "Festival of Risiing Spirits", "An Outsiders Celebration of their closeness to the shadow plane"),
    Holiday(Date(26, Month.Roots, 25, Era.Sixth_Age), "Liberation", "The day the 'Converted' were freed from Cithrel's control"),
    Holiday(Date(20, Month.Reap, 1, Era.First_Age), "Reaping", "Harvest Day"),
    Holiday(Date(14, Month.Apex, 1, Era.First_Age), "Sunrise", "Heliod's worship of the summer solstice"),
    Holiday(Date(14, Month.Bottom, 1, Era.First_Age), "Sunset", "Heliod's worship of the winter solstice"),
    Holiday(Date(5, Month.Bloom, 25, Era.Sixth_Age), "Shatter Solstice", "Pale Mistress' worship of seperating the continents"),
    Holiday(Date(10, Month.Ice, 97, Era.Sixth_Age), "Emergence", "The Emergence of the Warforged Army"),
    Holiday(Date(2, Month.Play, 98, Era.Sixth_Age), "Cyneric Remembrance Day", "The destruction of the Cyneric continent and its people"),
]

magic = Holiday(Date(11, Month.Apex , 25, Era.Fourth_Age), "Magic Campaign", "")
cipher = Holiday(Date(16, Month.Play, 98, Era.Sixth_Age), "Cipher Campaign", "")
dragon = Holiday(Date(19, Month.Bloom , 65, Era.Sixth_Age), "Dragon Campaign", "")
calamity = Holiday(Date(16, Month.Birth , 1, Era.Eight_Age), "Calamity Campaign", "")


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


def holiday_css(year, era):
    css = ""
    for holi in Holidays:
        if int(holi.Date.Era) > era:
            print("Skipping " + holi.Name, int(holi.Date.Era), '>', era)
            continue
        elif int(holi.Date.Era) == era and holi.Date.Year >= year:
            print("Skipping " + holi.Name, int(holi.Date.Year), '>', year)
            continue
        css += "#" + str(holi.Date.Month) + str(holi.Date.Day) + " { border-bottom: 4px solid #483D8B; position: relative; border-radius: 10px; }\n"
        css += "#" + str(holi.Date.Month) + str(holi.Date.Day) + "::after { content: \"" + holi.Name + ": " + holi.Description + "\"; width: 100px; top: 0; left: 50%; transform: translate(-50%, calc(-100% - 10px)); padding: 10px 15px; border-radius: 10px; background-color: #483D8B; color: #DCDCDC; display: none; position: absolute; z-index: 999; }\n"
        css += "#" + str(holi.Date.Month) + str(holi.Date.Day) + ":hover::after { display: block;  width: 100px; }\n"
    return css


def now_css(year, era):
    css = ""
    days_colors = ['lavender', 'dodgerblue', 'aquamarine', 'lightgreen',]
    days = [magic, cipher, dragon, calamity]
    for i in range(len(days)):
        if int(days[i].Date.Era) != era or days[i].Date.Year != year:
            print("Skipping " + days[i].Name + ". Era & Year doesn't match")
            continue
        css += "#" + str(days[i].Date.Month) + str(days[i].Date.Day) + " { position: relative; }\n"
        css += "#" + str(days[i].Date.Month) + str(days[i].Date.Day) + "::after { content: \"" + days[i].Name + "\"; width: 100px; top: 0; left: 50%; transform: translate(-50%, calc(-100% - 10px)); padding: 10px 15px; border-radius: 10px; background-color: " + days_colors[i] + "; color: black; display: none; position: absolute; z-index: 999; }\n"
        css += "#" + str(days[i].Date.Month) + str(days[i].Date.Day) + ":hover::after { display: block;  width: 100px; }\n"
    return css


# Views
def calender(request):
    return calender_era(request, calamity.Date.Year, int(calamity.Date.Era))


def calender_year(request, year):
    return calender_era(request, year, int(calamity.Date.Era))


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
        'cipher': cipher.Date.to_dict(),
        'magic': magic.Date.to_dict(),
        'dragon': dragon.Date.to_dict(),
        'calamity': calamity.Date.to_dict(),
        'cipher_year': cipher.Date.Year,
        'magic_year': magic.Date.Year,
        'dragon_year': dragon.Date.Year,
        'calamity_year': calamity.Date.Year,
        'cipher_era': int(cipher.Date.Era),
        'magic_era': int(magic.Date.Era),
        'dragon_era': int(dragon.Date.Era),
        'calamity_era': int(calamity.Date.Era),
        'current_year': year,
        'previous_year': year - 1,
        'next_year': year + 1,
        'era': era,
        'era_name': list(Era)[era],
        'year': months,
        'is_admin': user.is_authenticated,
        'now_css': now_css(year, era),
        'holiday_css': holiday_css(year, era),
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
    article = get_object_or_404(Article, pk=article_id)
    return handle_article_list(request, [article])


def article_day(request, era, year, month, day):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    context = {}
    if isinstance(era, int) and (era <= 0 or era > 12):
        context = {
            'article_list': [{ 'title': 'Date out of Bounds', 'article': "Unable to render due to the follow error: Era out of bounds"}],
            'is_admin': user.is_authenticated,
        }

    elif isinstance(era, str) and era.lower() not in [e.value.lower() for e in list(Era)]:
        print([e.value.lower() for e in list(Era)])
        context = {
            'article_list': [{ 'title': 'Date out of Bounds', 'article': "Unable to render due to the follow error: Era not valid."}],
            'is_admin': user.is_authenticated,
        }

    elif year <= 0 or year > 100:
        context = {
            'article_list': [{ 'title': 'Date out of Bounds', 'article': "Unable to Render due to the follow error: Year out of bounds"}],
            'is_admin': user.is_authenticated,
        }

    elif isinstance(month, int) and (month <= 0 or month > 12):
        context = {
            'article_list': [{ 'title': 'Date out of Bounds', 'article': "Unable to Render due to the follow error: Month out of bounds"}],
            'is_admin': user.is_authenticated,
        }

    elif isinstance(month, str) and month.lower() not in [m.value.lower() for m in list(Month)]:
        print([m.value.lower() for m in list(Month)])
        context = {
            'article_list': [{ 'title': 'Date out of Bounds', 'article': "Unable to Render due to the follow error: Month out of bounds"}],
            'is_admin': user.is_authenticated,
        }

    elif day <= 0 or day > 28:
        context = {
            'article_list': [{ 'title': 'Date out of Bounds', 'article': "Unable to Render due to the follow error: Day out of bounds"}],
            'is_admin': user.is_authenticated,
        }

    else:
        if isinstance(month, int):
            # Subtracting here, since it's 0 indexed
            month_as_enum = list(Month)[month - 1]
        else:
            month_as_enum = Month.from_str(month.title())

        if isinstance(era, int):
            era_as_enum = list(Era)[era]
        else:
            era_as_enum = Era.from_str(era.title())

        all_articles = Article.objects.filter(day=day, year=year, month=month_as_enum, era=era_as_enum)

        # If there are no articles print an error message
        if len(all_articles) > 0:
            return handle_article_list(request, all_articles)
        else:
            context = {
                'article_list': [{ 'title': repr(Date(day, month_as_enum, year, era_as_enum)), 'article': "No news articles for today"}],
                'is_admin': user.is_authenticated,
            }

    return render(request, 'news_list.html', context)


def article_list(request):
    if request.method == 'POST':
        # Receive '[#, #, etc]' or '[#]'
        all_links = request.POST['links'][1:-1]
        print(all_links, type(all_links))
        all_links = [int(s) for s in all_links.strip(',').split(', ') if s.isdigit()]
        print(all_links, type(all_links))

        return handle_article_list(request, [get_object_or_404(Article, pk=article_id) for article_id in all_links])
    else:
        return HttpResponseRedirect('/news/')


def article_latest(request):
    latest = Article.objects.all()[::-1]
    return handle_article_list(request, latest[:5])


def handle_article_list(request, all_articles):
    # Show certain info if the user is authenticated (i.e. logged in as admin)
    user = auth.get_user(request)

    context = {
        'article_list': [{ 'title': article.title, 'article': text_to_html(article.article) } for article in all_articles],
        'is_admin': user.is_authenticated,
    }
    return render(request, 'news_list.html', context)

