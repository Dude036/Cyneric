from django.urls import path

from . import views, init_views, vehicle_views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/<str:map_type>', views.map_info, name='map_info'),
    path('person/', views.person_search, name='person_search'),
    path('person/<str:person_name>', views.person_info, name='person'),
    path('search/', views.town_search, name='town_search'),
    path('admin/', views.admin_redirect, name='admin_redirect'),
    path('phrases/', views.magic_phrases, name='magic_phrases'),
    path('init/', init_views.initiative, name='initiative'),
    path('init/request/', init_views.initiative_request, name='initiative_request'),
    path('schedule/', views.schedule_reroute, name='schedule'),
    path('schedule/delete/<uuid:question_id>/', views.schedule_delete, name='schedule_delete'),
    path('schedule/edit/<uuid:question_id>/<str:submitter>', views.schedule_edit, name='schedule_edit'),
    path('schedule/form/<uuid:question_id>/', views.schedule_form, name='schedule_form'),
    path('schedule/<uuid:question_id>/', views.schedule, name='schedule_specific'),
    path('schedule/create/', views.schedule_create, name='schedule_create'),
    path('schedule/form/success/', views.schedule_success, name='schedule_success'),
    path('cast/', views.cast_list, name='cast_list'),
    path('vehicles/', vehicle_views.vehicles, name='vehicles'),
    path('vehicles/request/', vehicle_views.vehicles_request, name='vehicles_request'),
    path('<str:town_name>/', views.town_info, name='town'),
]
