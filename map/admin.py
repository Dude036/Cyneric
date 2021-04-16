from django.contrib import admin
from .models import Town, Person, GeneratorShop


class TownAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'governing_body')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


# Register your models here.
admin.site.register(Town, TownAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(GeneratorShop)

