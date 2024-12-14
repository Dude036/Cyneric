from django.contrib import admin
from .models import Schedule, Choice, VehicleEntry


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'submitter')


class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity', 'title', 'modified_on', 'deleted')


# Register your models here.
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(VehicleEntry, VehiclesAdmin)
