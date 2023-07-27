from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:team>_player/', views.team_detail),
    path('<str:team>/', views.team_info),
]