from django.contrib import admin
from .models import InitEntry, ConditionOption


class InitiativeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'initiative')


class ConditionOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# Register your models here.
admin.site.register(InitEntry, InitiativeAdmin)
admin.site.register(ConditionOption, ConditionOptionAdmin)
