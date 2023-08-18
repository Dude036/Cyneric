from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/<str:map_type>', views.map_info, name='map_info'),
    path('person/', views.person_search, name='person_search'),
    path('person/<str:person_name>', views.person_info, name='person'),
    path('crit/', views.crit, name='crit'),
    path('crit/form/', views.add_crit, name='add_crit'),
    path('crit/form/success/', views.add_crit_success, name='add_crit_success'),
    path('search/', views.town_search, name='town_search'),
    path('admin/', views.admin_redirect, name='admin_redirect'),
    path('phrases/', views.magic_phrases, name='magic_phrases'),
    path('init/', views.initiative, name='initiative'),
    path('init/request/', views.initiative_request, name='initiative_request'),
    path('schedule/', views.schedule, name='schedule'),
    path('schedule/update/', views.schedule_update, name='schedule_update'),
    path('schedule/create/', views.schedule_create, name='schedule_create'),
    path('schedule/form/', views.schedule_form, name='schedule_form'),
    path('schedule/form/success/', views.schedule_success, name='schedule_success'),
    path('<str:town_name>/', views.town_info, name='town'),
]
