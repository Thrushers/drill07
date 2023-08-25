from django.contrib import admin
from django.urls import path
from .views import *
 

urlpatterns = [
    path('', index, name= 'tabla'),
    path('ingresar',vista, name = 'vista'),
    path('editar/<int:pk>', editar, name='editar'),
    path('editar/actualizareditar/<int:id>', actualizareditar, name='actualizareditar'),
    path('eliminar/<int:pk>', eliminar, name='eliminar'),
]