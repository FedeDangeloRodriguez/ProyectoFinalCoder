from django.urls import path

from .views import *

urlpatterns = [
    path('torneos/', torneo, name= "Torneo" ),
    path('equipos/', equipo, name= "Equipo" ),
    path('jugadores/', jugador, name= "Jugador" ),
    path('entrenadores/', entrenador, name= "Entrenador" ),
    path('lista-torneos/', TorneoList.as_view(), name= "ListaTorneos" ),
    path('detalle-torneo/<pk>', TorneoDetail.as_view(), name= "DetalleTorneo" ),
    path('crear-torneo/', TorneoCreate.as_view(), name= "CrearTorneo" ),
    path('actualizar-torneo/<pk>', TorneoUpdate.as_view(), name= "ActualizarTorneo" ),
    path('eliminar-torneo/<pk>', TorneoDelete.as_view(), name= "EliminarTorneo" ),
    path('lista-equipos/', EquipoList.as_view(), name= "ListaEquipos" ),
    path('detalle-equipo/<pk>', EquipoDetail.as_view(), name= "DetalleEquipo" ),
    path('crear-equipo/', EquipoCreate.as_view(), name= "CrearEquipo" ),
    path('actualizar-equipo/<pk>', EquipoUpdate.as_view(), name= "ActualizarEquipo" ),
    path('eliminar-equipo/<pk>', EquipoDelete.as_view(), name= "EliminarEquipo" ),
    path('lista-jugadores/', JugadorList.as_view(), name= "ListaJugadores" ),
    path('detalle-jugador/<pk>', JugadorDetail.as_view(), name= "DetalleJugador" ),
    path('crear-jugador/', JugadorCreate.as_view(), name= "CrearJugador" ),
    path('actualizar-jugador/<pk>', JugadorUpdate.as_view(), name= "ActualizarJugador"),
    path('eliminar-jugador/<pk>', JugadorDelete.as_view(), name= "EliminarJugador" ),
    path('lista-entrenadores/', EntrenadorList.as_view(), name= "ListaEntrenadores" ),
    path('detalle-entrenador/<pk>', EntrenadorDetail.as_view(), name= "DetalleEntrenador" ),
    path('crear-entrenador/', EntrenadorCreate.as_view(), name= "CrearEntrenador" ),
    path('actualizar-entrenador/<pk>', EntrenadorUpdate.as_view(), name= "ActualizarEntrenador" ),
    path('eliminar-entrenador/<pk>', EntrenadorDelete.as_view(), name= "EliminarEntrenador" ),
]
