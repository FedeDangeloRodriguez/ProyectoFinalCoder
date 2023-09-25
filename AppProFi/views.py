from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout

from .models import Torneo,Equipo,Jugador,Entrenador


# Create your views here.

def inicio(req):
    return render(req,"index.html",{"mensaje":"Bienvenidos a la página del prode!!"})

def torneo(req):

    return render(req,"index.html")

def equipo(req):

    pass

def jugador(req):

    pass

def entrenador(req):

    pass

class TorneoList(ListView):
    model= Torneo
    template_name="torneo_list.html"
    context_object_name="torneos"

class TorneoDetail(DetailView):
    model= Torneo
    template_name="torneo_detalle.html"
    context_object_name="torneo"

class TorneoCreate(CreateView):
    model= Torneo
    template_name="torneo_crear.html"
    fields=('__all__')
    success_url="/app-profi/lista-torneos/"

class TorneoUpdate(UpdateView):
    model= Torneo
    template_name="torneo_actualizar.html"
    fields= ('__all__')
    success_url="/app-profi/lista-torneos/"

class TorneoDelete(DeleteView):
    model= Torneo
    template_name="torneo_eliminar.html"
    success_url = "/app-profi/lista-torneos/"

class EquipoList(ListView):
    model= Equipo
    template_name="equipo_list.html"
    context_object_name="equipos"


class EquipoDetail(DetailView):
    model= Equipo
    template_name="equipo_detalle.html"
    context_object_name="equipo"
    

class EquipoCreate(CreateView):
    model= Equipo
    template_name="equipo_crear.html"
    fields=('__all__')
    success_url="/app-profi/lista-equipos/"

class EquipoUpdate(UpdateView):
    model= Equipo
    template_name="equipo_actualizar.html"
    fields= ('__all__')
    success_url="/app-profi/lista-equipos/"

class EquipoDelete(DeleteView):
    model= Equipo
    template_name="equipo_eliminar.html"
    success_url = "/app-profi/lista-equipos/"

class JugadorList(ListView):
    model= Jugador
    template_name="jugador_list.html"
    context_object_name="jugadores"

class JugadorDetail(DetailView):
    model= Jugador
    template_name="jugador_detalle.html"
    context_object_name="jugador"

class JugadorCreate(CreateView):
    model= Jugador
    template_name="jugador_crear.html"
    fields=('__all__')
    success_url="/app-profi/lista-jugadores/"

class JugadorUpdate(UpdateView):
    model= Jugador
    template_name="jugador_actualizar.html"
    fields= ('__all__')
    success_url="/app-profi/lista-jugadores/"

class JugadorDelete(DeleteView):
    model= Jugador
    template_name="jugador_eliminar.html"
    success_url = "/app-profi/lista-jugadores/"

class EntrenadorList(ListView):
    model= Entrenador
    template_name="entrenador_list.html"
    context_object_name="entrenadores"

class EntrenadorDetail(DetailView):
    model= Entrenador
    template_name="entrenador_detalle.html"
    context_object_name="entrenador"

class EntrenadorCreate(CreateView):
    model= Entrenador
    template_name="entrenador_crear.html"
    fields=('__all__')
    success_url="/app-profi/lista-entrenadores"

class EntrenadorUpdate(UpdateView):
    model= Entrenador
    template_name="entrenador_actualizar.html"
    fields= ('__all__')
    success_url="/app-profi/lista-entrenadores"

class EntrenadorDelete(DeleteView):
    model= Entrenador
    template_name="entrenador_eliminar.html"
    success_url = "/app-profi/lista-entrenadores"

def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(req, "index.html", {"mensaje": "Datos incorrectos"})

        else:
            return render(req, "index.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFomulario": miFormulario})

def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]

            miFormulario.save()

            return render(req, "index.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        else:
            return render(req, "index.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFomulario": miFormulario})
