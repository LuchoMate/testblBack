from django.urls import path
from . import views

urlpatterns = [
   path('getcontactos', views.api_getContactos, name="getcontactos"),
   path('crearcontacto', views.api_crearContacto, name="crearcontacto"),
   path('actualizarcontacto/<int:contactoId>', views.api_actualizarContacto, name="actualizarcontacto"),
   path('borrarcontacto/<int:contactoId>', views.api_borrarContacto, name="borrarcontacto"),
   
]