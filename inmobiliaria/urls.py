from django.contrib import admin
# from Hito2.app.models import contacto
from inmobiliaria import settings
from django.urls import path, include
from django.conf.urls.static import static

from app.views import *
  
urlpatterns = [
    path('' ,home, name='home'),
    path('admin/', admin.site.urls),    
    #   Regiones es region o regiones
    path('regiones/', region_list_view, name='region-list'), 
    path('regiones/<int:pk>/', region_detail_view, name='region-detail'),    
    path('regiones/create/', region_create_view, name='region_create'),
    path('regiones/<int:pk>/update/', region_update_view, name='region_update'), 
    path('regiones/<int:pk>/delete/', region_delete_view, name='region_delete'),


    #   Comunas
    path('comunas/nueva/', comuna_create_view, name='comuna-create'),
    # si no he creado esta vista no debe estar path('comunas/', comuna_list_view, name='comuna-list'),   
    # path('comunas/<int:pk>/', comuna_detail_view, name='comuna-detail'), 
    path('comunas/<int:pk>/editar/', comuna_update_view, name='comuna-update'),
    # path('comunas/<int:pk>/eliminar/', comuna_delete_view, name='comuna-delete'),
    
    #    Usuarios
   
    path('usuarios/', usuario_list_view, name='usuario-list'),
    path('usuarios/<int:pk>/', usuario_detail_view, name='usuario-detail'),
    path('usuarios/crear/', crear_usuario, name='crear-usuario'),    
    path('perfil/<int:pk>/', usuario_update_view, name='usuario-update'),
 

    path('dashboard/', dashboard, name='dashboard'),
    path('usuarios/<int:pk>/delete/', usuario_delete_view, name='usuario-delete'),    
    path('accounts/', include('django.contrib.auth.urls')),
    
    #    Inmuebles
         
    path('inmuebles/', inmueble_list_view, name='inmueble-list'),
    path('inmuebles/<int:id>/generar-solicitud/', generar_solicitud_arriendo, name='generar_solicitud_arriendo'),
    path('inmuebles/<int:pk>/', inmueble_detail_view, name='inmueble-detail'),
    # path('inmuebles/crear/', inmueble_create_view, name='inmueble-create'),
    path('alta-inmueble/', inmueble_create_view, name='alta_inmueble'),
    path('inmuebles/<int:pk>/editar/', inmueble_update_view, name='inmueble-update'), 
    path('inmuebles/<int:pk>/eliminar/', inmueble_delete_view, name='inmueble-delete'),
   
    #    Solicitudes
  
    path('solicitudes-arriendo/', solicitud_arriendo_list_view, name='solicitud-arriendo-list'),
    path('solicitudes-arriendo/<int:pk>/', solicitud_arriendo_detail_view, name='solicitud-arriendo-detail'),
    path('solicitudes-arriendo/crear/', generar_solicitud_arriendo, name='solicitud-arriendo-create'),
    path('solicitudes/', solicitudes_arrendador, name='solicitudes_arrendador'),
    path('solicitudes-arriendo/<int:pk>/editar/', solicitud_arriendo_update_view, name='solicitud-arriendo-update'),
    path('solicitudes-arriendo/<int:pk>/eliminar/', solicitud_arriendo_delete_view, name='solicitud-arriendo-delete'),
      
   

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
