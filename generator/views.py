from django.http import HttpResponse, Http404
from map.models import GeneratorShop, Town


def generate_town(town_name, settings):
    # Run the rile remotely in a separate instance, and grab the returned HTML?
    return ''


# Create your views here.
def town_gen(request, town_name):
    try:
        town_data = Town.objects.all().filter(name=town_name.title())[0]
        print(town_data.generator_settings)
    except IndexError:
        raise Http404("Unable to find: '" + town_name + "'")
    if town_data.generator_settings is None:
        return Http404("Unable to find generator settings for " + town_name)
    generate_town(town_name, town_data.generator_settings)

    return HttpResponse("This is being tested! Please be patient.")
    # return HttpResponse(generate_town(town_data))


def dummy_town(request):
    try:
        town_data = GeneratorShop.objects.all()[0]
    except IndexError:
        raise Http404("No Default Generator Settings Applied. Please contact the site admin!")
    generate_town('', town_data)

    return HttpResponse("This is being tested! Please be patient.")
    # return HttpResponse(generate_town(town_data))
