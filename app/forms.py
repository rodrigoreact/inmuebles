from django import forms
from .models import Contacto, Usuario, SolicitudArriendo, Inmueble, Region, Comuna
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

# y porqué importa el modelo de User

# from django.contrib.auth.models import User si estuviera usando User por defecto que viene con Django

class UsuarioCreationForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'nombres', 'apellidos', 'rut', 'direccion', 'telefono', 'tipo_usuario', 'email']
        
        widgets = {
            #'password': forms.PasswordInput(),         
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
        }   

class MyForm(forms.Form):
    apellidos = forms.CharField(label='Apellido(s)', max_length=100)

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'direccion', 'descripcion', 'imagen', 'precio', 'comuna', 'disponible', 'm2_construidos', 'm2_terreno', 'cantidad_estacionamientos', 'cantidad_habitaciones', 'cantidad_banos', 'tipo_de_inmueble']
        # widgets = {
        #     'disponible': forms.CheckboxInput()
        # }
class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = ['username', 'nombres', 'apellidos', 'rut', 'direccion', 'telefono', 'tipo_usuario', 'email']


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['nombre']

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['nombre', 'region']


class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ['inmueble', 'mensaje']        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields= ['name', 'email', 'message', 'contact_type', 'suscription']

# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = Usuario
#         fields = ['nombres', 'apellidos', 'email']