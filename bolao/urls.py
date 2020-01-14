from django.urls import path
from . import views

urlpatterns = [
    path('', views.jogos_list, name='jogos_list'),
    path('classificacao/', views.classificacao, name='classificacao'),
    path('rodadas_anteriores/', views.rodadas_anteriores, name='rodadas_anteriores'),
]