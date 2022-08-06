from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor, name='editor'),
    path('parser/', views.parser, name='parser'),
    path('admin/', views.admin_view, name='admin_view'),
    path('admin/<int:action>', views.admin_action, name='admin_action'),
]
