from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, render, redirect

from django.urls import reverse_lazy

from .models import Region, Usuario, SolicitudArriendo, Inmueble, Comuna
from .forms import RegionForm, UsuarioChangeForm, SolicitudArriendoForm, InmuebleForm

#                              CustomUserChangeForm,
from .forms import ComunaForm, UsuarioCreationForm
#                              RegistroUsuarioForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

#Vista del index
class Login(LoginView):
    template_name="registration/login.html"
    
class Logout(LogoutView):
    next_page="/"

def home(request):
    print("home")
    inmuebles = Inmueble.objects.all()
    return render(request, 'index.html',{'inmuebles': inmuebles})

def region_list_view(request):
    regions = Region.objects.all()
    return render(request, 'region_list.html', {'region-list': regions})


def region_detail_view(request, pk):
    region = get_object_or_404(Region, pk=pk)
    return render(request, 'region_detail.html', {'object': region})

def region_create_view(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('region-list'))
    else:
        form = RegionForm()
    return render(request, 'region_form.html', {'form': form})

def region_update_view(request, pk):
    region = get_object_or_404(Region, pk=pk)
    if request.method == 'POST':
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('region-list'))
    else:
        form = RegionForm(instance=region)
    return render(request, 'region_form.html', {'form': form})

def region_delete_view(request, pk):
    region = get_object_or_404(Region, pk=pk)
    if request.method == 'POST':
        region.delete()
        return redirect(reverse_lazy('region-list'))
    return render(request, 'region_confirm_delete.html', {'object': region})

#   Comunas

def comuna_create_view(request):
    if request.method == 'POST':
        form = ComunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comuna-list')  # Redirigir a la página de lista de comunas
    else:
        form = ComunaForm()
    return render(request, 'comuna_form.html', {'form': form})

def comuna_update_view(request, pk):
    comuna = get_object_or_404(Comuna, pk=pk)
    if request.method == 'POST':
        form = ComunaForm(request.POST, instance=comuna)
        if form.is_valid():
            form.save()
            return redirect('comuna-list')
    else:
        form = ComunaForm(instance=comuna)
    return render(request, 'comuna_form.html', {'form': form})


#     Vistas Usuario

def usuario_list_view(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario_list.html', {'object_list': usuarios})

def usuario_detail_view(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuario_detail.html', {'object': usuario})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        print(form)
        if form.is_valid():
            usuario = form.save(commit=False)
            password = form.cleaned_data['password']
            usuario.set_password(password)
            usuario.save()
#           form.save()
            # Autenticar al usuario después del registro
            usuario_autenticado = authenticate(username=usuario.username, password=password)
            if usuario_autenticado is not None:
                  login(request, usuario_autenticado)
#                 return redirect('index') 
                  return redirect(reverse_lazy('usuario-list'))
    else:
        form = UsuarioCreationForm()
    
    return render(request, 'usuario_form.html', {'form': form})

@login_required
def usuario_update_view(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Los datos del usuario han sido actualizados!')
            return redirect(reverse_lazy('dashboard'))
        else: 
            messages.error(request, "Hay un error")
    else:
        form = UsuarioChangeForm(instance=request.user)
        
    return render(request, 'perfil.html', {'form': form})

# @login_required
# def actualizar_usuario(request):
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=request.user.usuario)
#         print(form)
#         if form.is_valid():
#             form.save()
#             messages.success(request, '¡Los datos del usuario han sido actualizados!')
#             return redirect('dashboard') 
#     else:
#         form = CustomUserChangeForm(instance=request.user.usuario)
#     return render(request, 'perfil.html', {'form': form})
    
  

def usuario_delete_view(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, '¡Los datos del usuario han sido eliminados!')
        return redirect(reverse_lazy('dashboard'))
    

    return render(request, 'usuario_confirm_delete.html', {'usuario': usuario})

#   Inmueble

def inmueble_list_view(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmueble_list.html', {'inmuebles': inmuebles})

@login_required
def inmueble_detail_view(request, pk):
   # inmueble = get_object_or_404(Inmueble, pk=pk)
    inmueble = Inmueble.objects.get(pk=pk)
    return render(request, 'inmueble_detail.html', {'inmueble': inmueble})


# @login_required
# def detalle_inmueble(request, id):
#     inmueble = Inmueble.objects.get (pk=id)
#     return render(request,'detalle_inmueble.html',{'inmueble':inmueble})

@login_required
def inmueble_create_view(request):
    #print("Entre a la funcion")
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    #print(request.method)
    if request.method == 'POST':

        #print("Entre al if")
        form = InmuebleForm(request.POST, request.FILES)
        #print(form)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user  # Asigna el usuario actual como propietario
            inmueble.save()
            #print("Entre al segundo if")
            # form.save()   
            return redirect('dashboard')
    else:
        #print("Entre al else")
        form = InmuebleForm()
    #print("Sali del if")
    return render(request, 'inmueble_form.html', {'regiones': regiones, 'comunas': comunas})

#revisar
# @login_required
# def crear_inmueble(request):
#     if request.method == 'POST':
#         form = InmuebleForm(request.POST, request.FILES)
#         print(form)
#         if form.is_valid():
#             inmueble = form.save(commit=False)
#             inmueble.propietario = request.user.usuario
#             inmueble.save()
#             return redirect('dashboard') 
#     else:
#         form = InmuebleForm()
#     return render(request, 'alta_inmueble.html', {'form': form})

def inmueble_update_view(request, pk):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    inmueble = get_object_or_404(Inmueble, pk=pk)
    
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user  # Asumiendo que el usuario autenticado es el propietario
            inmueble.save()
            return redirect('dashboard')
        # if form.is_valid():
        #     form.save()
        #     return redirect('dashboard')
    else:
        form = InmuebleForm(instance=inmueble)
    # return render(request, 'editar_inmueble.html', {'form': form})
    return render(request, 'editar_inmueble.html', {'form':form, 'regiones': regiones, 'comunas': comunas})

@login_required
def inmueble_delete_view(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    
    if request.method == 'POST':
        inmueble.delete()
        return redirect('dashboard') #inmueble-list=dashboard
    else:        
        return render(request, 'eliminar_inmueble.html', {'inmueble': inmueble})
    
# @login_required
# def eliminar_inmueble(request, id):
#     inmueble = get_object_or_404(Inmueble, pk=id)
#     if request.method == 'POST':
#         inmueble.delete()
#         return redirect('dashboard')
#     else:
#         return render(request,'eliminar_inmueble.html', {'inmueble':inmueble} )

# Funciones de solicitud de arriendo AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
@login_required
def dashboard(request):
      if request.user.tipo_usuario == 'arrendatario':
          solicitudes = SolicitudArriendo.objects.filter(arrendatario=request.user)
          regiones = Region.objects.all()
          comunas = Comuna.objects.all()
          region_id = request.GET.get('region')
          comuna_id = request.GET.get('comuna')
          inmuebles = Inmueble.objects.all()
          if region_id:
              inmuebles = inmuebles.filter(comuna__region_id=region_id)
          if comuna_id:
              inmuebles = inmuebles.filter(comuna_id=comuna_id)
        
          return render(request, 'dashboard_arrendatario.html', {'solicitudes': solicitudes, 'regiones': regiones, 'comunas': comunas, 'inmuebles': inmuebles})
    
      elif request.user.tipo_usuario == 'arrendador':
          # Obtener las solicitudes recibidas por el arrendador
          solicitudes_recibidas = SolicitudArriendo.objects.filter(inmueble__propietario=request.user)
          # Obtener los inmuebles del arrendador
          inmuebles = Inmueble.objects.filter(propietario=request.user)
          return render(request, 'dashboard_arrendador.html', {'solicitudes_recibidas': solicitudes_recibidas, 'inmuebles': inmuebles})

#   Solicitud de Arriendo
def solicitud_arriendo_list_view(request):
    solicitudes_arriendo = SolicitudArriendo.objects.all()
    return render(request, 'solicitud_list.html', {'solicitudes_arriendo': solicitudes_arriendo})


def solicitud_arriendo_detail_view(request, pk):
    solicitud_arriendo = get_object_or_404(SolicitudArriendo, pk=pk)
    return render(request, 'solicitud_detail.html', {'solicitud_arriendo': solicitud_arriendo})

# def solicitud_arriendo_create_view(request):
#     if request.method == 'POST':
#         form = SolicitudArriendoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('solicitud-list')
#     else:
#         form = SolicitudArriendoForm()
#     return render(request, 'solicitud_form.html', {'form': form})

@login_required
def generar_solicitud_arriendo(request, id):
    # Obtener el inmueble por su ID
    inmueble = get_object_or_404(Inmueble, pk=id)
    
    # Verificar si el usuario está autenticado y es un arrendatario
    if request.user.is_authenticated and request.user.tipo_usuario == 'arrendatario':
        if request.method == 'POST':
            form = SolicitudArriendoForm(request.POST)
            if form.is_valid():
                solicitud = form.save(commit=False)
                solicitud.arrendatario = request.user  # Asignar el usuario arrendatario
                solicitud.inmueble = inmueble
                solicitud.save()
                return redirect('detalle', id=inmueble.id)
        else:
            # Inicializar el formulario con el inmueble correspondiente
            form = SolicitudArriendoForm(initial={'inmueble': inmueble})
        return render(request, 'generar_solicitud_arriendo.html', {'form': form})
    else:
        return redirect('index')

def solicitud_arriendo_update_view(request, pk):
    solicitud_arriendo = get_object_or_404(SolicitudArriendo, pk=pk)
    if request.method == 'POST':
        form = SolicitudArriendoForm(request.POST, instance=solicitud_arriendo)
        if form.is_valid():
            form.save()
            return redirect('solicitud-list')
    else:
        form = SolicitudArriendoForm(instance=solicitud_arriendo)
    return render(request, 'solicitud_form.html', {'form': form})

def solicitud_arriendo_delete_view(request, pk):
    solicitud_arriendo = get_object_or_404(SolicitudArriendo, pk=pk)
    
    if request.method == 'POST':
        solicitud_arriendo.delete()
        return redirect('solicitud-list')
    
    return render(request, 'solicitud_confirm_delete.html', {'solicitud_arriendo': solicitud_arriendo})

@login_required
def solicitudes_arrendador(request):
#     Verificar si el usuario es un arrendador
      if request.user.tipo_usuario == 'arrendador':
         # Obtener todas las solicitudes recibidas por el arrendador
          solicitudes = SolicitudArriendo.objects.filter(inmueble__propietario=request.user)
          return render(request, 'solicitudes_arrendador.html', {'solicitudes': solicitudes})
      else:
          # Redirigir a otra página si el usuario no es un arrendador
          return redirect('index')  

