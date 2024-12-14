import os
import simplejson as json
from django.contrib import admin, messages
from .models import InitEntry, ConditionOption


# TODO: Add the rest of the conditions to the JSON file
@admin.action(description='Update Conditions from saved JSON')
def hydrate_conditions(modeladmin, request, queryset):
    conditions = []
    with open(os.path.join(os.getcwd(), 'initiative', 'conditions.json'), 'r') as conditions_file:
        conditions = json.load(conditions_file)

    if not conditions:
        messages.add_message(request, messages.ERROR, 'No conditions found.')

    for condition in conditions:
        new_cond, _ = ConditionOption.objects.get_or_create(**condition)
        new_cond.save()

    messages.add_message(request, messages.SUCCESS, "Rehydrated Condition Options list.")


class InitiativeAdmin(admin.ModelAdmin):
    model=InitEntry
    list_display = ('id', 'name', 'initiative')
    ordering = ['name']


class ConditionOptionAdmin(admin.ModelAdmin):
    model=ConditionOption
    list_display = ('id', 'name')
    ordering = ['id']
    actions = [hydrate_conditions]


# Register your models here.
admin.site.register(InitEntry, InitiativeAdmin)
admin.site.register(ConditionOption, ConditionOptionAdmin)
