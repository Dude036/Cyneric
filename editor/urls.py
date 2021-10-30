from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor, name='editor'),
    path('parser/', views.parser, name='parser'),
]
