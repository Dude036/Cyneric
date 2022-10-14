from django.urls import path
from . import views
from . import item_views
from . import store_views

urlpatterns = [
    path('', views.api, name='api'),

    # Player Data
    path('npc/', views.npc, name='npc'),
    path('npc/json/', views.npc_json, name='npc_json'),
    path('pc/', views.pc, name='pc'),
    path('pc/json/', views.pc_json, name='pc_json'),

    # Beastiary
    path('beast/', views.beast, name='beast'),
    path('beast/json/', views.beast_json, name='beast_json'),
    path('beast/5e/', views.beast_5e, name='beast_5e'),
    path('beast/5e/json/', views.beast_5e_json, name='beast_5e_json'),
    path('beast/pf1/', views.beast_pf1, name='beast_pf1'),
    path('beast/pf1/json/', views.beast_pf1_json, name='beast_pf1_json'),

    # Loot
    path('treasure/pf1/', views.treasure_pf1, name='treasure_pf1'),
    path('treasure/pf1/json/', views.treasure_pf1_json, name='treasure_pf1_json'),
    path('treasure/pf1/<int:cr>/', views.treasure_pf1_cr, name='treasure_pf1'),
    path('treasure/pf1/<int:cr>/json/', views.treasure_pf1_cr_json, name='treasure_pf1_json'),

    # Store Content
    path('store/weapon/', store_views.store_weapon, name='store_weapon'),
    path('store/weapon/json/', store_views.store_weapon_json, name='store_weapon_json'),
    path('store/armor/', store_views.store_armor, name='store_armor'),
    path('store/armor/json/', store_views.store_armor_json, name='store_armor_json'),
    path('store/firearm/', store_views.store_firearm, name='store_firearm'),
    path('store/firearm/json/', store_views.store_firearm_json, name='store_firearm_json'),
    path('store/book/', store_views.store_book, name='store_book'),
    path('store/book/json/', store_views.store_book_json, name='store_book_json'),
    path('store/enchanter/', store_views.store_enchanter, name='store_enchanter'),
    path('store/enchanter/json/', store_views.store_enchanter_json, name='store_enchanter_json'),
    path('store/scroll/', store_views.store_scroll, name='store_scroll'),
    path('store/scroll/json/', store_views.store_scroll_json, name='store_scroll_json'),
    path('store/potion/', store_views.store_potion, name='store_potion'),
    path('store/potion/json/', store_views.store_potion_json, name='store_potion_json'),
    path('store/jewel/', store_views.store_jewel, name='store_jewel'),
    path('store/jewel/json/', store_views.store_jewel_json, name='store_jewel_json'),
    path('store/general/', store_views.store_general, name='store_general'),
    path('store/general/json/', store_views.store_general_json, name='store_general_json'),
    path('store/food/', store_views.store_food, name='store_food'),
    path('store/food/json/', store_views.store_food_json, name='store_food_json'),
    path('store/inn/', store_views.store_inn, name='store_inn'),
    path('store/inn/json/', store_views.store_inn_json, name='store_inn_json'),
    path('store/variety/', store_views.store_variety, name='store_variety'),
    path('store/variety/json/', store_views.store_variety_json, name='store_variety_json'),

    # Randomly Generated Content
    path('item/weapon/', item_views.item_weapon, name='item_weapon'),
    path('item/weapon/json/', item_views.item_weapon_json, name='item_weapon_json'),
    path('item/weapon/<int:r>/', item_views.item_weapon_r, name='item_weapon_r'),
    path('item/weapon/<int:r>/json/', item_views.item_weapon_r_json, name='item_weapon_r_json'),
    path('item/armor/', item_views.item_armor, name='item_armor'),
    path('item/armor/json/', item_views.item_armor_json, name='item_armor_json'),
    path('item/armor/<int:r>/', item_views.item_armor_r, name='item_armor_r'),
    path('item/armor/<int:r>/json/', item_views.item_armor_r_json, name='item_armor_r_json'),
    path('item/firearm/', item_views.item_firearm, name='item_firearm'),
    path('item/firearm/json/', item_views.item_firearm_json, name='item_firearm_json'),
    path('item/firearm/<int:r>/', item_views.item_firearm_r, name='item_firearm_r'),
    path('item/firearm/<int:r>/json/', item_views.item_firearm_r_json, name='item_firearm_r_json'),
    path('item/scroll/', item_views.item_scroll, name='item_scroll'),
    path('item/scroll/json/', item_views.item_scroll_json, name='item_scroll_json'),
    path('item/scroll/<int:r>/', item_views.item_scroll_r, name='item_scroll_r'),
    path('item/scroll/<int:r>/json/', item_views.item_scroll_r_json, name='item_scroll_r_json'),
    path('item/potion/', item_views.item_potion, name='item_potion'),
    path('item/potion/json/', item_views.item_potion_json, name='item_potion_json'),
    path('item/potion/<int:r>/', item_views.item_potion_r, name='item_potion_r'),
    path('item/potion/<int:r>/json/', item_views.item_potion_r_json, name='item_potion_r_json'),
    path('item/book/', item_views.item_book, name='item_book'),
    path('item/book/json/', item_views.item_book_json, name='item_book_json'),
    path('item/food/', item_views.item_food, name='item_food'),
    path('item/food/json/', item_views.item_food_json, name='item_food_json'),
    path('item/trinket/', item_views.item_trinket, name='item_trinket'),
    path('item/trinket/json/', item_views.item_trinket_json, name='item_trinket_json'),

    # Existing Item Content
    path('item/existing/<str:item>/', views.existing_item, name='existing_item'),
    path('item/existing/<str:item>/json/', views.existing_item_json, name='existing_item_json'),
    # Setup API client to https://api.pathfinder2.fr/doc
]
