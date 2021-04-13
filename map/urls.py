from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/<str:map_type>', views.map, name='map'),
    path('<str:town_name>/', views.town_info, name='town'),
    # path('person/<str:person_name>', views.person_info, name='town'),
]