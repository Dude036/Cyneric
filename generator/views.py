from django.http import HttpResponse, Http404
from generator.DMToolkit.core import town_generator, variance
from map.models import GeneratorShop, Town


def generate_town(town_name, settings):
    # Run the rile remotely in a separate instance, and grab the returned HTML?
    variance.custom_settings(settings.race, settings.population, settings.variance, settings.exotic)
    Weapons = [
        settings.weapon_shop_num, settings.weapon_shop_rlo,
        settings.weapon_shop_rhi, settings.weapon_shop_qlo,
        settings.weapon_shop_qhi, settings.weapon_shop_add,
        settings.weapon_shop_inf
    ]
    Armor = [
        settings.armor_shop_num, settings.armor_shop_rlo,
        settings.armor_shop_rhi, settings.armor_shop_qlo,
        settings.armor_shop_qhi, settings.armor_shop_add,
        settings.armor_shop_inf
    ]
    Potion = [
        settings.potion_shop_num, settings.potion_shop_rlo,
        settings.potion_shop_rhi, settings.potion_shop_qlo,
        settings.potion_shop_qhi, settings.potion_shop_inf
    ]
    Enchant = [
        settings.enchant_shop_num, settings.enchant_shop_rlo,
        settings.enchant_shop_rhi, settings.enchant_shop_qlo,
        settings.enchant_shop_qhi, settings.enchant_shop_inf
    ]
    Enchanter = [
        settings.enchanter_shop_num, settings.enchanter_shop_rlo,
        settings.enchanter_shop_rhi, settings.enchanter_shop_qlo,
        settings.enchanter_shop_qhi, settings.enchanter_shop_inf
    ]
    Books = [
        settings.book_shop_num, settings.book_shop_qlo,
        settings.book_shop_qhi, settings.book_shop_inf
    ]
    Tavern = [
        settings.inn_shop_num, settings.inn_shop_rms,
        settings.inn_shop_qlo, settings.inn_shop_qhi,
        settings.inn_shop_inf
    ]
    Jewel = [
        settings.jewel_shop_num, settings.jewel_shop_rlo,
        settings.jewel_shop_rhi, settings.jewel_shop_qlo,
        settings.jewel_shop_qhi, settings.jewel_shop_inf
    ]
    Food = [
        settings.food_shop_num, settings.food_shop_qlo,
        settings.food_shop_qhi, settings.food_shop_inf
    ]
    General = [
        settings.general_shop_num, settings.general_shop_rlo,
        settings.general_shop_rhi, settings.general_shop_qlo,
        settings.general_shop_qhi, settings.general_shop_trk,
        settings.general_shop_inf
    ]
    Brothel = [
        settings.brothel_shop_num, settings.brothel_shop_qlo,
        settings.brothel_shop_qhi, settings.brothel_shop_inf
    ]
    Gunsmith = [
        settings.gun_shop_num, settings.gun_shop_rlo,
        settings.gun_shop_rhi, settings.gun_shop_qlo,
        settings.gun_shop_qhi, settings.gun_shop_add,
        settings.gun_shop_inf
    ]
    Variety = [
        settings.variety_shop_num, settings.variety_shop_qlo,
        settings.variety_shop_qhi, settings.variety_shop_inf
    ]
    Quests = [
        settings.quest_shop_num, settings.quest_shop_llo,
        settings.quest_shop_lhi, settings.quest_shop_inf
    ]

    town_name = town_generator.generate_shops(Weapons, Armor, Potion, Enchant, Enchanter, Books, Tavern, Jewel, Food,
                                              General, Brothel, Gunsmith, Variety, Quests, town_name, False)
    html = town_generator.generate_people([], [], town_name, False, False)
    return html


# Create your views here.
def town_gen(request, town_name):
    try:
        town_data = Town.objects.all().filter(name=town_name.title())[0]
    except IndexError:
        raise Http404("Unable to find: '" + town_name + "'")
    if town_data.generator_settings is None:
        return Http404("Unable to find generator settings for " + town_name)

    # return HttpResponse("This is being tested! Please be patient.")
    return HttpResponse(generate_town(town_name, town_data.generator_settings))


def dummy_town(request):
    try:
        town_data = GeneratorShop.objects.all()[0]
    except IndexError:
        raise Http404("No Default Generator Settings Applied. Please contact the site admin!")

    # return HttpResponse("This is being tested! Please be patient.")
    return HttpResponse(generate_town('', town_data))
