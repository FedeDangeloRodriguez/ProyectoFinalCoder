from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Torneo)
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Entrenador)