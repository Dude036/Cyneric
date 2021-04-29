from django.contrib import admin
from .models import Town, Person, GeneratorShop, Critical


class TownAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'governing_body')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


class CriticalAdmin(admin.ModelAdmin):
    list_display = ('flavor_text', 'category', 'severity', 'success')


# Register your models here.
admin.site.register(Town, TownAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(GeneratorShop)
admin.site.register(Critical, CriticalAdmin)
