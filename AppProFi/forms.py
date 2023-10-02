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

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):
        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('__all__')


