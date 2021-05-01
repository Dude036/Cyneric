from django.contrib import admin
from .models import Town, Person, GeneratorShop, Critical


class TownAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'governing_body')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


class CriticalAdmin(admin.ModelAdmin):
    list_display = ('flavor_text', 'category', 'severity', 'success')


class GeneratorAdmin(admin.ModelAdmin):
    list_display = (
        'race', 'weapon_shop_num', 'armor_shop_num', 'potion_shop_num', 'enchant_shop_num', 'book_shop_num',
        'inn_shop_num', 'jewel_shop_num', 'food_shop_num', 'general_shop_num', 'brothel_shop_num', 'gun_shop_num',
        'variety_shop_num', 'quest_shop_num'
    )


# Register your models here.
admin.site.register(Town, TownAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(GeneratorShop, GeneratorAdmin)
admin.site.register(Critical, CriticalAdmin)
