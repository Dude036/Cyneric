from django.urls import path
from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('npc/', views.npc, name='npc'),
    path('npc/json/', views.npc_json, name='npc_json'),
    path('pc/', views.pc, name='pc'),
    path('pc/json/', views.pc_json, name='pc_json'),

    path('beast/', views.beast, name='beast'),
    path('beast/json/', views.beast_json, name='beast_json'),
    path('beast/5e/', views.beast_5e, name='beast_5e'),
    path('beast/5e/json/', views.beast_5e_json, name='beast_5e_json'),
    path('beast/pf1/', views.beast_pf1, name='beast_pf1'),
    path('beast/pf1/json/', views.beast_pf1_json, name='beast_pf1_json'),

    path('treasure/pf1/', views.treasure_pf1, name='treasure_pf1'),
    path('treasure/pf1/json/', views.treasure_pf1_json, name='treasure_pf1_json'),
    path('treasure/pf1/<int:cr>/', views.treasure_pf1_cr, name='treasure_pf1'),
    path('treasure/pf1/<int:cr>/json/', views.treasure_pf1_cr_json, name='treasure_pf1_json'),

    path('store/weapon/', views.store_weapon, name='store_weapon'),
    path('store/weapon/json/', views.store_weapon_json, name='store_weapon_json'),
    path('store/armor/', views.store_armor, name='store_armor'),
    path('store/armor/json/', views.store_armor_json, name='store_armor_json'),
    path('store/firearm/', views.store_firearm, name='store_firearm'),
    path('store/firearm/json/', views.store_firearm_json, name='store_firearm_json'),
    path('store/book/', views.store_book, name='store_book'),
    path('store/book/json/', views.store_book_json, name='store_book_json'),
    path('store/enchanter/', views.store_enchanter, name='store_enchanter'),
    path('store/enchanter/json/', views.store_enchanter_json, name='store_enchanter_json'),
    path('store/scroll/', views.store_scroll, name='store_scroll'),
    path('store/scroll/json/', views.store_scroll_json, name='store_scroll_json'),
    path('store/potion/', views.store_potion, name='store_potion'),
    path('store/potion/json/', views.store_potion_json, name='store_potion_json'),
    path('store/jewel/', views.store_jewel, name='store_jewel'),
    path('store/jewel/json/', views.store_jewel_json, name='store_jewel_json'),
    path('store/general/', views.store_general, name='store_general'),
    path('store/general/json/', views.store_general_json, name='store_general_json'),
]