from django.shortcuts import render
from django.http import HttpResponse
from map.models import GeneratorShop


# Create your views here.
def town_gen(request, town_name):
    all_settings = GeneratorShop.objects.all()
    print(all_settings)

    return HttpResponse("This is being tested! Please be patient.")


def dummy_town(request):
    context = {}

    return render(request, 'index.html', context)

