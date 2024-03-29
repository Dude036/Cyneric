from django.urls import path

from . import views

urlpatterns = [
    path('', views.calender, name='calender'),
    path('<int:year>/', views.calender_year, name='calender_year'),
    path('<int:era>/<int:year>/', views.calender_era, name='calender_era'),
    path('<int:era>/<int:year>/<int:month>/<int:day>', views.article_day, name='article_day'),
    path('<int:era>/<int:year>/<str:month>/<int:day>', views.article_day, name='article_day'),
    path('<str:era>/<int:year>/<int:month>/<int:day>', views.article_day, name='article_day'),
    path('<str:era>/<int:year>/<str:month>/<int:day>', views.article_day, name='article_day'),
    path('add/', views.create_article, name='create_article'),
    path('add/success/', views.article_success, name='article_success'),
    path('latest/', views.article_latest, name='article_latest'),
    path('article/list', views.article_list, name='article_list'),
    path('article/<int:article_id>', views.article, name='article'),
]
