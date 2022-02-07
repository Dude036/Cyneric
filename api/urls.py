from django.urls import path
from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('npc/', views.npc, name='npc'),
    path('npc/json/', views.npc_json, name='npc_json'),
    path('pc/', views.pc, name='pc'),
    path('pc/json/', views.pc_json, name='pc_json'),
    path('beast/5e/', views.beast, name='beast'),
    path('beast/5e/json/', views.beast_json, name='beast_json'),
]
