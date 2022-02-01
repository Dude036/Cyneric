from django.urls import path
from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('npc/', views.npc, name='npc'),
    path('npc/json/', views.npc_json, name='npc_json'),
]
