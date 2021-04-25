from django.urls import path
from . import views

urlpatterns = [
    path('<str:town_name>/', views.town_gen, name='town'),
    path('', views.dummy_town, name='dummy'),
]
