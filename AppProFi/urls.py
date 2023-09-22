from django.urls import path

from .views import *

urlpatterns = [
    path('torneos/', torneo, name= "Torneo" ),
    path('equipos/', equipo, name= "Equipo" ),
    path('jugadores/', jugador, name= "Jugador" ),
    path('entrenadores/', entrenador, name= "Entrenador" ),
]