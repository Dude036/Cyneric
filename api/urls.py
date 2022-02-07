from django.urls import path
from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('npc/', views.npc, name='npc'),
    path('npc/json/', views.npc_json, name='npc_json'),
    path('pc/', views.pc, name='pc'),
    path('pc/json/', views.pc_json, name='pc_json'),
    path('beast/5e/', views.beast_5e, name='beast_5e'),
    path('beast/5e/json/', views.beast_5e_json, name='beast_5e_json'),
    path('beast/pf1/', views.beast_pf1, name='beast_pf1'),
    path('beast/pf1/json/', views.beast_pf1_json, name='beast_pf1_json'),
]
