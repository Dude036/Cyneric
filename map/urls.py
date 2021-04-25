from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/<str:map_type>', views.map_info, name='map_info'),
    path('person/', views.person_search, name='person_search'),
    path('person/<str:person_name>', views.person_info, name='person'),
    path('crit/', views.crit, name='crit'),
    path('search/', views.town_search, name='town_search'),
    path('<str:town_name>/', views.town_info, name='town'),
]
