from django.contrib import admin, messages
from .models import InitEntry, ConditionOption


# TODO: Populate Conditions as an admin action
@admin.action(description='Update Conditions from saved JSON')
def hydrate_conditions(modeladmin, request, queryset):
    messages.add_message(request, messages.ERROR, "Action not currently supported.")


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
