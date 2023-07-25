from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:player>/', views.team_detail),
]