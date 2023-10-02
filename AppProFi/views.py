from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from .models import Torneo, Equipo, Jugador, Entrenador, Avatar
from .forms import  UserEditForm


# Create your views here.

def inicio(req):
    return render(req,"index.html",{"mensaje":"Bienvenido a InfoTorneos"})

def about(req):

    return render(req,"about.html")


class TorneoList(ListView):
    paginate_by= 3
    model= Torneo
    template_name="torneo_list.html"
    context_object_name="torneos"

class TorneoDetail(DetailView):
    model= Torneo
    template_name="torneo_detalle.html"
    context_object_name="torneo"

@method_decorator(staff_member_required, name='dispatch')
class TorneoCreate(CreateView):
    model= Torneo
    template_name="torneo_crear.html"
    fields=('__all__')
    success_url="/app-profi/lista-torneos/"

@method_decorator(staff_member_required, name='dispatch')
class TorneoUpdate(UpdateView):
    model= Torneo
    template_name="torneo_actualizar.html"
    fields= ('__all__')
    success_url="/app-profi/lista-torneos/"

@method_decorator(staff_member_required, name='dispatch')
class TorneoDelete(DeleteView):
    model= Torneo
    template_name="torneo_eliminar.html"
    success_url= "/app-profi/lista-torneos/"

class EquipoList(ListView):
    model= Equipo
    template_name="equipo_list.html"
    context_object_name="equipos"


class EquipoDetail(DetailView):
    model= Equipo
    template_name="equipo_detalle.html"
    context_object_name="equipo"
    
@method_decorator(staff_member_required, name='dispatch')
class EquipoCreate(CreateView):
    model= Equipo
    template_name="equipo_crear.html"
    fields=('__all__')
    success_url="/app-profi/lista-equipos/"

@method_decorator(staff_member_required, name='dispatch')
class EquipoUpdate(UpdateView):
    model= Equipo
    template_name="equipo_actualizar.html"
    fields= ('__all__')
    success_url="/app-profi/lista-equipos/"

@method_decorator(staff_member_required, name='dispatch')
class EquipoDelete(DeleteView):
    model= Equipo
    template_name="equipo_eliminar.html"
    success_url= "/app-profi/lista-equipos/"

class JugadorList(ListView):
    model= Jugador
    template_name="jugador_list.html"
    context_object_name="jugadores"

class JugadorDetail(DetailView):
    model= Jugador
    template_name="jugador_detalle.html"
    context_object_name="jugador"

@method_decorator(staff_member_required, name='dispatch')
class JugadorCreate(CreateView):
    model= Jugador
    template_name="jugador_crear.html"
    fields=('__all__')
    success_url="/app-profi/lista-jugadores/"

@method_decorator(staff_member_required, name='dispatch')
class JugadorUpdate(UpdateView):
    model= Jugador
    template_name="jugador_actualizar.html"
    fields= ('__all__')
    success_url="/app-profi/lista-jugadores/"

@method_decorator(staff_member_required, name='dispatch')
class JugadorDelete(DeleteView):
    model= Jugador
    template_name="jugador_eliminar.html"
    success_url= "/app-profi/lista-jugadores/"

class EntrenadorList(ListView):
    model= Entrenador
    template_name="entrenador_list.html"
    context_object_name="entrenadores"

class EntrenadorDetail(DetailView):
    model= Entrenador
    template_name="entrenador_detalle.html"
    context_object_name="entrenador"

@method_decorator(staff_member_required, name='dispatch')
class EntrenadorCreate(CreateView):
    model= Entrenador
    template_name="entrenador_crear.html"
    fields=('__all__')
    success_url="/app-profi/lista-entrenadores/"

@method_decorator(staff_member_required, name='dispatch')
class EntrenadorUpdate(UpdateView):
    model= Entrenador
    template_name="entrenador_actualizar.html"
    fields= ('__all__')
    success_url="/app-profi/lista-entrenadores/"

@method_decorator(staff_member_required, name='dispatch')
class EntrenadorDelete(DeleteView):
    model= Entrenador
    template_name="entrenador_eliminar.html"
    success_url= "/app-profi/lista-entrenadores/"


def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data= miFormulario.cleaned_data
            usuario= data["username"]
            psw= data["password"]
            user= authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(req, "index.html", {"mensaje": "Datos incorrectos"})
            
        else:
            return render(req, "index.html", {"mensaje": "Formulario inválido"})
        
    else:
        miFormulario= AuthenticationForm()
        return render(req, "login.html", {"miFomulario": miFormulario})

def register(req):

    if req.method == 'POST':

        miFormulario = UserCreationForm(req.POST)
        if miFormulario.is_valid():
            data= miFormulario.cleaned_data
            usuario= data["username"]
            miFormulario.save()
            return render(req, "index.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})
        else:
            return render(req, "index.html", {"mensaje": "Formulario inválido"})
    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFomulario": miFormulario})
    
def editar_perfil(req):

    usuario= req.user

    try:
        if req.method == 'POST':

            miFormulario = UserEditForm(req.POST, instance=req.user)

            if miFormulario.is_valid():
                
                data = miFormulario.cleaned_data
                usuario.first_name= data["first_name"]
                usuario.last_name= data["last_name"]
                usuario.email= data["email"]
                usuario.set_password(data["password1"])
                usuario.save()
                return render(req, "index.html", {"mensaje": "Perfil actualizado con éxito"})
            else:
                return render(req, "editar_perfil.html", {"miFomulario": miFormulario})
        else:
            miFormulario= UserEditForm(instance=req.user)
            return render(req, "editar_perfil.html", {"miFomulario": miFormulario})
    except:
        return render(req,"index.html",{"mensaje":"Debes logearte primero."})

    
class AvatarEdit(UpdateView):

    model= Avatar
    template_name="editar_avatar.html"
    fields= ("imagen",)
    success_url="/app-profi/editar-perfil/"


class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self,req,*args,**kwargs):
        return super(StaffRequiredMixin,self.dispatch(req,*args,**kwargs))
    




