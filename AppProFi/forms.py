from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import *

class TorneoFormulario(forms.ModelForm):

    class Meta:
        model= Torneo
        fields= ('__all__')

class Equipo(forms.ModelForm):

    class Meta:
        model= Equipo
        fields= ('__all__')

class JugadorFormulario(forms.ModelForm):

    class Meta:
        model= Jugador
        fields= ('__all__')

class EntrenadorFormulario(forms.ModelForm):

    class Meta:
        model= Entrenador
        fields= ('__all__')