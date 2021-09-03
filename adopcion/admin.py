from django.contrib import admin
from .models import Post#, Especie, Mascota

""" class MascotasInline(admin.TabularInline):
    model = Mascota """

class PostAdmin(admin.ModelAdmin):
    list_display = ('fecha_publi', 'descripcion', 'contacto', 'disponibilidad', 'autor', 'tipo', 'nombre', 'raza', 'medida')
    list_filter = ('fecha_publi', 'disponibilidad', 'autor', 'tipo', 'nombre', 'raza', 'medida')
    
    #inlines = [MascotasInline]

""" class EspecieAdmin(admin.ModelAdmin):
    list_display = ('tipo',)

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'medida', 'especie', 'post')
    list_filter = ('raza', 'medida', 'especie') """

admin.site.register(Post, PostAdmin)
""" admin.site.register(Especie, EspecieAdmin)
admin.site.register(Mascota, MascotaAdmin) """

