from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Laboratorio)

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    ordering = ('id',)

@admin.register(DirectorGeneral)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','laboratorio')
    ordering = ('id',)
    
@admin.register(Producto)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','laboratorio')
    ordering = ('id',)